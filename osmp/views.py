import re

from profile.models import User
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden

class PaymentMixin(object):
	def is_valid(self):
		""" Initialize """

		self.txn_id = self.request.GET.get('txn_id')
		self.command = self.request.GET.get('command')
		self.account = self.request.GET.get('account')
		self.txn_date = self.request.GET.get('txn_date')
		self.money = self.request.GET.get('sum')
		try:
			self.user = User.objects.get(username=self.account)
		except User.DoesNotExist:
			self.user = None
		if self.command and self.money and self.txn_date and self.account:
			return True
		return False

	def ProcessPayment(self, **kwargs):
		""" 0 """

		if self.isAccountBadFormat() and self.AccountIsExist():
			if self.command == 'check':
				return HttpResponse(self.toXml( 0, "Processed", self.txn_id, self.money), content_type="application/xml")

	def isAccountBadFormat(self):
		""" 4 """
		return True if re.match(r'\d+', self.account) else HttpResponse(self.toXml(4, "Account Bad format"), content_type="application/xml")


	def AccountIsExist(self, **kwargs):
		""" 5 """
		return True if self.user else HttpResponse(self.toXml(5, "Account Does Not Exist"), content_type="application/xml")
	
	def Denied(self, **kwargs):
		""" 7 """
		pass
	def DeniedByTech(self, **kwargs):
		""" 8 """
		pass
	def AccountNotActive(self, **kwargs):
		""" 79 """
		return self.user.is_active
	
	def DelayedPayment(self, **kwargs):
		""" 90 """
		pass
	
	def TooLowMoney(self, **kwargs):
		""" 241 """
		pass
	def TooMuchMoney(self, **kwargs):
		""" 242 """
		pass
	
	def UnableToCheckBalance(self, **kwargs):
		""" 243 """
		pass
	
	def Unknown(self, **kwargs):
		""" 300 """
		return HttpResponse(self.toXml(300, "Unknown Error"), content_type="application/xml")

	def toXml(self, result, comment, osmp_txn_id=" ", sum=" ", prv_txn=" "):
		template = """<?xml version="1.0" encoding="UTF-8"?>    
	    <response>
	        <osmp_txn_id>%(txn_id)s</osmp_txn_id>
	        <prv_txn>%(prv_txn)s</prv_txn>
	        <sum>%(sum)s</sum>
	        <result>%(result)s</result>
	        <comment>%(comment)s</comment>
	    </response>""" % {
	               'txn_id': osmp_txn_id,
	               'prv_txn': prv_txn,
	               'sum': sum,
	               'result': result,
	               'comment': comment,
	               }
	    
		return template