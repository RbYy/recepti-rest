# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-21 17:28
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('svincnik', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jed',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='jedi', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='jed',
            name='vrsta',
            field=models.CharField(choices=[('glavna', 'glavna'), ('sladica', 'sladica'), ('predjed', 'predjed')], max_length=30),
        ),
        migrations.DeleteModel(
            name='Vrsta',
        ),
    ]