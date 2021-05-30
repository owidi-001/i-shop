from django.urls import path
from . import views

urlpatterns = [
    path('', views.vendor,name='vendor'),
    path('', views.vendor_admin,name='vendor_admin'),
]