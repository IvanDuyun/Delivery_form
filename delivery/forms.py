from django import forms
from . import models
from testovoe import settings

class DeliveryForm(forms.ModelForm):
    delivery_date = forms.DateField(required=False, input_formats=settings.DATE_INPUT_FORMATS,
            widget = forms.DateInput(
                format=settings.DATE_INPUT_FORMATS,
                attrs={'class': 'form-control'}))
    class Meta:
        model = models.Delivery
        fields = ['name', 'type', 'delivery_date', 'attachment', 'address']
