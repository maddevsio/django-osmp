# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('osmp', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='osmp',
            unique_together=set([('txn_id', 'method')]),
        ),
    ]
