# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='number',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='step',
            name='step_number',
            field=models.IntegerField(max_length=2),
        ),
    ]
