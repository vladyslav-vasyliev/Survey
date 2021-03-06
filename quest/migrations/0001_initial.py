# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-28 16:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AnswerBase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('text', models.TextField()),
                ('required', models.BooleanField()),
                ('type', models.CharField(choices=[('TQ', 'Text Question'), ('RQ', 'Radio Question'), ('CQ', 'Check Question'), ('LQ', 'List Question'), ('NQ', 'Numeric Question')], max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Response',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Survey',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('name', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Table',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='AnswerInteger',
            fields=[
                ('answerbase_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='quest.AnswerBase')),
                ('body', models.IntegerField(blank=True, null=True)),
            ],
            bases=('quest.answerbase',),
        ),
        migrations.CreateModel(
            name='AnswerRadio',
            fields=[
                ('answerbase_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='quest.AnswerBase')),
                ('body', models.TextField(blank=True, null=True)),
            ],
            bases=('quest.answerbase',),
        ),
        migrations.CreateModel(
            name='AnswerSelect',
            fields=[
                ('answerbase_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='quest.AnswerBase')),
                ('body', models.TextField(blank=True, null=True)),
            ],
            bases=('quest.answerbase',),
        ),
        migrations.CreateModel(
            name='AnswerSelectMultiple',
            fields=[
                ('answerbase_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='quest.AnswerBase')),
                ('body', models.TextField(blank=True, null=True)),
            ],
            bases=('quest.answerbase',),
        ),
        migrations.CreateModel(
            name='AnswerText',
            fields=[
                ('answerbase_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='quest.AnswerBase')),
                ('body', models.TextField(blank=True, null=True)),
            ],
            bases=('quest.answerbase',),
        ),
        migrations.AddField(
            model_name='response',
            name='survey',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quest.Survey'),
        ),
        migrations.AddField(
            model_name='answerbase',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quest.Question'),
        ),
        migrations.AddField(
            model_name='answerbase',
            name='response',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quest.Response'),
        ),
    ]
