# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Step',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('step_number', models.IntegerField()),
                ('step_name', models.CharField(max_length=200)),
                ('image', models.CharField(max_length=200, null=True, blank=True)),
                ('description', models.TextField()),
            ],
        ),
    ]
