from django.contrib import admin

from foodtruck.models import Menu, Category, Foodtruck

admin.site.register([Menu, Category, Foodtruck])
