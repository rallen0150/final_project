from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from foodtruck.serializers import FoodtruckSerializer
from foodtruck.permissions import IsUser

from django.urls import reverse_lazy
from foodtruck.models import Category, Foodtruck, Menu, Commenter, Comment, Reply

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

class FoodtruckDetailView(DetailView):
    model = Foodtruck

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['truck'] = Foodtruck.objects.all()
        return context

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = Menu.objects.filter(truck=self.kwargs['pk'])
        return context

class FoodtruckUpdateView(UpdateView):
    model = Foodtruck
    fields = ('truck_name', 'picture')
    success_url = reverse_lazy('index_view')

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

class CheckinUpdateView(UpdateView):
    model = Foodtruck
    fields = ('checked_in', )
    success_url = reverse_lazy('index_view')

    # def form_valid(self, form):
    #     instance = form.save(commit=False)
    #     return super().form_valid(form)

class CommenterCreateView(CreateView):
    model = Commenter
    fields = ('image', 'favorite')
    success_url = reverse_lazy('index_view')

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.user = self.request.user
        return super().form_valid(form)

class CommentCreateView(CreateView):
    model = Comment
    fields = ('comment', )
    success_url = reverse_lazy('index_view')

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.user = self.request.user
        instance.truck_comment = Foodtruck.objects.get(id=self.kwargs['pk'])
        return super().form_valid(form)

class CommentUpdateView(UpdateView):
    model = Comment
    fields = ('comment', )
    success_url = reverse_lazy('index_view')

class FoodtruckListCreateAPIView(ListCreateAPIView):
    queryset = Foodtruck.objects.all()
    serializer_class = FoodtruckSerializer

class FoodtruckDetailUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Foodtruck.objects.all()
    serializer_class = FoodtruckSerializer
    permission_classes = (IsUser, )

class ReplyCreateView(CreateView):
    model = Reply
    fields = ('reply', )
    success_url = reverse_lazy('index_view')

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.user = self.request.user
        instance.comment = Comment.objects.get(id=self.kwargs['pk'])
        return super().form_valid(form)

class CommenterDetailView(DetailView):
    model = Commenter

    # def get_object(self):
    #     return Commenter.objects.get(user=self.request.user)
