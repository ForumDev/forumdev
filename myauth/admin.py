from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as AuthUserAdmin
from cms.admin.placeholderadmin import PlaceholderAdminMixin
 
from myauth.models import User, Interest
from myauth.forms import UserCreationForm, UserChangeForm
 
class InterestsAdmin(PlaceholderAdminMixin, admin.ModelAdmin):
    pass

admin.site.register(Interest, InterestsAdmin)

class UserAdmin(AuthUserAdmin):
  fieldsets = (
#     (None, {'fields': ('username', 'password', 'receive_newsletter')}),
    ('Personal info', {'fields': ('first_name', 'last_name', 'username', 'password', 'email'
                                  ,'telephone','affiliation','department','address','bill_address')}),
    ('More about yourself', {'fields': ('avatar','gender', 'research_status'
                                        , 'research_field', 'supervisor','short_bio'
                                        #, 'interests'
                                        )}),
    ('Social networking', {'fields': ('twitter','google_plus', 'facebook'
                                      , 'personal_email', 'news_feed','google_scholar','orcid_id')}),
    ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser',
                    #'groups'#, 'user_permissions'
                    )}),
    ('Important dates', {'fields': ('last_login', 'date_joined')}),
  )
  add_fieldsets = (
   ('Personal info', {'fields': ('first_name', 'last_name', 'username', 'password1', 'password2', 'email'
              ,'telephone','affiliation','department','address','bill_address')}),
    ('More about yourself', {'fields': ('avatar','gender', 'research_status'
                                        , 'research_field', 'supervisor','short_bio'
                                        #, 'interests'
                                        )}),
    ('Social networking', {'fields': ('twitter','google_plus', 'facebook'
                                      , 'personal_email', 'news_feed','publication_feed')}),
    ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser',
                    #'groups'#, 'user_permissions'
                    )}),
  )
  form = UserChangeForm
  add_form = UserCreationForm
  list_display = ('username', 'first_name', 'last_name', 'email')
  list_editable = ('first_name', 'last_name', 'email')
  list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups', 'receive_newsletter')
  search_fields = ('username', 'last_name', 'first_name', 'email','affiliation','department','research_field')
  ordering = ('last_name','first_name')
 
 
admin.site.register(User, UserAdmin)
