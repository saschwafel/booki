# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booklist', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book_entry',
            name='date_added',
            field=models.DateField(verbose_name=b'Date Added'),
        ),
        migrations.AlterField(
            model_name='book_entry',
            name='date_finished',
            field=models.DateField(verbose_name=b'Date Finished'),
        ),
        migrations.AlterField(
            model_name='book_entry',
            name='date_started',
            field=models.DateField(verbose_name=b'Date Started'),
        ),
    ]
