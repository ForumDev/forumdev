from cms.plugin_base import CMSPluginBase
from cms.models.pluginmodel import CMSPlugin
from cms.plugin_pool import plugin_pool
from logos import models
from django.utils.translation import ugettext as _
from django.contrib.sites.models import Site


class Logos(CMSPluginBase):
    model = CMSPlugin  # Model where data about this plugin is saved
    module = _("Logo")
    name = _("Logo Plugin")  # Name of the plugin
    render_template = "logos/logo.html"  # template to render the plugin with

    def render(self, context, instance, placeholder):
        context['logos'] = models.Logo.objects.all
        context['site'] = Site.objects.get_current()
        return context

plugin_pool.register_plugin(Logos)  # register the plugin

