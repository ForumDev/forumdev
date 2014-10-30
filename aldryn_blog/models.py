# -*- coding: utf-8 -*-
import datetime
from collections import Counter

from django.core.exceptions import ImproperlyConfigured
from django.core.urlresolvers import reverse, NoReverseMatch
from django.db import models
from django.db.models import Q
from django.template.defaultfilters import slugify
from django.utils import timezone
from django.utils.translation import get_language, ugettext_lazy as _, override

from app_data import AppDataField
from cms.utils.i18n import get_current_language
from cms.models.fields import PlaceholderField
from cms.models.pluginmodel import CMSPlugin
from djangocms_text_ckeditor.fields import HTMLField
from filer.fields.image import FilerImageField
from hvad.models import TranslationManager, TranslatableModel, TranslatedFields
from taggit.managers import TaggableManager
from taggit.models import TaggedItem, Tag

from .conf import settings
from .utils import generate_slugs, get_blog_authors, get_slug_for_user, get_slug_in_language


AUTH_USER_MODEL = getattr(settings, 'AUTH_USER_MODEL', 'auth.User')


class CategoryManager(TranslationManager):

    def get_with_usage_count(self, language=None, **kwargs):
        categories = list(self.language(language).filter(**kwargs).distinct())

        # No annotate in hvad
        for category in categories:
            category.post_count = category.post_set.count()
        return sorted(categories, key=lambda x: -x.post_count)


class Category(TranslatableModel):

    translations = TranslatedFields(
        name=models.CharField(_('Name'), max_length=255),
        slug=models.SlugField(
            verbose_name=_('Slug'),
            max_length=255,
            blank=True,
            help_text=_('Auto-generated. Clean it to have it re-created. '
                        'WARNING! Used in the URL. If changed, the URL will change. ')
        ),
        meta={'unique_together': [['slug', 'language_code']]}
    )

    ordering = models.IntegerField(_('Ordering'), default=0)

    objects = CategoryManager()

    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')
        ordering = ['ordering']

    def __unicode__(self):
        return self.lazy_translation_getter('name', str(self.pk))

    def get_absolute_url(self, language=None):
        language = language or get_current_language()
        slug = get_slug_in_language(self, language)
        with override(language):
            if slug:
                return reverse('aldryn_blog:category-posts', kwargs={'category': slug})

            # category not translated in given language
            try:
                return reverse('aldryn_blog:latest-posts')
            except (ImproperlyConfigured, NoReverseMatch):
                return '/%s' % language


class RelatedManager(models.Manager):

    def get_query_set(self):
        qs = super(RelatedManager, self).get_query_set()
        return qs.select_related('key_visual')

    def filter_by_language(self, language):
        qs = self.get_query_set()
        return qs.filter(Q(language__isnull=True) | Q(language=language))

    def filter_by_current_language(self):
        return self.filter_by_language(get_language())

    def get_tags(self, entries=None, language=None):
        """Returns tags used to tag post and its count. Results are ordered by count."""

        if not entries:
            entries = self

        if language:
            entries = entries.filter_by_language(language)
        entries = entries.distinct()
        if not entries:
            return []
        kwargs = TaggedItem.bulk_lookup_kwargs(entries)

        # aggregate and sort
        counted_tags = dict(TaggedItem.objects
                                      .filter(**kwargs)
                                      .values('tag')
                                      .annotate(count=models.Count('tag'))
                                      .values_list('tag', 'count'))

        # and finally get the results
        tags = Tag.objects.filter(pk__in=counted_tags.keys())
        for tag in tags:
            tag.count = counted_tags[tag.pk]
        return sorted(tags, key=lambda x: -x.count)

    def get_categories(self, language=None):
        """
        Returns all categories used in posts and the amount, ordered by amount.
        """

        entries = (self.filter_by_language(language) if language else self).distinct()
        if not entries:
            return Category.objects.none()

        return Category.objects.filter(post__in=entries).annotate(count=models.Count('post')).order_by('-count')

    def get_months(self, language):
        """Get months with aggregatet count (how much posts is in the month). Results are ordered by date."""
        # done via naive way as django's having tough time while aggregating on date fields
        entries = self.filter_by_language(language)
        dates = entries.values_list('publication_start', flat=True)
        dates = [(x.year, x.month) for x in dates]
        date_counter = Counter(dates)
        dates = set(dates)
        dates = sorted(dates, reverse=True)
        return [{'date': datetime.date(year=year, month=month, day=1),
                 'count': date_counter[year, month]} for year, month in dates]


