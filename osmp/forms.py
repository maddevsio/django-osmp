from django import forms


class PaymentForm(forms.Form):
    CHOICES = (
        (1, 'check'),
        (2, 'pay')
    )

    txn_id = forms.IntegerField()
    command = forms.ChoiceField(choices=CHOICES)
    money = forms.DecimalField(max_digits=7, decimal_places=2)
    txn_date = forms.DateTimeField(input_formats=['%Y%m%d%H%M%S'])
    account = forms.CharField(max_length=50, min_length=1)
