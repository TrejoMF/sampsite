# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-06-05 06:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='registro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=200, null=True)),
                ('descripcion', models.CharField(blank=True, max_length=200, null=True)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]
