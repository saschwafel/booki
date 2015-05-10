# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booklist', '0002_auto_20150510_1425'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book_entry',
            name='date_finished',
            field=models.DateField(null=True, verbose_name=b'Date Finished', blank=True),
        ),
        migrations.AlterField(
            model_name='book_entry',
            name='date_started',
            field=models.DateField(null=True, verbose_name=b'Date Started', blank=True),
        ),
    ]
