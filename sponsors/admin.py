from django.contrib import admin
from sponsors.models import Sponsor
from cms.admin.placeholderadmin import PlaceholderAdminMixin
# Register your models here.

class SponsorAdmin(PlaceholderAdminMixin, admin.ModelAdmin):
    pass

admin.site.register(Sponsor, SponsorAdmin)