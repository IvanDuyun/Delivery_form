from django import forms
from .models import Delivery, Address
from testovoe import settings
from django.forms.models import inlineformset_factory

class DeliveryForm(forms.ModelForm):
    delivery_date = forms.DateField(required=False, input_formats=settings.DATE_INPUT_FORMATS,
            widget = forms.DateInput(
                format=settings.DATE_INPUT_FORMATS,
                attrs={'class': 'form-control'}))
    class Meta:
        model = Delivery
        fields = ['name', 'type', 'delivery_date', 'attachment', 'address']

AddressDeliveryFormset = inlineformset_factory(Address, Delivery,
                         fields=('name','type', 'delivery_date', 'attachment',))