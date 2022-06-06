from django.shortcuts import render
from django.views.generic import (TemplateView, ListView, CreateView, DetailView, FormView)
from django.contrib import messages
from django.urls import reverse
from django.views.generic.detail import SingleObjectMixin
from django.http import HttpResponseRedirect
from .models import Delivery, Address
from django.views.generic import View
from django.views.generic import (TemplateView, ListView, CreateView, DetailView, FormView)
from django.urls import reverse_lazy
from .forms import AddressDeliveryFormset

class HomeView(TemplateView):
    template_name = 'home.html'

class AddressListView(ListView):
    model = Address
    template_name = 'delivery/address_list.html'

class AddressDetailView(DetailView):
    model = Address
    template_name = 'delivery/address_detail.html'


###########
class AddressCreateView(CreateView):
    model = Address
    template_name = 'delivery/address_create.html'
    fields = ['name',]

    def form_valid(self, form):

        messages.add_message(
            self.request,
            messages.SUCCESS,
            'The address has been added'
        )

        return super().form_valid(form)

class AddressDeliveryEditView(SingleObjectMixin, FormView):

    model = Address
    template_name = 'delivery/address_delivery_edit.html'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=Address.objects.all())
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=Address.objects.all())
        return super().post(request, *args, **kwargs)

    def get_form(self, form_class=None):
        return AddressDeliveryFormset(**self.get_form_kwargs(), instance=self.object)

    def form_valid(self, form):
        form.save()

        messages.add_message(
            self.request,
            messages.SUCCESS,
            'Changes were saved.'
        )

        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse('delivery:address_detail', kwargs={'pk': self.object.pk})


##########
'''class DeliveryCreateView(View):
    model = Delivery
    template_name = 'delivery/delivery_new.html'
    form_class = DeliveryForm
    success_url = reverse_lazy('delivery_new')

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(self.success_url)
        else:
            return render(request, self.template_name, {'form': form})'''


