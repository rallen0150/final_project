from django.contrib import admin

from foodtruck.models import Menu, Category, Foodtruck, Profile, Comment, Reply, Truck_Rating

admin.site.register([Menu, Category, Foodtruck, Profile, Comment, Reply, Truck_Rating])
