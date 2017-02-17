# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2017-02-17 01:56
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Publicaciones', '0003_auto_20170214_0248'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publicacion',
            name='autor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Publicaciones', to=settings.AUTH_USER_MODEL),
        ),
    ]