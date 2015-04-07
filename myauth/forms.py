from django.contrib.auth.forms import UserCreationForm as AuthUserCreationForm, UserChangeForm as AuthUserChangeForm, AuthenticationForm,\
    ReadOnlyPasswordHashField
from django import forms
from django.db.models import Q

from crispy_forms.helper import FormHelper                                                
from crispy_forms.layout import Layout, HTML, Submit, Fieldset
 
from myauth.models import User, Registration, Interest
from django.forms.models import ModelChoiceField, SelectMultiple


class LoginFormMixin(object):
  
  username = forms.CharField(label = 'Username or e-mail', required=True)
  password  = forms.CharField(label = 'Password', widget = forms.PasswordInput, required = True)
 
  def clean(self):
    username = self.cleaned_data.get('username', '')
    password = self.cleaned_data.get('password', '')
    self.user = None
    users = User.objects.filter(Q(username=username)|Q(email=username))
    for user in users:
      if user.is_active and user.check_password(password):
        self.user = user
    if self.user is None:
      raise forms.ValidationError('Invalid username or password')
    # We are setting the backend here so you may (and should) remove the line setting it in myauth.views
    self.user.backend = 'django.contrib.auth.backends.ModelBackend'
    return self.cleaned_data

class LoginForm(LoginFormMixin, forms.Form):                           
         
  username = forms.CharField(label = 'Username or e-mail', required=True)
  password  = forms.CharField(label = 'Password', widget = forms.PasswordInput, required = True)

  def __init__(self, *args, **kwargs):                                                    
    super(LoginForm, self).__init__(*args, **kwargs)                                      
    self.helper = FormHelper()
    self.helper.form_method = 'post'
    self.helper.form_action = 'login'                                                    
    self.helper.form_class = 'form-horizontal'                                           
    self.helper.label_class = 'col-md-5'                                                 
    self.helper.field_class = 'col-md-6'
    self.helper.layout = Layout(
      'username', 'password',
      HTML('<div class="form-group"><div class="col-md-5"></div><div class="col-md-6">'),
      Submit('submit', 'Log in'),
      HTML('</div></div>'),
    )


class AuthLoginForm(LoginFormMixin, AuthenticationForm):
 
  # Because of the way Python's MRO works we have to redefine username which has been overridden by AuthenticationForm
  username = forms.CharField(label = 'Username or e-mail', required=True)
  this_is_the_login_form = forms.BooleanField(widget=forms.HiddenInput, initial=1, error_messages={'required': "Please log in again, because your session has expired."})
 
  def clean(self):
    cleaned_data = super(AuthLoginForm, self).clean()
    if self.user is not None:
      self.user_cache = self.user
    return cleaned_data


class UserCreationForm(AuthUserCreationForm):
 
  receive_newsletter = forms.BooleanField(required=False)
#   interests = ModelChoiceField(queryset=Interests.objects.all())
  class Meta:
    model = User
 
  ## This method is defined in django.contrib.auth.form.UserCreationForm and explicitly links to auth.models.User so we need to override it
  def clean_username(self):
    username = self.cleaned_data["username"]
    try:
      User._default_manager.get(username=username)
    except User.DoesNotExist:
      return username
    raise forms.ValidationError(
      self.error_messages['duplicate_username'],
      code='duplicate_username',
    )
 
 
class UserChangeForm(AuthUserChangeForm):
  password = ReadOnlyPasswordHashField(label='Password',
                                       help_text="""Raw passwords are not stored, use <a href=\"lost_password.html\">this form</a>.""")
  class Meta:
    # Since we are overriding Meta we have to re-tell it the model also
    model = User
    exclude = ['password1', 'password2']
 
  def __init__(self, *args, **kwargs):
    super(UserChangeForm, self).__init__(*args, **kwargs)
    self.helper = FormHelper()
    self.helper.form_method = 'post'
    self.helper.form_action = 'save'
    self.helper.form_class = 'form-horizontal'
    self.helper.label_class = 'col-md-5'
    self.helper.field_class = 'col-md-6'
    self.helper.layout = Layout(
      Fieldset('Personal info'
               ,'first_name','last_name','username', 'password'
               ,'email','telephone','affiliation','department','address','bill_address'
               ),
      Fieldset('More about yourself'
               ,'avatar','gender','research_status', 'research_field', 'supervisor'
               ,'short_bio'
               ),
      Fieldset('Social networking'
               ,'twitter','google_plus','facebook', 'personal_email', 'news_feed'
               ,'publication_feed'
               ),
      Fieldset('Admin'
               ,'last_login', 'date_joined'
               ),
                                
      HTML('<div class="form-group"><div class="col-md-5"> </div><div class="col-md-6">'), 
      Submit('submit', 'Update'), 
      HTML('</div></div>'),
    )  
