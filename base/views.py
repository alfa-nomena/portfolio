from typing import Any
from django import http
from django.views.generic import TemplateView
from .models import *
from faker import Faker
import numpy as np
# Create your views here.

class HomeTemplateView(TemplateView):
    template_name = "base/index.html"
    def get(self, request, *args, **kwargs):
        owners = Owner.objects.all()
        if not owners:
            
            users = User.objects.all()
            if users:
                user=users[0]
            else:
                user = User.objects.create_user(username='test', password='test', email="hackibosy@gmail.com")
                user.is_superuser = True
                user.is_staff = True
                user = user.save()
            faker = Faker()
            owner = Owner.objects.create(
                user=user,
                short_description = faker.text(100),
                description=faker.text(200),
            )
            owner = owner.save()
            
            for _ in range(2):
                skill = Skill.objects.create(
                    owner=owner,
                    name = faker.text(100),
                    duration = faker.text(100)
                )
                skill = skill.save()
                for _ in range(5):
                    skill_detail = SkillDetail.objects.create(
                        skill=skill,
                        level = np.random.randint(1,101)
                    )
                    skill_detail.save()
            
            for _ in range(2):
                qual = Qualification.objects.create(
                    owner=owner,
                    name = faker.text(100),
                )
                qual = qual.save()
                for _ in range(5):
                    qual_detail = QualificationDetail.objects.create(
                        qualification=qual,
                        start=timezone.now(),
                        end=timezone.now(),
                        name=faker.text(30),
                        detail=faker.text(100)
                    )
                    qual_detail.save()
                    
            for _ in range(2):
                serv = Service.objects.create(
                    owner=owner,
                    name = faker.text(100),
                )
                serv = serv.save()
                for _ in range(5):
                    serv_detail = ServiceDetail.objects.create(
                        service=serv,
                        description=faker.text(100)
                    )
                    qual_detail.save()
            
            for _ in range(3):
                port = Portfolio.objects.create(
                    owner=owner,
                    name = faker.text(30),
                    link = faker.url(),
                    description = faker.text(100)
                )
                port.save()










        return super().get(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["owner"] = Owner.objects.get(pk=1)
        context['services'] = Service.objects.all()[:3]
        # context["softs"] = SoftSkill.objects.filter(owner=context["owner"])
        # context['works'] = Work.objects.all()[:2]
        
        
        return context
    
