from django.contrib import admin
from logos.models import Logo
from cms.admin.placeholderadmin import PlaceholderAdminMixin
# Register your models here.
#
class LogosAdmin(PlaceholderAdminMixin, admin.ModelAdmin):
    pass

admin.site.register(Logo, LogosAdmin)
