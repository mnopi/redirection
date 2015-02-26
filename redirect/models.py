from django.db import models

# Create your models here.
class Page(models.Model):
    uri = models.CharField(max_length=255, null=False, blank=False, default='none', db_index=True)
    all = models.URLField(max_length=200, null=True, blank=True)
    android = models.URLField(max_length=200, null=True, blank=True)
    ios = models.URLField(max_length=200, null=True, blank=True)
    other = models.URLField(max_length=200, null=True, blank=True)
    card_img_file = models.ImageField(upload_to='pages_imgs', blank=True, null=True)
    card_img_url = models.URLField(max_length=200, blank=True, null=True)
    card_title = models.CharField(max_length=140, blank=True, null=True)

    def __unicode__(self):
        return str(self.pk)
