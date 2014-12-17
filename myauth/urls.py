
__license__ = 'MIT License <http://www.opensource.org/licenses/mit-license.php>'
__author__ = 'Maik Berchten <mberchten@crisler.ch>'
__docformat__ = 'epytext'

from myauth.views import LoginView, LogoutView, RegisterView, EmailSentView, ActivationView, LostPasswordView, LostPasswordEmailSentView, LostPasswordChangeView

try:
    from django.conf.urls import patterns, url
except ImportError:
    from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('',
    url(r'^email_sent\.html$', EmailSentView.as_view(), name='confirmation_mail_sent'),                   
    url(r'^login\.html$', LoginView.as_view(), name='login'),
    url(r'^logout\.html$', LogoutView.as_view(), name='logout'),
    url(r'^register\.html$', RegisterView.as_view(), name='register'),
    url(r'^lost_password\.html', LostPasswordView.as_view(), name='lost_password'),
    url(r'^lost_password_mail_sent\.html', LostPasswordEmailSentView.as_view(), name='lost_password_mail_sent'),
    url(r'^reset_password\.html', LostPasswordChangeView.as_view(), name='reset_password'), 
)
