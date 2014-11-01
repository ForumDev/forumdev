from django.db import models

import re
import uuid
from dateutil.relativedelta import relativedelta

from django.core import validators
from django.utils import timezone
from django.core.mail import send_mail
from django.utils.http import urlquote
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django import forms


def two_days_from_now():
  return timezone.now() + relativedelta(days=2)


def get_uuid_str():
  return uuid.uuid4().__str__()
      

class UserManager(BaseUserManager):

  def _create_user(self, username, email, password, is_staff, is_superuser, **extra_fields):
    now = timezone.now()
    if not username:
      raise ValueError(_('The given username must be set'))
    email = self.normalize_email(email)
    user = self.model(username=username, email=email,
             is_staff=is_staff, is_active=False,
             is_superuser=is_superuser, last_login=now,
             date_joined=now, **extra_fields)
    user.set_password(password)
    user.save(using=self._db)
    return user

  def create_user(self, username, email=None, password=None, **extra_fields):
    return self._create_user(username, email, password, False, False,
                 **extra_fields)

  def create_superuser(self, username, email, password, **extra_fields):
    user=self._create_user(username, email, password, True, True,
                 **extra_fields)
    user.is_active=True
    user.save(using=self._db)
    return user



class User(AbstractBaseUser, PermissionsMixin):
  username = models.CharField(_('username'), max_length=30, unique=True,
    help_text=_('Required. 30 characters or fewer. Letters, numbers and @/./+/-/_ characters'),
    validators=[
      validators.RegexValidator(re.compile('^[\w.@+-]+$'), _('Enter a valid username.'), _('invalid'))
    ])
  short_name = models.CharField(_('short name'), max_length=30, blank=True, null=True)
  full_name = models.CharField(_('full name'), max_length=255, blank=True, null=True)
  email = models.EmailField(_('email address'), max_length=255, unique=True)
  is_staff = models.BooleanField(_('staff status'), default=False,
    help_text=_('Designates whether the user can log into this admin site.'))
  is_active = models.BooleanField(_('active'), default=False,
    help_text=_('Designates whether this user should be treated as active. Unselect this instead of deleting accounts.'))
  date_joined = models.DateTimeField(_('date joined'), default=timezone.now)
  receive_newsletter = models.BooleanField(_('receive newsletter'), default=False)

  USERNAME_FIELD = 'username'
  REQUIRED_FIELDS = ['email',]


  class Meta:
    verbose_name = _('user')
    verbose_name_plural = _('users')

  def get_full_name(self):
    return self.full_name
 
  def get_short_name(self):
    return self.short_name

  def email_user(self, subject, message, from_email=None):
    send_mail(subject, message, from_email, [self.email])

  objects = UserManager()


class Registration(models.Model):
 
  uuid = models.CharField(max_length=36, default=get_uuid_str)
  user = models.ForeignKey(User, related_name='registration')
  expires = models.DateTimeField(default=two_days_from_now)
  type = models.CharField(max_length=10, choices=(
    ('register', 'register'),
    ('lostpass', 'lostpass'),
  ), default = 'register')
