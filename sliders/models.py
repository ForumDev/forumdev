from django.db import models
from cms.models.pluginmodel import CMSPlugin
from django.utils.http import int_to_base36
# Create your models here.

class Slider(models.Model):
    title = models.TextField(max_length=25)
    index = models.IntegerField(default=0)
    descript = models.TextField(default='')
    short_name = models.CharField(max_length=25,default='',help_text='short-name: no special characters, no spaces')
    image = models.ImageField("Slider image", upload_to="images/slider/", blank=False, null=False)
    get_latest_by = 'index'
    def __str__(self):              # __unicode__ on Python 2
        return int_to_base36(self.index)+ ' ' + self.title
    def __unicode__(self):
        return int_to_base36(self.index)+ ' ' + self.title