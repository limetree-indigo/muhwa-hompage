from django.urls import path
from .views import *

app_name = 'menu'

urlpatterns = [
  path('coffee/', CoffeeListView.as_view(), name='coffee'),
  path('beverage/', BeverageListView.as_view(), name='beverage'),
  path('food/', FoodListView.as_view(), name='food'),
]