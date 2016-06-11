# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0002_auto_20150713_2135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='step',
            name='step_number',
            field=models.IntegerField(),
        ),
    ]
