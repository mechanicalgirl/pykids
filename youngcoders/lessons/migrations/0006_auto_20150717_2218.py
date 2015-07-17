# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0005_auto_20150717_2125'),
    ]

    operations = [
        migrations.AlterField(
            model_name='step',
            name='image',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
    ]
