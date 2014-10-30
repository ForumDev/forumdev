# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _

from cms.toolbar_pool import toolbar_pool
from cms.toolbar_base import CMSToolbar

from . import request_post_identifier
from .models import Post


@toolbar_pool.register
class BlogToolbar(CMSToolbar):
    watch_models = (Post, )

    def populate(self):
        if not (self.is_current_app and self.request.user.has_perm('aldryn_blog.add_post')):
            return
        menu = self.toolbar.get_or_create_menu('blog-app', _('News'))
        menu.add_modal_item(_('Add News Post'), reverse('admin:aldryn_blog_post_add'))

        blog_entry = getattr(self.request, request_post_identifier, None)
        if blog_entry and self.request.user.has_perm('aldryn_blog.change_post'):
            menu.add_modal_item(_('Edit News Post'), reverse('admin:aldryn_blog_post_change', args=(blog_entry.pk,)),
                                active=True)
