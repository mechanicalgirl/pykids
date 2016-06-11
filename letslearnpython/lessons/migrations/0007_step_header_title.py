# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0006_auto_20150717_2218'),
    ]

    operations = [
        migrations.AddField(
            model_name='step',
            name='header_title',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
    ]
