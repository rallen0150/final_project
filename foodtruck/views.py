from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, FormView

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from foodtruck.serializers import FoodtruckSerializer, ProfileSerializer, RatingSerializer
from foodtruck.permissions import IsUser, IsProfileUser
from rest_framework.permissions import IsAuthenticated

from foodtruck.forms import ContactForm
from django.core.mail import send_mail

from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from foodtruck.models import Category, Foodtruck, Menu, Profile, Comment, Reply, Truck_Rating

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
    fields = ('truck_name', 'picture', 'category', 'address', 'checked_in')
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
    fields = ('address', )
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

class EmailUpdateView(UpdateView):
    model = Profile
    fields = ('email', )
    success_url = reverse_lazy('index_view')

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

class TruckRatingListCreateAPIView(ListCreateAPIView):
    queryset = Truck_Rating.objects.all()
    serializer_class = RatingSerializer

    def perform_create(self, serializer):
        Truck_Rating.objects.filter(rater=self.request.user, truck_rated=serializer.validated_data["truck_rated"]).delete()
        serializer.save(rater=self.request.user)

class TruckRatingDetailUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Truck_Rating.objects.all()
    serializer_class = RatingSerializer

class ContactMeView(TemplateView):
    template_name = 'contact.html'

    def get_context_data(self):
        context = super().get_context_data()
        context['form'] = ContactForm()
        return context

class SendMailView(FormView):
    template_name = 'contact.html'
    success_url = reverse_lazy("contact_me_view")
    form_class = ContactForm

    def form_valid(self, form):
        form.send_email()
        return super().form_valid(form)

class MapTestView(TemplateView):
    template_name = 'map_test.html'
