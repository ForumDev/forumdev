from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from django.utils.translation import ugettext_lazy as _


class SponsorsApp(CMSApp):
    name = _("Sponsors App")  # give your app a name, this is required
    urls = ["sponsors.urls"]  # link your app to url configuration(s)
    app_name = "sponsors"

apphook_pool.register(SponsorsApp)  # register your app
