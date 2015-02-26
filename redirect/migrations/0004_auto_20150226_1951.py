# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('redirect', '0003_auto_20150225_1634'),
    ]

    operations = [
        migrations.RenameField(
            model_name='page',
            old_name='card_img',
            new_name='card_img_file',
        ),
        migrations.AddField(
            model_name='page',
            name='card_img_url',
            field=models.URLField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
