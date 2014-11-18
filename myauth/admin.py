from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as AuthUserAdmin
 
from myauth.models import User
from myauth.forms import UserCreationForm, UserChangeForm
 
class UserAdmin(AuthUserAdmin):
  fieldsets = (
    (None, {'fields': ('username', 'password', 'receive_newsletter')}),
    ('Personal info', {'fields': ('short_name', 'full_name', 'email', 'avatar')}),
    ('Academic info', {'fields': ('affiliation', 'research_status', 'research_field', 'interests')}),
    ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser',
                    'groups', 'user_permissions')}),
    ('Important dates', {'fields': ('last_login', 'date_joined')}),
  )
  add_fieldsets = (
    (None, {'fields': ('username', 'password1', 'password2', 'receive_newsletter')}),
    ('Personal info', {'fields': ('short_name', 'full_name', 'email', 'avatar')}),
    ('Academic info', {'fields': ('affiliation', 'research_status', 'research_field', 'interests')}),
    ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
  )
  form = UserChangeForm
  add_form = UserCreationForm
  list_display = ('username', 'email', 'short_name', 'affiliation', 'full_name', 'is_active', 'is_staff', 'receive_newsletter')
  list_editable = ('is_active','receive_newsletter')
  list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups', 'receive_newsletter')
  search_fields = ('username', 'email', 'short_name', 'affiliation', 'full_name')
  ordering = ('full_name',)
 
 
admin.site.register(User, UserAdmin)
