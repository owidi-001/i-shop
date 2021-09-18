from django.conf.urls import url
from django.urls import path,include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    path('',include('apps.core.urls')),
    path('vendors/',include('apps.vendors.urls')),
]
