from django.conf import settings
from django.conf.urls import url
from django.urls import path,include
from django.contrib import admin
from django.conf.urls.static import static

urlpatterns = [
    path('admin/',admin.site.urls),
    path('',include('apps.core.urls')),
    path('vendors/',include('apps.vendors.urls')),
    path('',include('apps.products.urls')),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

