# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.conf import settings
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_userprofile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Membership',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_end', models.DateTimeField(default=datetime.datetime(2015, 11, 6, 21, 22, 20, 570912, tzinfo=utc))),
                ('date_start', models.DateTimeField(default=datetime.datetime(2015, 11, 6, 21, 22, 20, 571424, tzinfo=utc))),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
