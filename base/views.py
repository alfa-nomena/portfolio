from typing import Any
from django.views.generic import TemplateView
from .models import *
# Create your views here.

class HomeTemplateView(TemplateView):
    template_name = "base/index.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["owner"] = Owner.objects.all()[0]
        return context
    
