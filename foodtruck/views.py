
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from foodtruck.serializers import FoodtruckSerializer, ProfileSerializer
from foodtruck.permissions import IsUser, IsProfileUser
from rest_framework.permissions import IsAuthenticated


from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from foodtruck.models import Category, Foodtruck, Menu, Profile, Comment, Reply

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
        context['menu'] = Menu.objects.filter(truck=self.kwargs['pk'])
        context['favorite'] = Profile.objects.all()
        return context

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
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

class ProfileUpdateView(UpdateView):
    model = Profile
    fields = ('image', 'status')
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

class FoodtruckListAPIView(ListAPIView):
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

class ProfileDetailView(DetailView):
    model = Profile

    # def get_object(self):
    #     return Commenter.objects.get(user=self.request.user)

class ImageUpdateView(UpdateView):
    model = Profile
    fields = ('image', )
    success_url = reverse_lazy('index_view')

class FavoriteUpdateView(UpdateView):
    model = Profile
    fields = ('favorite', )
    success_url = reverse_lazy('index_view')

    # Davis helped with the def post!
    def post(self, request, pk):
        favorite = self.request.POST.get('favorite')
        profile = Profile.objects.get(user=self.request.user)
        if favorite == 'Favorite':
            profile.favorite.add(Foodtruck.objects.get(id=self.kwargs['pk']))
        else:
            profile.favorite.remove(Foodtruck.objects.get(id=self.kwargs['pk']))
        return HttpResponseRedirect("/")

class ProfileListCreateAPIView(ListCreateAPIView):
    # queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        return Profile.objects.filter(user=self.request.user)


class ProfileDetailUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    # queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = (IsProfileUser, )

    def get_queryset(self):
        return Profile.objects.filter(user=self.request.user)

class MapTestView(TemplateView):
    template_name = 'map_test.html'
