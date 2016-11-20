from django.conf.urls import url, include
from django.contrib import admin

from django.conf.urls.static import static
from django.conf import settings

from foodtruck.views import IndexView, UserCreateView, CategoryCreateView, \
                            FoodtruckCreateView, MenuCreateView, FoodtruckDetailView, \
                            FoodUpdateView, PriceUpdateView, LocationUpdateView, \
                            CheckinUpdateView, FoodtruckUpdateView, ProfileUpdateView, \
                            CommentCreateView, CommentUpdateView, FoodtruckListAPIView, \
                            FoodtruckDetailUpdateDestroyAPIView, ReplyCreateView, ProfileDetailView, \
                            ImageUpdateView, FavoriteUpdateView, MapTestView, ProfileListCreateAPIView, \
                            ProfileDetailUpdateDestroyAPIView

from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', IndexView.as_view(), name='index_view'),
    url(r'^', include('django.contrib.auth.urls'), name='login'),
    url(r'^search/', include('haystack.urls'), name='search_url'),
    url(r'^obtain-token/$', obtain_auth_token),
    url(r'^new_user/$', UserCreateView.as_view(), name='user_create_view'),
    url(r'^new_category/$', CategoryCreateView.as_view(), name='category_create_view'),
    url(r'^new_foodtruck/$', FoodtruckCreateView.as_view(), name='foodtruck_create_view'),
    url(r'^create_menu/$', MenuCreateView.as_view(), name='menu_create_view'),
    url(r'^foodtruck/(?P<pk>\d+)/$', FoodtruckDetailView.as_view(), name='foodtruck_detail_view'),
    url(r'^foodtruck/(?P<pk>\d+)/update/$', FoodtruckUpdateView.as_view(), name='foodtruck_update_view'),
    url(r'^food/update/(?P<pk>\d+)/$', FoodUpdateView.as_view(), name='food_update_view'),
    url(r'^price/update/(?P<pk>\d+)/$', PriceUpdateView.as_view(), name='price_update_view'),
    url(r'^new_location/(?P<pk>\d+)/$', LocationUpdateView.as_view(), name='location_update_view'),
    url(r'^checkin/(?P<pk>\d+)/$', CheckinUpdateView.as_view(), name='checkin_update_view'),
    url(r'^account/profile/(?P<pk>\d+)/$', ProfileUpdateView.as_view(), name='profile_update_view'),
    url(r'^foodtruck/(?P<pk>\d+)/comment/$', CommentCreateView.as_view(), name='comment_create_view'),
    url(r'^(?P<pk>\d+)/update/comment/$', CommentUpdateView.as_view(), name='comment_update_view'),
    url(r'^api/foodtrucks/$', FoodtruckListAPIView.as_view(), name='foodtruck_list_api_view'),
    url(r'^api/foodtrucks/(?P<pk>\d+)/$', FoodtruckDetailUpdateDestroyAPIView.as_view(), name='foodtruck_detail_update_api_view'),
    url(r'^comment/(?P<pk>\d+)/reply/$', ReplyCreateView.as_view(), name='reply_create_view'),
    url(r'^account/profile/(?P<pk>\d+)/detail/$', ProfileDetailView.as_view(), name='profile_detail_view'),
    url(r'^account/profile/(?P<pk>\d+)/image/$', ImageUpdateView.as_view(), name='image_update_view'),
    url(r'^account/profile/(?P<pk>\d+)/favorite/$', FavoriteUpdateView.as_view(), name='favorite_update_view'),
    url(r'^api/profile/$', ProfileListCreateAPIView.as_view(), name='profile_list_create_api_view'),
    url(r'^api/profile/(?P<pk>\d+)/$', ProfileDetailUpdateDestroyAPIView.as_view(), name='profile_detail_update_destroy_api_view'),
    url(r'^map/test/$', MapTestView.as_view()),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
