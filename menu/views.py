from pyexpat import model
from re import template
from django.shortcuts import render
from django.views.generic import ListView
from .models import *

# Create your views here.
class CoffeeListView(ListView):
  model = Coffee
  template_name = 'menu/coffee.html'
  context_object_name = 'coffee_list'
  
class BeverageListView(ListView):
  model = Beverage
  template_name = 'menu/beverage.html'
  context_object_name = 'beverage_list'
  
  
class FoodListView(ListView):
  model = Food
  template_name = 'menu/food.html'
  context_object_name = 'food_list'
  
