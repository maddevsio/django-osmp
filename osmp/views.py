# -*- coding: utf-8 -*-
from datetime import datetime
from decimal import Decimal
from django.http import HttpResponse, HttpResponseBadRequest
from django.db import IntegrityError
from django.db import transaction

from osmp.models import OSMP
from django.conf import settings

import_string = "from {0} import {1} as User".format(settings.OSMP_BALANCE_APP, settings.OSMP_BALANCE_MODEL)
exec import_string


class BadAccountException(Exception):
    pass


class AccountDoesNotExistException(Exception):
    pass


class PaymentMixin(object):
    """<?xml version="1.0" encoding="UTF-8"?>
    <response>
      <osmp_txn_id>%(txn_id)s</osmp_txn_id>
      <prv_txn>%(prv_txn)s</prv_txn>
      <sum>%(sum)s</sum>
      <result>%(result)s</result>
      <comment>%(comment)s</comment>
    </response>
    """
    def __check_params(self):
        self.account = self.request.GET.get('account')
        lookup_filter = {settings.OSMP_MODEL_LOOKUP_FIELD: self.account}
        try:
            self.user = User.objects.get(**lookup_filter)
        except User.DoesNotExist:
            self.user = None
        if self.account:
            return True
        return False

    def __pay_params(self):
        self.account = self.request.GET.get('account')
        self.txn_date = datetime.strptime(self.request.GET.get('txn_date'), '%Y%m%d%H%M%S')
        self.money = Decimal(self.request.GET.get('sum'))
        lookup_filter = {settings.OSMP_MODEL_LOOKUP_FIELD: self.account}
        try:
            self.user = User.objects.get(**lookup_filter)
        except User.DoesNotExist:
            self.user = None
        if self.account and self.txn_date and self.money:
            return True
        return False

    def is_valid(self):
        """ Initialize """

        commands = {
            "check": self.__check_params,
            "pay": self.__pay_params
        }
        self.txn_id = self.request.GET.get('txn_id')
        self.command = self.request.GET.get('command')

        if self.command and self.txn_id:
            return commands.get(self.command)()
        return False

    def ProcessPayment(self, method, **kwargs):
        """ 0 """
        commands = {
            "check": self.__check,
            "pay": self.__pay
        }

        try:
            if self.isAccountBadFormat() and self.AccountIsExist():
                data = commands.get(self.command)(method)
                return HttpResponse(data, content_type="application/xml")

        except BadAccountException:
            return HttpResponse(self.toXml(4, "Account Bad Format"), content_type='application/xml')

        except AccountDoesNotExistException:
            return HttpResponse(self.toXml(5, "Account Does Not Exist"), content_type="application/xml")

    def __check(self, method, *args, **kwargs):
        try:
            payment = OSMP.objects.get(method=method, txn_id=self.txn_id, account=self.account)
        except OSMP.DoesNotExist:
            try:
                payment = OSMP.objects.create(method=method, txn_id=self.txn_id, account=self.account)
            except IntegrityError:
                payment = OSMP.objects.get(method=method, txn_id=self.txn_id, account=self.account)

        return self.toXml(0, "Processed", payment.txn_id)

    def __pay(self, method, *args, **kwargs):
        try:
            payment = OSMP.objects.get(method=method, txn_id=self.txn_id, account=self.account)
        except OSMP.DoesNotExist:
            try:
                payment = OSMP.objects.create(method=method, txn_id=self.txn_id, account=self.account)
            except IntegrityError:
                payment = OSMP.objects.get(method=method, txn_id=self.txn_id, account=self.account)

        if not payment.added:
            payment.money = self.money
            payment.txn_date = self.txn_date
            payment.added = True
            payment.save()
            self.user.update_balance = getattr(self.user, settings.OSMP_UPDATE_BALANCE_PATH)
            with transaction.atomic():
                self.user.update_balance(self.money, "Пополнение баланса", payment=payment)
        return HttpResponse(self.toXml(0, "Processed", payment.txn_id, payment.money, payment.pk), content_type='application/xml')

    def isAccountBadFormat(self):
        """ 4 """
        if self.account.isdigit():
            return True
        raise BadAccountException()

    def AccountIsExist(self, **kwargs):
        """ 5 """
        if self.user:
            return True
        raise AccountDoesNotExistException()

    def Denied(self, **kwargs):
        """ 7 """

    def DeniedByTech(self, **kwargs):
        """ 8 """

    def AccountNotActive(self, **kwargs):
        """ 79 """
        return self.user.is_active

    def DelayedPayment(self, **kwargs):
        """ 90 """

    def TooLowMoney(self, **kwargs):
        """ 241 """

    def TooMuchMoney(self, **kwargs):
        """ 242 """

    def UnableToCheckBalance(self, **kwargs):
        """ 243 """

    def Unknown(self, **kwargs):
        """ 300 """
        return HttpResponse(self.toXml(300, "Unknown Error"), content_type="application/xml")

    def BadRequest(self):
        return HttpResponseBadRequest("Bad Request")

    def toXml(self, result, comment, osmp_txn_id=" ", sum=" ", prv_txn=" "):
        payload = {
            'txn_id': osmp_txn_id,
            'prv_txn': prv_txn,
            'sum': sum,
            'result': result,
            'comment': comment,
        }

        return PaymentMixin.__doc__ % payload
