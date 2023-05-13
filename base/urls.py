from django.urls import path
from .views import *

urlpatterns = [
    path('', HomeTemplateView.as_view(), name='home'),
]
