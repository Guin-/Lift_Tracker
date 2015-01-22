# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('bodyweight', models.IntegerField()),
                ('goals', models.TextField(max_length=500)),
                ('timestamp', models.DateTimeField(default=datetime.datetime.now, auto_now_add=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
