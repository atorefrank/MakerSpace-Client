# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('billing', '0003_auto_20151107_0426'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('transaction_id', models.CharField(max_length=128)),
                ('order_id', models.CharField(max_length=128)),
                ('amount', models.DecimalField(max_digits=100, decimal_places=2)),
                ('success', models.BooleanField(default=True)),
                ('transaction_status', models.CharField(max_length=220, null=True, blank=True)),
                ('card_type', models.CharField(max_length=120)),
                ('last_four', models.PositiveIntegerField(null=True, blank=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='membership',
            name='date_end',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 9, 1, 1, 56, 491861, tzinfo=utc), verbose_name=b'End Date'),
        ),
        migrations.AlterField(
            model_name='membership',
            name='date_start',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 9, 1, 1, 56, 491430, tzinfo=utc), verbose_name=b'Start Date'),
        ),
    ]
