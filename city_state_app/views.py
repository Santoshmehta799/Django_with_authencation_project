from django.shortcuts import render

from city_state_app import models

# Create your views here.


india = models.Country.objects.get(name="INDIA")

print("=================>>",india)