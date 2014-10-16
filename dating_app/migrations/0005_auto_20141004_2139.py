# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('dating_app', '0004_auto_20141004_2134'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='dater',
            field=models.ForeignKey(related_name=b'locations', default='', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='location',
            name='city',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='location',
            name='country',
            field=models.CharField(max_length=100),
        ),
    ]
