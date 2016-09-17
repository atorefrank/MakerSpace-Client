# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('billing', '0004_auto_20151109_0101'),
    ]

    operations = [
        migrations.AlterField(
            model_name='membership',
            name='date_end',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 9, 23, 26, 31, 460621, tzinfo=utc), verbose_name=b'End Date'),
        ),
        migrations.AlterField(
            model_name='membership',
            name='date_start',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 9, 23, 26, 31, 460175, tzinfo=utc), verbose_name=b'Start Date'),
        ),
    ]
