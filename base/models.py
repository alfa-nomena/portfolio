from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class Owner(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    short_description = models.TextField(null=True)
    title = models.CharField(max_length=100)
    description = models.TextField(null=True)
    profile_picture = models.ImageField(upload_to="images/about", null=True)
    cover_picture = models.ImageField(upload_to="images/about", null=True)
    name = lambda self: f"{self.user.first_name} {self.user.last_name}"
    cv = models.FileField("Curriculum Vitae", upload_to="document/owner", blank=True, null=True)
    phone_number = PhoneNumberField(blank=True, null=True)
    location = models.CharField(max_length=100)
    class Meta:
        verbose_name = "About me"
        verbose_name_plural = "About me"
    def current_name(self):
        return self.user.first_name.split()[-1] or ''
    def __str__(self) -> str:
        return f"{self.user.first_name} {self.user.last_name}"

class AbstractAbout(models.Model):
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    
    class Meta:
        abstract=True

    def __str__(self):
        return self.title
class AbstractWithLogo(AbstractAbout):
    class_logo = models.CharField(max_length=50)
    class Meta:
        abstract=True
class Skill(AbstractWithLogo):
    pass
    
    

class SkillDetail(models.Model):
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    level = models.IntegerField(
        default=50, 
        validators=[
            MaxValueValidator(100),
            MinValueValidator(1)
        ]
    )
    def __str__(self):
        return f"{self.skill} - {self.name}"
    
class Qualification(AbstractWithLogo):
    pass

class QualificationDetail(models.Model):
    qualification = models.ForeignKey(Qualification, on_delete=models.CASCADE)
    start = models.DateField()
    end = models.DateField(null=True, blank=True)
    name = models.CharField(max_length=100)
    detail = models.CharField(max_length=100)
    
    def duration(self):
        end = f"- {self.end.strftime('%m/%Y')}" if self.end else ''
        return f"{self.start.strftime('%m/%Y')} {end}"
    def __str__(self):
        return f"{self.qualification} - {self.name}"
        
class Service(AbstractWithLogo):
    pass

class ServiceDetail(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    description = models.CharField("Service name",max_length=100)
    
    def __str__(self):
        return f"{self.service} - {self.description}"
    
class Project(AbstractAbout):
    link = models.URLField()
    description = models.TextField()
    image = models.ImageField(upload_to='images/projects', null=True)
    source = models.URLField()
    detail = models.URLField()

    def __str__(self):
        return self.title

class SocialMediaContact(AbstractAbout):
    link = models.URLField(blank=True, null=True)
    pseudo = models.CharField("name",max_length=100)
    class_logo = models.CharField(max_length=50)
    
class Message(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField(null=False, blank=False)
    def __str__(self):
        return f"{self.title} - {self.name}"