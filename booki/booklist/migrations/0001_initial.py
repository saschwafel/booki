# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book_Entry',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=300)),
                ('author', models.CharField(max_length=100)),
                ('date_added', models.DateTimeField(verbose_name=b'Date Added')),
                ('date_started', models.DateTimeField(verbose_name=b'Date Started')),
                ('date_finished', models.DateTimeField(verbose_name=b'Date Finished')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
