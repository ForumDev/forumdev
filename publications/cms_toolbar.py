#from django.core.urlresolvers import reverse
#from django.utils.translation import ugettext_lazy as _
#from cms.toolbar_pool import toolbar_pool
#from cms.toolbar_base import CMSToolbar
#
#@toolbar_pool.register
#class PubToolbar(CMSToolbar):
#
#    def populate(self):
#        if self.is_current_app:
#            menu = self.toolbar.get_or_create_menu('pubs-app', _('Publications'))
#            url = '../admin/publications'
#            menu.add_sideframe_item(_('Publication admin'), url=url)