from django.db import models

# Create your models here.
from django.db import models
from users.models import User
from users.forms import UserProfileForm
# Create your models here.

class Sports(models.Model):
    name = models.CharField(max_length=256)
    level = models.CharField(max_length=256)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='sport_images')

class Basket(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    sport = models.ForeignKey(to=Sports, on_delete=models.CASCADE)
    created_timestamp = models.DateTimeField(auto_now_add=True)

class EducationProgramm(models.Model):
    studyduration = models.CharField(max_length=256)
    name = models.CharField(max_length=256)
    modeofstudy = models.CharField(max_length=256)
    degree = models.CharField(max_length=256)
    fieldofstudy = models.CharField(max_length=256)
    image = models.ImageField(upload_to='products_images')

    class Meta:
        verbose_name = 'Образовательная программа'
        verbose_name_plural = 'Образовательные программы'