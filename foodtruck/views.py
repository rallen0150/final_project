from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView, UpdateView

from django.urls import reverse_lazy
from foodtruck.models import Category, Foodtruck, Menu

class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['truck_list'] = Foodtruck.objects.all()
        return context

class UserCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('index_view')

class CategoryCreateView(CreateView):
    model = Category
    fields = ('food_type', )
    success_url = reverse_lazy('index_view')

class FoodtruckCreateView(CreateView):
    model = Foodtruck
    fields = ('truck_name', 'picture', 'category', 'latitude', 'longitude', 'checked_in')
    success_url = reverse_lazy('menu_create_view')

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.driver = self.request.user
        return super().form_valid(form)

class FoodtruckDetailView(ListView):
    model = Foodtruck

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = Menu.objects.filter(truck=self.kwargs['pk'])
        return context

class MenuCreateView(CreateView):
    model = Menu
    fields = ('food', 'price', 'truck')
    success_url = reverse_lazy('index_view')

    # def form_valid(self, form):
    #     instance = form.save(commit=False)
    #     instance.truck = self.truck.driver
    #     return super().form_valid(form)

class FoodUpdateView(UpdateView):
    model = Menu
    fields = ('food', )
    success_url = reverse_lazy('index_view')

class PriceUpdateView(UpdateView):
    model = Menu
    fields = ('price', )
    success_url = reverse_lazy('index_view')

class LocationUpdateView(UpdateView):
    model = Foodtruck
    fields = ('latitude', 'longitude')
    success_url = reverse_lazy('index_view')
