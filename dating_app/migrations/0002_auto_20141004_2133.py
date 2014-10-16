# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dating_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dater',
            name='paid',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='dater',
            name='gender',
            field=models.CharField(max_length=3, choices=[(b'M', b'Male'), (b'F', b'Female'), (b'O', b'Other')]),
        ),
    ]
