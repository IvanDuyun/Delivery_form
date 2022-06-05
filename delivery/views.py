from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .forms import DeliveryForm
from .models import Delivery
from django.views.generic import View
from django.urls import reverse_lazy

class DeliveryCreateView(View):
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
            return render(request, self.template_name, {'form': form})


