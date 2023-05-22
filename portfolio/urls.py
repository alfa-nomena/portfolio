from django.contrib import admin
from django.shortcuts import redirect
from django.urls import path, include

from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', lambda x : redirect('base:home', permanent=False)),
    path('portfolio/', include('base.urls')),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
