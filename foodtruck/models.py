from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
import googlemaps
from django.contrib.auth.models import User
from django.db.models import Avg

from rest_framework.authtoken.models import Token
from django.conf import settings

# For token
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

gmaps = googlemaps.Client(key='AIzaSyCJ2GhgOOCaoypV0JCC4NnxS-M0enWpN64')

class Menu(models.Model):
    food = models.CharField(max_length=255)
    price = models.FloatField()
    truck = models.ForeignKey('foodtruck.Foodtruck')

    def __str__(self):
        return self.food

    # @property
    # def get_food(self):
    #     return self.food.filter(truck=self)

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
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    checked_in = models.BooleanField(default=False)
    # truck_comment = models.ForeignKey('foodtruck.Comment', null=True, blank=True)
    address = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.truck_name

    @property
    def avg_rating(self):
        return round(Truck_Rating.objects.filter(truck_rated=self).aggregate(Avg('rating')).get('rating__avg'))

    @property
    def show_avg_rating(self):
        return Truck_Rating.objects.filter(truck_rated=self).aggregate(Avg('rating')).get('rating__avg')

    @property
    def get_comment(self):
        return Comment.objects.filter(truck_comment=self)

    @property
    def find_address(self):
        reverse_geocode_result = gmaps.reverse_geocode((self.latitude, self.longitude))
        return reverse_geocode_result[0]['formatted_address']

    @property
    def find_lat_lng(self):
        geocode_result = gmaps.geocode(self.address)
        return(geocode_result[0]['geometry']['location'])

    @property
    def get_user(self):
        return Profile.objects.filter(user=self)

    @property
    def image_url(self):
        if self.picture:
            return self.picture.url
        return "https://upload.wikimedia.org/wikipedia/commons/5/55/Question_Mark.svg"

STATUS = [
    ('T', 'Truck Driver'),
    ('A', 'User Account')
]


class Profile(models.Model):
    user = models.OneToOneField('auth.User')
    image = models.FileField(null=True, blank=True)
    favorite = models.ManyToManyField(Foodtruck, blank=True)
    status = models.CharField(max_length=1, choices=STATUS)
    email = models.EmailField(null=True, blank=True)

    @property
    def contents(self):
        return self.favorite.all()

    @property
    def is_driver(self):
        return self.status == 'T'

    @property
    def is_user(self):
        return self.status == 'A'

    @property
    def image_url(self):
        if self.image:
            return self.image.url
        return "https://dhqbrvplips7x.cloudfront.net/webchat/1.0.23/agent-e202505f.png"

    # def __str__(self):
    #     return self.contents

@receiver(post_save, sender=User)
def create(**kwargs):
    created = kwargs['created']
    instance = kwargs['instance']
    if created:
        Profile.objects.create(user=instance)

class Comment(models.Model):
    user = models.ForeignKey('auth.User')
    comment = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    truck_comment = models.ForeignKey('foodtruck.Foodtruck')

    def __str__(self):
        return self.comment

    def get_reply(self):
        return Reply.objects.filter(comment=self)

class Reply(models.Model):
    comment = models.ForeignKey(Comment)
    reply = models.TextField()
    user = models.ForeignKey('auth.User')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.reply

class Truck_Rating(models.Model):
    rater = models.ForeignKey('auth.User')
    rating = models.IntegerField()
    truck_rated = models.ForeignKey(Foodtruck)
