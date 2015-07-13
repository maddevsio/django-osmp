# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OSMP',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('txn_id', models.CharField(unique=True, max_length=255, db_index=True)),
                ('money', models.DecimalField(default=0, max_digits=7, decimal_places=2)),
                ('txn_date', models.DateTimeField(null=True)),
                ('account', models.CharField(max_length=255)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('method', models.PositiveIntegerField()),
                ('added', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'osmp',
            },
            bases=(models.Model,),
        ),
    ]
