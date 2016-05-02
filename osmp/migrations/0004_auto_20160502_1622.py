# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('osmp', '0003_auto_20150713_1250'),
    ]

    operations = [
        migrations.AlterField(
            model_name='osmp',
            name='account',
            field=models.CharField(max_length=255, db_index=True),
        ),
        migrations.AlterField(
            model_name='osmp',
            name='added',
            field=models.BooleanField(default=False, db_index=True),
        ),
        migrations.AlterField(
            model_name='osmp',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, db_index=True),
        ),
        migrations.AlterField(
            model_name='osmp',
            name='method',
            field=models.PositiveIntegerField(db_index=True),
        ),
        migrations.AlterField(
            model_name='osmp',
            name='txn_date',
            field=models.DateTimeField(null=True, db_index=True),
        ),
    ]
