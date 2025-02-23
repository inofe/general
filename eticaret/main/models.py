from django.db import models
from django.urls import reverse

# Create your models here.



#This! is the proper model    
class User(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    points=models.IntegerField()
    is_active=models.BooleanField(default=True)

    #dinamik url olusturup kolayca cagirmak icin    
    def get_absolute_url(self):
        return reverse("main:user",kwargs={"pk":self.id})