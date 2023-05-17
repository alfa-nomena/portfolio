from typing import Any
from django.views.generic import TemplateView
from .models import *
# Create your views here.

class HomeTemplateView(TemplateView):
    template_name = "base/index.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["owner"] = Owner.objects.get(pk=1)
        context['services'] = Service.objects.all()[:3]
        # context["softs"] = SoftSkill.objects.filter(owner=context["owner"])
        # context['works'] = Work.objects.all()[:2]
        
        
        return context
    
