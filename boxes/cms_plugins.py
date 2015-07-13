from cms.plugin_base import CMSPluginBase
from cms.models.pluginmodel import CMSPlugin
from cms.plugin_pool import plugin_pool
from boxes import models
from django.utils.translation import ugettext as _


class Boxes(CMSPluginBase):
    model = CMSPlugin  # Model where data about this plugin is saved
    module = _("ForumdevBoxes")
    name = _("ForumdevBoxes Plugin")  # Name of the plugin
    render_template = "boxes/boxes.html"  # template to render the plugin with

    def render(self, context, instance, placeholder):
        context.update({'instance': instance
            , 'boxes': models.Box.objects.all})
        return context

plugin_pool.register_plugin(Boxes)  # register the plugin

