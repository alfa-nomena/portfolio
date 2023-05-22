from django.urls import path
from .views import *

app_name="base"
urlpatterns = [
    path('home/', HomeTemplateView.as_view(), name='home'),
    path('message/', send_message, name="message")
]
