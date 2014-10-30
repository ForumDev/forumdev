from cms.plugin_base import CMSPluginBase
from cms.models.pluginmodel import CMSPlugin
from cms.plugin_pool import plugin_pool
from publications import models
from django.utils.translation import ugettext as _


class Publications(CMSPluginBase):
    model = CMSPlugin  # Model where data about this plugin is saved
    module = _("Publications")
    name = _("Publications Plugin")  # Name of the plugin
    render_template = "publications/publications.html"  # template to render the plugin with

    def render(self, context, instance, placeholder):
        context['publications'] = models.Publication.objects.all
        return context

plugin_pool.register_plugin(Publications)  # register the plugin

