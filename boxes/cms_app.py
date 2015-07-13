from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from django.utils.translation import ugettext_lazy as _


class BoxesApp(CMSApp):
    name = _("Boxes App")  # give your app a name, this is required
    urls = ["boxes.urls"]  # link your app to url configuration(s)
    app_name = "boxes"

apphook_pool.register(BoxesApp)  # register your app
