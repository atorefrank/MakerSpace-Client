# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20151106_2300'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='membership',
            name='user',
        ),
        migrations.DeleteModel(
            name='Membership',
        ),
    ]
