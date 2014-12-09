# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('redirect', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='uri',
            field=models.CharField(default=b'none', max_length=255, db_index=True),
            preserve_default=True,
        ),
    ]
