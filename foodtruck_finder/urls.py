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
                            ImageUpdateView, FavoriteUpdateView, MapTestView, ProfileListAPIView, \
                            ProfileDetailUpdateDestroyAPIView, TruckRatingListCreateAPIView, \
                            TruckRatingDetailUpdateDestroyAPIView, EmailUpdateView, ContactMeView, \
                            SendMailView, MenuDetailView, FoodtruckListView, MapView, FoodtruckEmailView, \
                            ProfileCommentCreateView, ProfileReplyCreateView, ProfileCommentUpdateView, \
                            ProfileReplyUpdateView, ReplyUpdateView, AboutMeView, SuccessChangeLocationView

from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', IndexView.as_view(), name='index_view'),
    url(r'^', include('django.contrib.auth.urls'), name='login'),
    url(r'^search/', include('haystack.urls'), name='search'),
    url(r'^obtain-token/$', obtain_auth_token),
    url(r'^new_user/$', UserCreateView.as_view(), name='user_create_view'),
    url(r'^new_category/$', CategoryCreateView.as_view(), name='category_create_view'),
    url(r'^new_foodtruck/$', FoodtruckCreateView.as_view(), name='foodtruck_create_view'),
    url(r'^foodtruck/(?P<pk>\d+)/create_menu/$', MenuCreateView.as_view(), name='menu_create_view'),
    url(r'^foodtruck/(?P<pk>\d+)/$', FoodtruckDetailView.as_view(), name='foodtruck_detail_view'),
    url(r'^foodtruck/(?P<pk>\d+)/update/$', FoodtruckUpdateView.as_view(), name='foodtruck_update_view'),
    url(r'^item/(?P<pk>\d+)/food/update$', FoodUpdateView.as_view(), name='food_update_view'),
    url(r'^item/(?P<pk>\d+)/price/update$', PriceUpdateView.as_view(), name='price_update_view'),
    url(r'^foodtruck/list/$', FoodtruckListView.as_view(), name='foodtruck_list_view'),
    url(r'^new_location/(?P<pk>\d+)/$', LocationUpdateView.as_view(), name='location_update_view'),
    url(r'^checkin/(?P<pk>\d+)/$', CheckinUpdateView.as_view(), name='checkin_update_view'),
    url(r'^account/profile/$', ProfileUpdateView.as_view(), name='profile_update_view'),
    url(r'^foodtruck/(?P<pk>\d+)/comment/$', CommentCreateView.as_view(), name='comment_create_view'),
    url(r'^(?P<pk>\d+)/update/comment/$', CommentUpdateView.as_view(), name='comment_update_view'),
    url(r'^foodtruck/(?P<pk>\d+)/menu/$', MenuDetailView.as_view(), name='menu_detail_view'),
    url(r'^api/foodtrucks/$', FoodtruckListAPIView.as_view(), name='foodtruck_list_api_view'),
    url(r'^api/foodtrucks/(?P<pk>\d+)/$', FoodtruckDetailUpdateDestroyAPIView.as_view(), name='foodtruck_detail_update_api_view'),
    url(r'^comment/(?P<pk>\d+)/reply/$', ReplyCreateView.as_view(), name='reply_create_view'),
    url(r'^reply/(?P<pk>\d+)/comment/update/$', ReplyUpdateView.as_view(), name='reply_update_view'),
    url(r'^account/profile/(?P<pk>\d+)/detail/$', ProfileDetailView.as_view(), name='profile_detail_view'),
    url(r'^account/profile/(?P<pk>\d+)/image/$', ImageUpdateView.as_view(), name='image_update_view'),
    url(r'^account/profile/(?P<pk>\d+)/favorite/$', FavoriteUpdateView.as_view(), name='favorite_update_view'),
    url(r'^account/profile/(?P<pk>\d+)/email/$', EmailUpdateView.as_view(), name='email_update_view'),
    url(r'^account/profile/(?P<pk>\d+)/comment/$', ProfileCommentCreateView.as_view(), name='profile_comment_create_view'),
    url(r'^profile/comment/(?P<pk>\d+)/reply/$', ProfileReplyCreateView.as_view(), name='profile_reply_create_view'),
    url(r'^account/profile/(?P<pk>\d+)/comment/update/$', ProfileCommentUpdateView.as_view(), name='profile_comment_update_view'),
    url(r'^reply/(?P<pk>\d+)/update/$', ProfileReplyUpdateView.as_view(), name='profile_reply_update_view'),
    url(r'^api/profile/$', ProfileListAPIView.as_view(), name='profile_list_api_view'),
    url(r'^api/profile/(?P<pk>\d+)/$', ProfileDetailUpdateDestroyAPIView.as_view(), name='profile_detail_update_destroy_api_view'),
    url(r'^api/foodtrucks/(?P<pk>\d+)/rating/$', TruckRatingListCreateAPIView.as_view(), name='truck_rating_list_create_api_view'),
    url(r'^api/(?P<pk>\d+)/rating/$', TruckRatingDetailUpdateDestroyAPIView.as_view(), name='truck_rating_detail_update_destroy_api_view'),
    url(r'^contact/$', ContactMeView.as_view(), name='contact_me_view'),
    url(r'^send_mail/$', SendMailView.as_view(), name='send_mail'),
    url(r'^full_map/$', MapView.as_view(), name='map_view'),
    url(r'^foodtruck/(?P<pk>\d+)/email/$', FoodtruckEmailView.as_view(), name='foodtruck_email_view'),
    url(r'^map/test/$', MapTestView.as_view()),
    url(r'^about_me/$', AboutMeView.as_view(), name='about_me'),
    url(r'^foodtruck/(?P<pk>\d+)/location/$', SuccessChangeLocationView.as_view(), name='success_change_location_view'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
