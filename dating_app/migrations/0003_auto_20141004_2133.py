# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dating_app', '0002_auto_20141004_2133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dater',
            name='age',
            field=models.IntegerField(help_text=b'age', max_length=3, blank=True),
        ),
    ]
