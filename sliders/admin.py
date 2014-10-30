from django.contrib import admin
from sliders.models import Slider
from cms.admin.placeholderadmin import PlaceholderAdminMixin
# Register your models here.

class SliderAdmin(PlaceholderAdminMixin, admin.ModelAdmin):
    pass

admin.site.register(Slider, SliderAdmin)