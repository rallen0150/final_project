from django.contrib import admin

from foodtruck.models import Menu, Category, Foodtruck, Commenter, Comment, Reply

admin.site.register([Menu, Category, Foodtruck, Commenter, Comment, Reply])
