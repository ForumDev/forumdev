from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from django.utils.translation import ugettext_lazy as _


class LogosApp(CMSApp):
    name = _("Logos App")  # give your app a name, this is required
    urls = ["logos.urls"]  # link your app to url configuration(s)
    app_name = "logos"

apphook_pool.register(LogosApp)  # register your app
