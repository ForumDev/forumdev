from django.contrib import admin
from boxes.models import Box
from cms.admin.placeholderadmin import PlaceholderAdminMixin
# Register your models here.
#
class BoxesAdmin(PlaceholderAdminMixin, admin.ModelAdmin):
    pass

admin.site.register(Box, BoxesAdmin)

