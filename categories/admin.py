from django.contrib import admin
from categories.models import Category,SubCat
from cms.admin.placeholderadmin import PlaceholderAdminMixin
# Register your models here.
#
class CategoriesAdmin(PlaceholderAdminMixin, admin.ModelAdmin):
    pass

admin.site.register(Category, CategoriesAdmin)

class SubCatAdmin(PlaceholderAdminMixin, admin.ModelAdmin):
    pass

admin.site.register(SubCat, SubCatAdmin)