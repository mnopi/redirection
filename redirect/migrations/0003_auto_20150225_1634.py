# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('redirect', '0002_page_uri'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='card_img',
            field=models.ImageField(null=True, upload_to=b'pages_imgs', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='page',
            name='card_title',
            field=models.CharField(max_length=140, null=True, blank=True),
            preserve_default=True,
        ),
    ]
