from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from django.utils.translation import ugettext_lazy as _


class CategoriesApp(CMSApp):
    name = _("Categories App")  # give your app a name, this is required
    urls = ["categories.urls"]  # link your app to url configuration(s)
    app_name = "categories"

apphook_pool.register(CategoriesApp)  # register your app
