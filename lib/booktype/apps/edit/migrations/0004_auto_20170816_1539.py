# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2017-08-16 15:39
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('editor', '0009_chapter_content_json'),
        ('edit', '0003_auto_20170420_0144'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChatMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('datetime', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ChatThread',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='editor.Book')),
            ],
        ),
        migrations.AddField(
            model_name='chatmessage',
            name='thread',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='edit.ChatThread'),
        ),
    ]