#   receive_newsletter = forms.BooleanField(required=False)
# #   interests = ModelChoiceField(queryset=Interests.objects.all())
# #   interests = forms.MultipleChoiceField( required=False,
# #     widget=SelectMultiple(), choices=[ (o.id, str(o)) for o in Interest.objects.all()])#Interest.objects.all())
#   interests = forms.ModelMultipleChoiceField(queryset=Interest.objects.all(),widget=SelectMultiple(),required=False)
# 
#   class Meta:
#     model = User


class UserRegistrationForm(UserCreationForm):
 
  class Meta:
    # Since we are overriding Meta we have to re-tell it the model also
    model = User
    exclude = ['password', 'last_login', 'date_joined']
 
  def __init__(self, *args, **kwargs):
    super(UserRegistrationForm, self).__init__(*args, **kwargs)
    self.helper = FormHelper()
    self.helper.form_method = 'post'
    self.helper.form_action = 'register'
    self.helper.form_class = 'form-horizontal'
    self.helper.label_class = 'col-md-5'
    self.helper.field_class = 'col-md-6'
    self.helper.layout = Layout(
      # password1 and password2 are the fields defined in django.contrib.auth.forms.UserCreationForm
      Fieldset('Personal info'
               ,'first_name','last_name','username', 'password1', 'password2'
               ,'email','telephone','affiliation','department','address','bill_address'
               ),
      Fieldset('More about yourself'
               ,'avatar','gender','research_status', 'research_field', 'supervisor'
               ,'short_bio'
               ),
      Fieldset('Social networking'
               ,'twitter','google_plus','facebook', 'personal_email', 'news_feed'
               ,'publication_feed'
               ),
      HTML('<div class="form-group"><div class="col-md-5"> </div><div class="col-md-6">'), 
      Submit('submit', 'Register'), 
      HTML('</div></div>'),
    ) 


class LostPasswordForm(forms.Form):
 
  email = forms.EmailField(label='E-mail address')
 
  def __init__(self, *args, **kwargs):
    super(LostPasswordForm, self).__init__(*args, **kwargs)
    self.helper = FormHelper()
    self.helper.form_method = 'post'
    self.helper.form_action = 'lost_password'
    self.helper.form_class = 'form-horizontal'
    self.helper.label_class = 'col-md-5'
    self.helper.field_class = 'col-md-6'
    self.helper.layout = Layout(
      'email', 
      HTML('<div class="form-group"><div class="col-md-5"> </div><div class="col-md-6">'), 
      Submit('submit', 'Request new password'), HTML('</div></div>'),
    ) 
     
  def clean(self):
    cleaned_data = super(LostPasswordForm, self).clean()
    try:
      self.user = User.objects.get(email=cleaned_data['email'], is_active=True)
    except User.DoesNotExist:
      raise forms.ValidationError("We don't know of any user with that e-mail address")
    return cleaned_data


class LostPasswordChangeForm(forms.ModelForm):
 
  id = forms.IntegerField(widget=forms.HiddenInput())
  password1 = forms.CharField(label="Password", min_length=8, widget=forms.PasswordInput())
  password2 = forms.CharField(label="Password confirmation", widget=forms.PasswordInput())
 
  class Meta:
    model = Registration
    fields = ['id',]
     
  def __init__(self, *args, **kwargs):
    super(LostPasswordChangeForm, self).__init__(*args, **kwargs)
    # Just in case someone else uses our form
    if self.instance is None:
      raise Registration.DoesNotExist
    self.fields['id'].initial = self.instance.pk
    self.helper = FormHelper()
    self.helper.form_method = 'post'
    self.helper.form_action = 'reset_password'
    self.helper.form_class = 'form-horizontal'
    self.helper.label_class = 'col-md-5'
    self.helper.field_class = 'col-md-6'
    self.helper.layout = Layout(
      'id', 'password1', 'password2',
      HTML('<div class="form-group"><div class="col-md-5"> </div><div class="col-md-6">'), 
      Submit('submit', 'Change password'), HTML('</div></div>'),
    ) 
 
  def clean_password2(self):
    cleaned_data = super(LostPasswordChangeForm, self).clean()
    self.password = cleaned_data.get('password1')
    if self.password != cleaned_data.get('password2'):
      raise forms.ValidationError('Password do not match')
    self.user = self.instance.user
    return self.password
