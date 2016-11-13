from django.contrib import admin

from foodtruck.models import Menu, Category, Foodtruck, Commenter

admin.site.register([Menu, Category, Foodtruck, Commenter])
