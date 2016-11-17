from django.conf.urls import url, include
from django.contrib import admin

from django.conf.urls.static import static
from django.conf import settings

from foodtruck.views import IndexView, UserCreateView, CategoryCreateView, \
                            FoodtruckCreateView, MenuCreateView, FoodtruckDetailView, \
                            FoodUpdateView, PriceUpdateView, LocationUpdateView, \
                            CheckinUpdateView, FoodtruckUpdateView, CommenterCreateView, \
                            CommentCreateView, CommentUpdateView, FoodtruckListCreateAPIView, \
                            FoodtruckDetailUpdateDestroyAPIView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', IndexView.as_view(), name='index_view'),
    url(r'^', include('django.contrib.auth.urls'), name='login'),
    url(r'^new_driver/$', UserCreateView.as_view(), name='user_create_view'),
    url(r'^new_category/$', CategoryCreateView.as_view(), name='category_create_view'),
    url(r'^new_foodtruck/$', FoodtruckCreateView.as_view(), name='foodtruck_create_view'),
    url(r'^create_menu/$', MenuCreateView.as_view(), name='menu_create_view'),
    url(r'^foodtruck/(?P<pk>\d+)/$', FoodtruckDetailView.as_view(), name='foodtruck_detail_view'),
    url(r'^foodtruck/(?P<pk>\d+)/update/$', FoodtruckUpdateView.as_view(), name='foodtruck_update_view'),
    url(r'^food/update/(?P<pk>\d+)/$', FoodUpdateView.as_view(), name='food_update_view'),
    url(r'^price/update/(?P<pk>\d+)/$', PriceUpdateView.as_view(), name='price_update_view'),
    url(r'^new_location/(?P<pk>\d+)/$', LocationUpdateView.as_view(), name='location_update_view'),
    url(r'^checkin/(?P<pk>\d+)/$', CheckinUpdateView.as_view(), name='checkin_update_view'),
    url(r'^new_commenter/$', CommenterCreateView.as_view(), name='commenter_create_view'),
    url(r'^foodtruck/(?P<pk>\d+)/comment/$', CommentCreateView.as_view(), name='comment_create_view'),
    url(r'^(?P<pk>\d+)/update/comment/$', CommentUpdateView.as_view(), name='comment_update_view'),
    url(r'^api/foodtrucks/$', FoodtruckListCreateAPIView.as_view(), name='foodtruck_list_create_api_view'),
    url(r'^api/foodtrucks/(?P<pk>\d+)/$', FoodtruckDetailUpdateDestroyAPIView.as_view(), name='foodtruck_detail_update_api_view'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
