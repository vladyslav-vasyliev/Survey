# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-28 16:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quest', '0002_delete_table'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='survey',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='quest.Survey'),
            preserve_default=False,
        ),
    ]
