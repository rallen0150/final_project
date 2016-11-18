from django.contrib import admin

from foodtruck.models import Menu, Category, Foodtruck, Profile, Comment, Reply

admin.site.register([Menu, Category, Foodtruck, Profile, Comment, Reply])
