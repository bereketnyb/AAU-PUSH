# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2017-03-22 14:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import push_page.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='contact_info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('bio', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='PushPage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('content1', models.TextField()),
                ('content2', models.TextField()),
                ('img1', models.FileField(upload_to=push_page.models.upload_path)),
                ('img2', models.FileField(blank=True, upload_to=push_page.models.upload_path)),
                ('contact', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='push_page.contact_info')),
            ],
        ),
    ]
