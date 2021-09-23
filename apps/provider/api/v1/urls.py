from django.urls import path
from .views import NotificationListView, InternetTariffListView, TelephonyTariffListView, PopularServiceListView, \
    TypeChannelListView, ChannelListView, CityAreaListView, DistrictAreaListView, StreetAreaListView, HomeAreaListView \
    , RequestCreateView

urlpatterns = [
    path('notifications/', NotificationListView.as_view(), name='notification'),
    path('internet/tariffs/', InternetTariffListView.as_view(), name='internet-tariff'),
    path('telephony/tariffs/', TelephonyTariffListView.as_view(), name='telephony-tariff'),
    path('popular-services/', PopularServiceListView.as_view(), name='popular-service'),
    path('channels/all/', TypeChannelListView.as_view(), name='all-channels'),
    path('channels/popular/', ChannelListView.as_view(), name='popular-channel'),
    path('city-list/', CityAreaListView.as_view(), name='city-list'),
    path('district-list/', DistrictAreaListView.as_view(), name='district-list'),
    path('street-list/', StreetAreaListView.as_view(), name='street-list'),
    path('home-list/', HomeAreaListView.as_view(), name='home-list'),
    path('request/', RequestCreateView.as_view(), name='internet-request'),
]
