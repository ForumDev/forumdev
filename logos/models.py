from django.db import models
from django.contrib.sites.models import Site
#from cms.models import Page
from cms.models import fields
# Create your models here.


class Logo(models.Model):
    title = models.TextField(max_length=30, default='', blank=True, null=True)
    description = models.TextField(max_length=100, default='', blank=True, null=True)
    url = models.URLField(blank=True, null=True, help_text="Link to an external page (will override page link)",)
    page = fields.PageField(
        verbose_name="page",
        help_text="Select an existing page to link to.",
        blank=True,
        null=True
    )
    image = models.ImageField("Logo image", upload_to="images/logo/", blank=False, null=False)
    sites = models.ManyToManyField(Site)
    def __str__(self):              # __unicode__ on Python 2
        return self.title
    def __unicode__(self):
        return self.title
    class Meta:
        verbose_name_plural = 'Logos'
    def link(self):
        if self.url:
            return self.url
        elif self.page:
            return self.page.get_absolute_url()
        else: return "#"

