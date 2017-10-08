from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login

from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, FormView

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from foodtruck.serializers import FoodtruckSerializer, ProfileSerializer, RatingSerializer
from foodtruck.permissions import IsUser, IsProfileUser
from rest_framework.permissions import IsAuthenticated

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from foodtruck.forms import ContactForm, MultipleEmailForm
from django.core.mail import send_mail

from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect

from django.contrib.auth.mixins import PermissionRequiredMixin

from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from foodtruck.models import Category, Foodtruck, Menu, Profile, Comment, Reply, Truck_Rating, Profile_Comment, Profile_Reply

class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['truck_list'] = Foodtruck.objects.all()
        context['login'] = AuthenticationForm
        return context

class UserCreateView(FormView):
    template_name = "auth/user_form.html"
    model = User
    form_class = UserCreationForm
    # success_url = reverse_lazy('index_view')

    def get_success_url(self, **kwargs):
      return reverse_lazy('profile_update_view')

    # Had to look this up on StackOverflow
    def form_valid(self, form):
      #save the new user first
      form.save()
      #get the username and password
      username = self.request.POST['username']
      password = self.request.POST['password1']
      #authenticate user then login
      user = authenticate(username=username, password=password)
      login(self.request, user)
      return super(UserCreateView, self).form_valid(form)

class CategoryCreateView(CreateView):
    model = Category
    fields = ('food_type', )
    success_url = reverse_lazy('index_view')

class FoodtruckCreateView(CreateView):
    model = Foodtruck
    fields = ('truck_name', 'picture', 'category', 'address', 'checked_in', 'start_time', 'end_time')
    success_url = reverse_lazy('foodtruck_list_view')
    # def get_success_url(self, *args, **kwargs):
    #     x = Foodtruck.objects.get(id=self.kwargs['pk'])
    #     return reverse('foodtruck_detail_view', args=[x])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context

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
        context['profile'] = Profile.objects.all()
        return context

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class FoodtruckUpdateView(UpdateView):
    template_name = 'foodtruck/foodtruck_update.html'
    model = Foodtruck
    fields = ('truck_name', 'picture')
    # success_url = reverse_lazy('index_view')

    def get_success_url(self, **kwargs):
        return reverse_lazy('foodtruck_detail_view', args=[int(self.kwargs['pk'])])

class FoodtruckListView(ListView):
    model = Foodtruck
    paginate_by = 8

class MenuCreateView(CreateView):
    model = Menu
    fields = ('food', 'price')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = Menu.objects.get(id=self.kwargs['pk'])
        return context

    def get_success_url(self, **kwargs):
        return reverse_lazy('menu_create_view', args=[int(self.kwargs['pk'])])

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.truck = Foodtruck.objects.get(id=self.kwargs['pk'])
        return super().form_valid(form)

class FoodUpdateView(UpdateView):
    template_name = 'foodtruck/food_update.html'
    model = Menu
    fields = ('food', )
    def get_success_url(self, *args, **kwargs):
        x = Menu.objects.get(id=self.kwargs['pk']).truck.id
        return reverse('foodtruck_detail_view', args=[x])

class PriceUpdateView(UpdateView):
    template_name = 'foodtruck/price_update.html'
    model = Menu
    fields = ('price', )
    def get_success_url(self, *args, **kwargs):
        x = Menu.objects.get(id=self.kwargs['pk']).truck.id
        return reverse('foodtruck_detail_view', args=[x])

class MenuDetailView(DetailView):
    model = Menu

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = Menu.objects.filter(truck=self.kwargs['pk'])
        return context

class LocationUpdateView(UpdateView):
    template_name = "foodtruck/location_update.html"
    model = Foodtruck
    fields = ('address', 'start_time', 'end_time')
    # success_url = reverse_lazy('index_view')

    def get_success_url(self, **kwargs):
        return reverse_lazy('foodtruck_email_view', args=[int(self.kwargs['pk'])])

class CheckinUpdateView(UpdateView):
    template_name = "foodtruck/checkin_update.html"
    model = Foodtruck
    fields = ('checked_in', )
    # success_url = reverse_lazy('index_view')

    def get_success_url(self, **kwargs):
        return reverse_lazy('success_change_location_view', args=[int(self.kwargs['pk'])])

    # def form_valid(self, form):
    #     instance = form.save(commit=False)
    #     return super().form_valid(form)


class ProfileUpdateView(UpdateView):
    template_name = 'foodtruck/profile_update.html'
    fields = ('image', 'status')
    # success_url = reverse_lazy('index_view')
    def get_object(self):
        return Profile.objects.get(user=self.request.user)


    def get_success_url(self, **kwargs):
        return reverse('profile_detail_view', args=[self.request.user.pk])

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.user = self.request.user
        return super().form_valid(form)

class CommentCreateView(CreateView):
    model = Comment
    fields = ('comment', )
    # success_url = reverse_lazy('index_view')

    def get_success_url(self, **kwargs):
        return reverse_lazy('foodtruck_detail_view', args=[int(self.kwargs['pk'])])

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.user = self.request.user
        instance.truck_comment = Foodtruck.objects.get(id=self.kwargs['pk'])
        return super().form_valid(form)

