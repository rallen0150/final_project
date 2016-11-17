from django.db import models
import googlemaps

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
    latitude = models.FloatField()
    longitude = models.FloatField()
    checked_in = models.BooleanField(default=False)
    # truck_comment = models.ForeignKey('foodtruck.Comment', null=True, blank=True)
    rating = models.FloatField(null=True, blank=True)

    def __str__(self):
        return self.truck_name

    def get_comment(self):
        return Comment.objects.filter(truck_comment=self)

    def find_address(self):
        reverse_geocode_result = gmaps.reverse_geocode((self.latitude, self.longitude))
        return reverse_geocode_result[0]['formatted_address']

    @property
    def image_url(self):
        if self.picture:
            return self.picture.url
        return "https://upload.wikimedia.org/wikipedia/commons/5/55/Question_Mark.svg"

class Commenter(models.Model):
    user = models.ForeignKey('auth.User')
    image = models.FileField(null=True, blank=True)
    favorite = models.ManyToManyField(Foodtruck, blank=True)

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
