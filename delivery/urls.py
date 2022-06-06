from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'delivery'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('addresses/', views.AddressListView.as_view(), name='list_address'),
    path('addresses/<int:pk>/', views.AddressDetailView.as_view(), name='address_detail'),
    path('addresses/add/', views.AddressCreateView.as_view(), name='add_address'),
    path('addresses/<int:pk>/delivery/edit/', views.AddressDeliveryEditView.as_view(), name='address_delivery_edit')

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)