from rest_framework import serializers

from foodtruck.models import Category, Comment, Profile, Foodtruck, Menu, Truck_Rating

class FoodtruckSerializer(serializers.ModelSerializer):
    # get_food = serializers.ReadOnlyField()
    show_avg_rating = serializers.FloatField()
    class Meta:
        model = Foodtruck
        fields = '__all__'

class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = '__all__'

class RatingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Truck_Rating
        fields = ('truck_rated', 'rating')
