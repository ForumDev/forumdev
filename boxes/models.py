from django.db import models
from cms.models.pluginmodel import CMSPlugin
#from cms.models import Page
from cms.models import fields
# Create your models here.


class Box(models.Model):
    title = models.TextField(max_length=15, default='')
    url = models.URLField(blank=True, null=True, help_text="Link to an external page (will override page link)",)
    page = fields.PageField(
        verbose_name="page",
        help_text="Select an existing page to link to.",
        blank=True,
        null=True
    )
    image = models.ImageField("Box image", upload_to="images/box/", blank=False, null=False)
    def __str__(self):              # __unicode__ on Python 2
        return self.title
    def __unicode__(self):
        return self.title
    class Meta:
        verbose_name_plural = 'Boxes'
    def link(self):
        if self.url:
            return self.url
        elif self.page:
            return self.page.get_absolute_url()
        else: return "#"

    
#class CatSel(CMSPlugin):
#    cat = models.ForeignKey(Box)
