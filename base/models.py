from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Owner(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    short_description = models.TextField(null=True)
    description = models.TextField(null=True)
    image = models.ImageField(upload_to="about", default="moi.png", null=True)
    name = lambda self: f"{self.user.first_name} {self.user.last_name}"
    cv = models.FileField("Curriculum Vitae", upload_to="owner", blank=True, null=True,)
    class Meta:
        verbose_name = "About me"
        verbose_name_plural = "About me"
        
    def __str__(self) -> str:
        return f"{self.user.first_name} {self.user.last_name}"

class Skill(models.Model):
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    duration = models.CharField(max_length=100)
    logo = models.ImageField(upload_to="skill", null=True)
    
    def __str__(self):
        return self.name

class SkillDetail(models.Model):
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)
    level = models.IntegerField(
        default=50, 
        validators=[
            MaxValueValidator(100),
            MinValueValidator(1)
        ]
    )
    
class Qualification(models.Model):
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='qualification', null=True)

class QualificationDetail(models.Model):
    qualification = models.ForeignKey(Qualification, on_delete=models.CASCADE)
    start = models.DateField()
    end = models.DateField(default=timezone.now)
    name = models.CharField(max_length=100)
    detail = models.CharField(max_length=100)
        
class Service(models.Model):
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    name = models.CharField("Service name",max_length=100)
    logo = models.ImageField(upload_to="services", null=True)
    
    def __str__(self):
        return self.name

class ServiceDetail(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    description = models.CharField("Service name",max_length=100)
    
class Portfolio(models.Model):
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    link = models.URLField()
    description = models.TextField()
    

    def __str__(self):
        return self.name
