from haystack import indexes

from foodtruck.models import Foodtruck


class FoodtruckIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    driver = indexes.CharField(model_attr='driver')
    truck_name = indexes.CharField(model_attr='truck_name')
    category = indexes.CharField(model_attr='category')
    checked_in = indexes.CharField(model_attr='checked_in')

    def get_model(self):
        return Foodtruck
