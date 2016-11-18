from rest_framework import serializers

from foodtruck.models import Category, Comment, Profile, Foodtruck, Menu

class FoodtruckSerializer(serializers.ModelSerializer):
    # get_food = serializers.ReadOnlyField()
    class Meta:
        model = Foodtruck
        fields = '__all__'
