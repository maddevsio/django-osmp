### OSMP(Qiwi) payment Integration for Django
#### Tested on Django 1.5

#### Usage:
1. Install and add it to INSTALLED_APPS
2. Create your models and custom view as CBV
Model

```python
from osmp.models import OSMP 
class SomePaymentModel(OSMP):
  pass
```
and view

```python
from osmp.models import PaymentMixin
from django.views.generic import View

class SomePayment(view, PaymentMixin):
  def get(self, request, *args, **kwargs):
    if self.is_valid():
      ....
      ....
      ....
    return self.Unknown()
```
