from re import template
from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

urlpatterns = [
    path('', views.vendor,name='vendor'),
    path('vendor_admin/', views.vendor_admin,name='vendor_admin'),

    path('logout/',auth_views.LogoutView.as_view(),name='logout'),
    path('login/',auth_views.LoginView.as_view(template_name='vendors/login.html'),name='login')
]