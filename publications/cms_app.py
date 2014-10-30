from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from django.utils.translation import ugettext_lazy as _


class PublicationsApp(CMSApp):
    name = _("Publications")  # give your app a name, this is required
    urls = ["publications.urls"]  # link your app to url configuration(s)
    app_name = "publications"

apphook_pool.register(PublicationsApp)  # register your app
