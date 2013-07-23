# -*- coding: utf-8
from django.db import models

class OSMP(models.Model):
	txn_id = models.PositiveIntegerField(unique=True, db_index=True)
	money = models.DecimalField(decimal_places=2, max_digits=7)
	txn_date = models.DateTimeField()
	account = models.CharField(max_length=255)
	created_on = models.DateTimeField(auto_now_add=True, editable=False)

	class Meta:
		db_table = 'osmp'

	def __unicode__(self):
		return "%s - %s (%s)" % ( self.txn_id, self.money, self.account)