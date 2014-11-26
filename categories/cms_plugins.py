from cms.plugin_base import CMSPluginBase
from cms.models.pluginmodel import CMSPlugin
from cms.plugin_pool import plugin_pool
from categories import models
from django.utils.translation import ugettext as _


class Categories(CMSPluginBase):
    model = models.CatSel  # Model where data about this plugin is saved
    module = _("NewmsCategories")
    name = _("NewmsCategories Plugin")  # Name of the plugin
    render_template = "categories/categories.html"  # template to render the plugin with

    def render(self, context, instance, placeholder):
        context.update({'instance': instance
            , 'cats': models.Category.objects.all
            , 'subcats': models.SubCat.objects.all})
        return context

plugin_pool.register_plugin(Categories)  # register the plugin

