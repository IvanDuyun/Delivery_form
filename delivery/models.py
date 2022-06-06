from django.db import models
from django.urls import reverse


class Type(models.Model):
    name = models.CharField('Тип товара', max_length=250, blank=True)

    class Meta:
        db_table = 'type'

    def __str__(self):
        return self.name

class Address(models.Model):
    name = models.CharField('Адрес', max_length=250, blank=False, null=False)

    def get_absolute_url(self):
        return reverse('delivery:address_detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.address

class Delivery(models.Model):
    name = models.CharField('Название товара', max_length=250, blank=True)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    delivery_date = models.DateField('Дата доставки', blank=True, null=True)
    attachment = models.FileField('Вложение', upload_to='uploads/', blank=True, null=True)
    address = models.ForeignKey('Address', on_delete=models.CASCADE, blank=False,
                                null=False, related_name='delivery_address')

    def __str__(self):
        return self.name


