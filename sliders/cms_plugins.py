from cms.plugin_base import CMSPluginBase
from cms.models.pluginmodel import CMSPlugin
from cms.plugin_pool import plugin_pool
from sliders import models
from django.utils.translation import ugettext as _


class Sliders(CMSPluginBase):
    model = CMSPlugin  # Model where data about this plugin is saved
    module = _("forumdev-Sliders")
    name = _("forumdev-Sliders Plugin")  # Name of the plugin
    render_template = "sliders/flexsliders.html"  # template to render the plugin with

    def render(self, context, instance, placeholder):
        context['sliders'] = models.Slider.objects.all
        return context

plugin_pool.register_plugin(Sliders)  # register the plugin

