from django.db import models
from cms.models.pluginmodel import CMSPlugin
# Create your models here.

class Sponsor(CMSPlugin):
    title = models.TextField()
    url = models.TextField(default='')
    image = models.ImageField("Spnsor image", upload_to="images/sponsor/", blank=False, null=False)
    def __str__(self):              # __unicode__ on Python 2
        return self.title
    def __unicode__(self):
        return self.title