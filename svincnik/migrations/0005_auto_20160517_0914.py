# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-17 09:14
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('svincnik', '0004_auto_20160516_2028'),
    ]

    operations = [
        migrations.CreateModel(
            name='Komentar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vsebina', models.TextField()),
                ('objavljeno', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'Komentarji',
            },
        ),
        migrations.RemoveField(
            model_name='zapis',
            name='jed',
        ),
        migrations.RemoveField(
            model_name='zapis',
            name='user',
        ),
        migrations.RenameField(
            model_name='jed',
            old_name='vrsta',
            new_name='kategorija',
        ),
        migrations.AddField(
            model_name='jed',
            name='dodano',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2016, 5, 17, 9, 14, 11, 416252, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Zapis',
        ),
        migrations.AddField(
            model_name='komentar',
            name='jed',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='komentarji', to='svincnik.Jed'),
        ),
        migrations.AddField(
            model_name='komentar',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='komentarji', to=settings.AUTH_USER_MODEL),
        ),
    ]
