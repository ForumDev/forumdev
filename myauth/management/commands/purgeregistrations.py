from django.core.management.base import BaseCommand
from django.utils import timezone
 
from myauth.models import User, Registration
 
class Command(BaseCommand):
  args = None
  help = 'Purges expired registrations'
 
  def handle(self, *args, **kwargs):
    User.objects.filter(registration__expires__lte=timezone.now()).delete()
    Registration.objects.filter(expires_lte=timezone.now()).delete()
