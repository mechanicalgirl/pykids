# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0004_lesson_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='step',
            name='audiocast',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='step',
            name='screencast',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
    ]
