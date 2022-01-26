
from django.db import models
from django.urls import reverse

# Create your models here.

class Coffee(models.Model):
  title = models.CharField(max_length=100)
  photo = models.ImageField(upload_to='coffee/%Y/%m/%d', default='coffee/no_image.png')
  
  desc = models.TextField()
  
  class Meta:
    ordering = ['title']
    
  def __str__(self):
    return self.title
  
class Beverage(models.Model):
  title = models.CharField(max_length=100)
  photo = models.ImageField(upload_to='beverage/%Y/%m/%d', default='beverage/no_image.png')
  
  desc = models.TextField()
  
  class Meta:
    ordering = ['title']
    
  def __str__(self):
    return self.title
  
class Food(models.Model):
  title = models.CharField(max_length=100)
  photo = models.ImageField(upload_to='food/%Y/%m/%d', default='food/no_image.png')
  
  desc = models.TextField()
  
  class Meta:
    ordering = ['title']
    
  def __str__(self):
    return self.title
  
