# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('redirect', '0004_auto_20150226_1951'),
    ]

    operations = [
        migrations.CreateModel(
            name='PageAlias',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('uri', models.CharField(default=b'none', max_length=255, db_index=True)),
                ('page', models.ForeignKey(related_name='aliases', to='redirect.Page')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='page',
            name='card_description',
            field=models.CharField(max_length=500, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='page',
            name='card_type',
            field=models.PositiveIntegerField(default=1, choices=[(1, b'photo'), (2, b'summary_large_image'), (3, b'summary'), (4, b'app')]),
            preserve_default=True,
        ),
    ]
