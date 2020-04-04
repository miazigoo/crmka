from django import forms
from .models import Customer

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        exclude = ['']
        verbose_name = 'Customer'
        verbose_name_plural = 'Customers'