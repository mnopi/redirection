from django.db import models

# Create your models here.
class Page(models.Model):
    uri = models.CharField(max_length=255, null=False, blank=False, default='none', db_index=True)
    all = models.URLField(max_length=200, null=True, blank=True)
    android = models.URLField(max_length=200, null=True, blank=True)
    ios = models.URLField(max_length=200, null=True, blank=True)
    other = models.URLField(max_length=200, null=True, blank=True)

    def __unicode__(self):
        return str(self.pk)