class CommentUpdateView(UpdateView):
    model = Comment
    fields = ('comment', )
    # success_url = reverse_lazy('index_view')

    def get_success_url(self, *args, **kwargs):
        x = Comment.objects.get(id=self.kwargs['pk']).truck_comment.id
        return reverse('foodtruck_detail_view', args=[x])

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
    # success_url = reverse_lazy('index_view')

    def get_success_url(self, *args, **kwargs):
        x = Comment.objects.get(id=self.kwargs['pk']).truck_comment.id
        return reverse('foodtruck_detail_view', args=[x])

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.user = self.request.user
        instance.comment = Comment.objects.get(id=self.kwargs['pk'])
        return super().form_valid(form)

    # def get_success_url(self, **kwargs):
    #     return reverse_lazy('foodtruck_detail_view', args=[int(self.kwargs['pk'])])

class ReplyUpdateView(UpdateView):
    model = Reply
    fields = ('reply', )
    # success_url = reverse_lazy('index_view')

    def get_success_url(self, *args, **kwargs):
        x = Reply.objects.get(id=self.kwargs['pk']).comment.truck_comment.id
        return reverse('foodtruck_detail_view', args=[x])

class ProfileDetailView(DetailView):
    model = Profile

    # def get_object(self):
    #     return Commenter.objects.get(user=self.request.user)

class ProfileCommentCreateView(CreateView):
    model = Profile_Comment
    fields = ('comment', )
    # success_url = reverse_lazy('index_view')

    def get_success_url(self, **kwargs):
        return reverse_lazy('profile_detail_view', args=[int(self.kwargs['pk'])])

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.user = self.request.user
        instance.profile_comment = Profile.objects.get(id=self.kwargs['pk'])
        return super().form_valid(form)

class ProfileCommentUpdateView(UpdateView):
    model = Profile_Comment
    fields = ('comment', )
    # success_url = reverse_lazy('index_view')

    def get_success_url(self, *args, **kwargs):
        x = Profile_Comment.objects.get(id=self.kwargs['pk']).profile_comment.id
        return reverse('profile_detail_view', args=[x])

    # def get_success_url(self, **kwargs):
    #     return reverse_lazy('profile_detail_view', args=[int(self.kwargs['pk'])])

class ProfileReplyCreateView(CreateView):
    model = Profile_Reply
    fields = ('reply', )
    # success_url = reverse_lazy('index_view')

    def get_success_url(self, *args, **kwargs):
        x = Profile_Comment.objects.get(id=self.kwargs['pk']).profile_comment.id
        return reverse('profile_detail_view', args=[x])

    # def get_success_url(self, **kwargs):
    #     return reverse_lazy('foodtruck_detail_view', args=[int(self.kwargs['pk'])])

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.user = self.request.user
        instance.comment = Profile_Comment.objects.get(id=self.kwargs['pk'])
        return super().form_valid(form)

class ProfileReplyUpdateView(UpdateView):
    model = Profile_Reply
    fields = ('reply', )
    # success_url = reverse_lazy('index_view')

    def get_success_url(self, *args, **kwargs):
        x = Profile_Reply.objects.get(id=self.kwargs['pk']).comment.profile_comment.id
        return reverse('profile_detail_view', args=[x])

class ImageUpdateView(UpdateView):
    template_name = "foodtruck/image_update.html"
    model = Profile
    fields = ('image', )
    # success_url = reverse_lazy('index_view')

    def get_success_url(self, **kwargs):
        return reverse_lazy('profile_detail_view', args=[int(self.kwargs['pk'])])

class FavoriteUpdateView(UpdateView):
    model = Profile
    fields = ('favorite', )
    # success_url = reverse_lazy('index_view')

    def get_success_url(self, **kwargs):
        return reverse_lazy('foodtruck_detail_view', args=[int(self.kwargs['pk'])])

    # Davis helped with the def post!
    def post(self, request, pk):
        favorite = self.request.POST.get('favorite')
        profile = Profile.objects.get(user=self.request.user)
        if favorite == 'Favorite':
            profile.favorite.add(Foodtruck.objects.get(id=self.kwargs['pk']))
        else:
            profile.favorite.remove(Foodtruck.objects.get(id=self.kwargs['pk']))
        return HttpResponseRedirect(reverse_lazy('foodtruck_detail_view', args=[int(self.kwargs['pk'])]))

class EmailUpdateView(UpdateView):
    template_name = "foodtruck/email_update.html"
    model = Profile
    fields = ('email', )
    # success_url = reverse_lazy('index_view')

    def get_success_url(self, **kwargs):
        return reverse_lazy('profile_detail_view', args=[int(self.kwargs['pk'])])

class ProfileListAPIView(ListAPIView):
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

class MapView(TemplateView):
    template_name = 'map.html'

class FoodtruckEmailView(FormView):
    template_name = 'email_users.html'
    # success_url = reverse_lazy("contact_me_view")
    form_class = MultipleEmailForm

    def get_success_url(self, **kwargs):
        return reverse_lazy('success_change_location_view', args=[int(self.kwargs['pk'])])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['trucks'] = Foodtruck.objects.get(id=self.kwargs['pk'])
        return context

    def form_valid(self, form):
        form.send_email(self.kwargs['pk'])
        return super().form_valid(form)

class MapTestView(TemplateView):
    template_name = 'map_test.html'

class AboutMeView(TemplateView):
    template_name = "about.html"

class SuccessChangeLocationView(TemplateView):
    template_name = 'foodtruck/success_location.html'
    model = Foodtruck

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['truck'] = Foodtruck.objects.get(id=self.kwargs['pk'])
        return context
