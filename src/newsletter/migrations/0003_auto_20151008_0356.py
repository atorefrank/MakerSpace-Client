# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0002_auto_20151005_1303'),
    ]

    operations = [
        migrations.AddField(
            model_name='signup',
            name='ip_address',
            field=models.CharField(default=b'ABC', max_length=120),
        ),
        migrations.AddField(
            model_name='signup',
            name='password',
            field=models.CharField(default=b'ABC', max_length=120),
        ),
        migrations.AddField(
            model_name='signup',
            name='ref_id',
            field=models.CharField(default=b'ABC', max_length=120),
        ),
        migrations.AlterUniqueTogether(
            name='signup',
            unique_together=set([('email', 'ref_id')]),
        ),
    ]
