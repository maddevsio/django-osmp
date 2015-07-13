# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('osmp', '0002_auto_20150713_1227'),
    ]

    operations = [
        migrations.AlterField(
            model_name='osmp',
            name='txn_id',
            field=models.CharField(max_length=255, db_index=True),
            preserve_default=True,
        ),
    ]
