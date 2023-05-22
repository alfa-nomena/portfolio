from typing import Any
from django.http import BadHeaderError
from django.shortcuts import redirect, render
from django.views.generic import TemplateView
from .models import Owner
from .forms import MessageForm
from django.core.mail import send_mail
from django.contrib import messages
# Create your views here.

class HomeTemplateView(TemplateView):
    template_name = "base/index.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["owner"] = Owner.objects.all()[0]
        context['form'] = MessageForm()
        return context
    
def send_message(request):
    if request.method == "POST":
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Message sent")
        else:
            messages.error(request, "Something went wrong. Please try again.")
    else:
        messages.error(request, "Something went wrong. Please try again.")
            
    return redirect("base:home")