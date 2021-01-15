from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.

class Item(models.Model):

    image = models.ImageField(upload_to = 'pics/')
    name = models.CharField(max_length=50,blank=True)	   
    price = models.CharField(max_length=50, blank=True)	
    category = models.ForeignKey('Category', on_delete=models.CASCADE, null='True', blank=True)
    date_posted = models.DateTimeField(default=timezone.now)
    

    def __str__(self):
        return self.name

    @classmethod
    def search_by_name(cls, search_term):
        images = cls.objects.filter(name__icontains=search_term)
        return images 

class Category(models.Model):

    name = models.CharField(max_length=50,blank=True)	
    
    def __str__(self):
        return self.name
    