from django.db import models


class Menu(models.Model):
    food = models.CharField(max_length=255)
    price = models.FloatField()
    truck = models.ForeignKey('foodtruck.Foodtruck')

    def __str__(self):
        return self.food


class Category(models.Model):
    food_type = models.CharField(max_length=255)

    def __str__(self):
        return self.food_type

class Foodtruck(models.Model):
    driver = models.ForeignKey('auth.User')
    truck_name = models.CharField(max_length=255)
    picture = models.FileField(null=True, blank=True)
    category = models.ForeignKey(Category)
    # menu = models.ManyToManyField(Menu)
    latitude = models.FloatField()
    longitude = models.FloatField()
    checked_in = models.BooleanField(default=False)


    def __str__(self):
        return self.truck_name

class Commenter(models.Model):
    user = models.ForeignKey('auth.User')
    image = models.FileField(null=True, blank=True)
    favorite = models.ManyToManyField(Foodtruck, blank=True)

    def __str__(self):
        return self.user

class Comment(models.Model):
    user = models.ForeignKey('auth.User')
    comment = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    truck_comment = models.ForeignKey('foodtruck.Foodtruck', null=True, blank=True)

    def __str__(self):
        return self.comment
