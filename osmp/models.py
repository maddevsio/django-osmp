# -*- coding: utf-8
from django.db import models


class OSMP(models.Model):
    txn_id = models.CharField(db_index=True, max_length=255)
    money = models.DecimalField(decimal_places=2, max_digits=7, default=0)
    txn_date = models.DateTimeField(null=True, db_index=True)
    account = models.CharField(max_length=255, db_index=True)
    created_on = models.DateTimeField(auto_now_add=True, editable=False, db_index=True)
    method = models.PositiveIntegerField(db_index=True)
    added = models.BooleanField(default=False, db_index=True)

    def __unicode__(self):
        return "%s - %s (%s)" % (self.txn_id, self.money, self.account)

    class Meta:
        db_table = 'osmp'
        unique_together = ('txn_id', 'method')
