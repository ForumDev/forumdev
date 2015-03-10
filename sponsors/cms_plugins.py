from cms.plugin_base import CMSPluginBase
from cms.models.pluginmodel import CMSPlugin
from cms.plugin_pool import plugin_pool
from sponsors import models
from django.utils.translation import ugettext as _
from django.contrib.sites.models import Site

class Sponsors(CMSPluginBase):
    model = CMSPlugin  # Model where data about this plugin is saved
    module = _("Sponsors")
    name = _("Sponsors Plugin")  # Name of the plugin
    render_template = "sponsors/sponsors.html"  # template to render the plugin with
    
    def render(self, context, instance, placeholder):
        context['sponsors'] = models.Sponsor.objects.all
        context['site'] = Site.objects.get_current()
        return context

plugin_pool.register_plugin(Sponsors)  # register the plugin

