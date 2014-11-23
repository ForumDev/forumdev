from django.core.urlresolvers import reverse           
from django.views.generic.edit import FormView         
from django.views.generic.base import TemplateView, RedirectView
from django.contrib.auth import login, logout
from django.contrib import messages
from django.conf import settings
from django.http import Http404
from django.contrib.sites.models import Site
 
from templated_email import send_templated_mail
       
from myauth.forms import LoginForm, UserRegistrationForm, LostPasswordForm, LostPasswordChangeForm
from myauth.models import Registration, User


class RegisterView(FormView):
 
  template_name = 'myauth/register.html'
  form_class = UserRegistrationForm
 
  def get_success_url(self):
    return reverse('confirmation_mail_sent')
   
  def form_valid(self, form):
    user = form.save()
    registration = Registration.objects.create(user=user)
    messages.info(self.request, 'Registration successfull')
    send_templated_mail(
      template_name='registration',
      # substitute your e-mail adress
      from_email='noreply@crisler.ch',
      recipient_list=[form.cleaned_data['email'],],
      context={
        'url_name': 'activation',
        'url_param': 'key',
        'registration': registration,
        'current_site': Site.objects.get_current(),
        'base_url': settings.SITE_URL,
      },
    )
    return super(RegisterView, self).form_valid(form)
 
 
class EmailSentView(TemplateView):
 
  template_name = 'myauth/email_sent.html'
 
 
class ActivationView(RedirectView):
 
  permanent = False
 
  def get_redirect_url(self):
    return reverse('login')
 
  def get(self, request, *args, **kwargs):
    uuid = request.GET.get('key', None)
    if uuid is None:
      raise Http404
    try:
      user = User.objects.get(registration__uuid=uuid, type='register')
      user.is_active = True
      user.save()
      user.registration.delete()
      messages.info(self.request, 'User activation successfull')
    except:
      raise Http404
    return super(ActivationView, self).get(request, *args, **kwargs)

   
class LoginView(FormView):
     
  template_name = 'myauth/login.html'
  form_class = LoginForm
   
  def get_success_url(self):                           
   return '/' #reverse('homepage')
   
  def form_valid(self, form):
    form.user.backend = 'django.contrib.auth.backends.ModelBackend'
    login(self.request, form.user)
    messages.info(self.request, 'Login successfull')
    return super(LoginView, self).form_valid(form)


class LogoutView(RedirectView):
                                                        
  permanent = False
                                                        
  def get_redirect_url(self):
    return reverse('login')
 
  def dispatch(self, request, *args, **kwargs):
    try:
      logout(request)
    except:
      ## if we can't log the user out, it probably means they we're not logged-in to begin with, so we do nothing
      pass
    messages.info(request, 'You have successfully logged out. Come back soon.')
    return super(LogoutView, self).dispatch(request, *args, **kwargs)


class LostPasswordView(FormView):
 
  template_name = 'myauth/lost_password.html'
  form_class = LostPasswordForm
 
  def get_success_url(self):
    return reverse('lost_password_mail_sent')
 
  def form_valid(self, form):
    user = form.user
    registration = Registration.objects.create(user=user, type='lostpass')
    send_templated_mail(
      template_name='lost_password',
      # substitute your e-mail adress
      from_email='noreply@crisler.ch',
      recipient_list=[form.cleaned_data['email'],],
      context={
        'url_name': 'reset_password',
        'url_param': 'key',
        'registration': registration,
        'current_site': Site.objects.get_current(),
        'base_url': settings.SITE_URL,
      },
    ) 
    return super(LostPasswordView, self).form_valid(form)
     
     
class LostPasswordEmailSentView(TemplateView):
 
  template_name = 'myauth/lost_password_email_sent.html'


class LostPasswordChangeView(FormView):
 
  template_name = 'myauth/lost_password_change.html'
  form_class = LostPasswordChangeForm
 
  def get_success_url(self):
    return reverse('login')
   
  def get_form_kwargs(self):
    kwargs = super(LostPasswordChangeView, self).get_form_kwargs()
    if self.request.method == 'GET':
      key = self.request.GET.get('key')
      try:
        registration = Registration.objects.get(uuid=key, type='lostpass')
      except:
        raise Http404
    else:
      try: 
        registration = Registration.objects.get(pk=kwargs['data'].get('id'), type='lostpass')
      except:
        raise Http404
    kwargs['instance'] = registration
    return kwargs
 
  def form_valid(self, form):
    form.user.set_password(form.password)
    form.user.save()
    form.instance.delete()
    messages.info(self.request, 'Your password has been successfully updated')
    return super(LostPasswordChangeView, self).form_valid(form)
