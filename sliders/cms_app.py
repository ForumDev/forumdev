from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from django.utils.translation import ugettext_lazy as _


class SlidersApp(CMSApp):
    name = _("forumdev-Sliders")  # give your app a name, this is required
    urls = ["sliders.urls"]  # link your app to url configuration(s)
    app_name = "forumdev-sliders"

apphook_pool.register(SlidersApp)  # register your app