class PublishedManager(RelatedManager):

    def get_query_set(self):
        qs = super(PublishedManager, self).get_query_set()
        now = timezone.now()
        qs = qs.filter(publication_start__lte=now)
        qs = qs.filter(Q(publication_end__isnull=True) | Q(publication_end__gte=now))
        return qs


class Post(models.Model):

    title = models.CharField(_('Title'), max_length=255)
    slug = models.SlugField(
        verbose_name=_('Slug'),
        max_length=255,
        unique=True,
        blank=True,
        help_text=_('Used in the URL. If changed, the URL will change. Clean it to have it re-created.')
    )
    language = models.CharField(
        verbose_name=_('language'),
        max_length=5,
        null=True,
        blank=True,
        choices=settings.LANGUAGES,
        help_text=_('leave empty to display in all languages')
    )
    key_visual = FilerImageField(verbose_name=_('Key Visual'), blank=True, null=True)
    lead_in = HTMLField(
        verbose_name=_('Lead-in'),
        help_text=_('Will be displayed in lists, and at the start of the detail page (in bold)')
    )
    content = PlaceholderField('aldryn_blog_post_content', related_name='aldryn_blog_posts')
    author = models.ForeignKey(to=AUTH_USER_MODEL, verbose_name=_('Author'))
    coauthors = models.ManyToManyField(
        to=AUTH_USER_MODEL,
        verbose_name=_('Co-Authors'),
        null=True,
        blank=True,
        related_name='aldryn_blog_coauthors'
    )
    publication_start = models.DateTimeField(
        verbose_name=_('Published Since'),
        default=timezone.now,
        help_text=_('Used in the URL. If changed, the URL will change.')
    )
    publication_end = models.DateTimeField(
        verbose_name=_('Published Until'),
        null=True,
        blank=True
    )
    category = models.ForeignKey(
        to=Category,
        verbose_name=_('Category'),
        null=True,
        blank=True
    )

    objects = RelatedManager()
    published = PublishedManager()
    tags = TaggableManager(blank=True)
    app_data = AppDataField()

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        kwargs = {
            'year': self.publication_start.year,
            'month': self.publication_start.month,
            'day': self.publication_start.day,
            'slug': self.slug
        }

        if self.language and not getattr(settings, 'ALDRYN_BLOG_SHOW_ALL_LANGUAGES', False):
            with override(self.language):
                return reverse('aldryn_blog:post-detail', kwargs=kwargs)
        return reverse('aldryn_blog:post-detail', kwargs=kwargs)

    class Meta:
        ordering = ['-publication_start']

    def save(self, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super(Post, self).save(**kwargs)

    def get_author_slug(self):
        # FIXME: This is a potential performance hogger
        return get_slug_for_user(self.author)


class LatestEntriesPlugin(CMSPlugin):

    latest_entries = models.IntegerField(
        default=5,
        help_text=_('The number of latests entries to be displayed.')
    )
    tags = models.ManyToManyField(
        to='taggit.Tag',
        blank=True,
        help_text=_('Show only the blog posts tagged with chosen tags.')
    )

    def __unicode__(self):
        """
        must return a unicode string
        """
        return str(self.latest_entries).decode('utf8')

    def copy_relations(self, oldinstance):
        self.tags = oldinstance.tags.all()

    def get_posts(self):
        posts = Post.published.filter_by_language(self.language)
        tags = self.tags.values_list('pk', flat=True)

        if tags.exists():
            posts = posts.filter(tags__in=tags)
        return posts[:self.latest_entries]


class AuthorsPlugin(CMSPlugin):

    def get_authors(self):
        return generate_slugs(get_blog_authors())


def force_language(sender, instance, **kwargs):
    if issubclass(sender, CMSPlugin) and instance.placeholder \
            and instance.placeholder.slot == 'aldryn_blog_post_content':
        instance.language = settings.ALDRYN_BLOG_PLUGIN_LANGUAGE


for model in CMSPlugin.__subclasses__():
    models.signals.pre_save.connect(force_language, sender=model)
