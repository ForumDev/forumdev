from django.db import models
from django.contrib.sites.models import Site
from cms.models.pluginmodel import CMSPlugin
# Create your models here.

class Sponsor(models.Model):
    title = models.TextField()
    url = models.TextField(default='')
    sites = models.ManyToManyField(Site)
    image = models.ImageField("Spnsor image", upload_to="images/sponsor/", blank=False, null=False)
    def __str__(self):              # __unicode__ on Python 2
        return self.title
    def __unicode__(self):
        return self.title