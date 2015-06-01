# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booklist', '0003_auto_20150510_1522'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book_entry',
            options={'verbose_name_plural': 'Book Entries'},
        ),
    ]
