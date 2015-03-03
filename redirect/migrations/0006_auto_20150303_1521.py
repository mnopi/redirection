# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('redirect', '0005_auto_20150303_1439'),
    ]

    operations = [
        migrations.CreateModel(
            name='Redirection',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('url', models.URLField(null=True, blank=True)),
                ('platform', models.PositiveIntegerField(blank=True, null=True, choices=[(1, b'android'), (2, b'ios'), (3, b'others')])),
                ('language', models.CharField(max_length=2, null=True, blank=True)),
                ('page', models.ForeignKey(related_name='redirections', to='redirect.Page')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterModelOptions(
            name='pagealias',
            options={'verbose_name_plural': 'pages aliases'},
        ),
        migrations.RemoveField(
            model_name='page',
            name='all',
        ),
        migrations.RemoveField(
            model_name='page',
            name='android',
        ),
        migrations.RemoveField(
            model_name='page',
            name='ios',
        ),
        migrations.RemoveField(
            model_name='page',
            name='other',
        ),
        migrations.AlterField(
            model_name='page',
            name='card_type',
            field=models.PositiveIntegerField(default=1, null=True, blank=True, choices=[(1, b'photo'), (2, b'summary_large_image'), (3, b'summary'), (4, b'app')]),
            preserve_default=True,
        ),
    ]
