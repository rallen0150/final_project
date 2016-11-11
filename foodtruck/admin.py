from django.contrib import admin

from foodtruck.models import Menu, Category, Foodtruck, Location

admin.site.register([Menu, Category, Foodtruck, Location])
