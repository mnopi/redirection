from django.db import models

# Create your models here.
class Page(models.Model):
    uri = models.CharField(max_length=255, null=False, blank=False, default='none', db_index=True)

    # twitter card
    PHOTO = 1
    SUMMARY_LARGE_IMAGE = 2
    SUMMARY = 3
    APP = 4
    CARD_TYPES = (
        (PHOTO, 'photo'),
        (SUMMARY_LARGE_IMAGE, 'summary_large_image'),
        (SUMMARY, 'summary'),
        (APP, 'app'),
    )
    card_type = models.PositiveIntegerField(null=True, blank=True, choices=CARD_TYPES, default=None)
    card_img_file = models.ImageField(upload_to='pages_imgs', blank=True, null=True)
    card_img_url = models.URLField(max_length=200, blank=True, null=True)
    card_title = models.CharField(max_length=140, blank=True, null=True)
    card_description = models.TextField(max_length=500, blank=True, null=True)

    def __unicode__(self):
        return self.uri


class PageAlias(models.Model):
    uri = models.CharField(max_length=255, null=False, blank=False, default='none', db_index=True)
    page = models.ForeignKey(Page, related_name='aliases')

    class Meta:
        verbose_name_plural = 'pages aliases'

    def __unicode__(self):
        return '%s -> %s' % (self.uri, self.page.uri)


class Redirection(models.Model):
    page = models.ForeignKey(Page, related_name='redirections')
    url = models.URLField(max_length=200, null=True, blank=True)

    ANDROID = 1
    IOS = 2
    OTHERS = 3
    PLATFORMS = (
        (ANDROID, 'android'),
        (IOS, 'ios'),
        (OTHERS, 'others'),
    )
    platform = models.PositiveIntegerField(null=True, blank=True, choices=PLATFORMS)
    language = models.CharField(max_length=2, null=True, blank=True)

    def __unicode__(self):
        platform_str = ' @%s' % self.get_platform_str()
        return '%s%s -> %s' % (self.page, platform_str, self.url)

    def get_platform_str(self):
        return self.get_platform_display() if self.platform else 'all'
