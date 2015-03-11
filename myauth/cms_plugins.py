from cms.plugin_base import CMSPluginBase
from cms.models.pluginmodel import CMSPlugin
from cms.plugin_pool import plugin_pool
from myauth import models
from django.utils.translation import ugettext as _
from django.contrib.sites.models import Site

class Users(CMSPluginBase):
    model = CMSPlugin  # Model where data about this plugin is saved
    module = _("UserList")
    name = _("User List")  # Name of the plugin
    render_template = "myauth/list.html"  # template to render the plugin with
    
    def render(self, context, instance, placeholder):
        context['users'] = models.User.objects.all
        context['site'] = Site.objects.get_current()
        return context

plugin_pool.register_plugin(Users)  # register the plugin

