from rest_framework import generics
from rest_framework.response import Response

from apps.device.api.v1.serializers import ProductSerializer
from apps.device.models import Product
from apps.index.api.v1.serializers import NewsSerializer
from apps.index.models import News
from ...models import (
    Notification,
    InternetTariff,
    CityArea,
    DistrictArea,
    StreetArea,
    HomeArea,
    Request,
    TypeChannel,
    Channel,
    TelephonyTariff
)
from .serializers import (
    NotificationSerializer,
    InternetTariffSerializer,
    TelephonyTariffSerializer,
    ChannelSerializer,
    TypeChannelSerializer,
    CityAreaSerializer,
    DistrictAreaSerializer,
    StreetAreaSerializer,
    HomeAreaSerializer,
    RequestSerializer,
)


class NotificationListView(generics.ListAPIView):
    queryset = Notification.objects.filter(is_active=True).order_by('-id')[:1]
    serializer_class = NotificationSerializer


class InternetTariffListView(generics.ListAPIView):
    queryset = InternetTariff.objects.filter(is_active=True)
    serializer_class = InternetTariffSerializer


class TelephonyTariffListView(generics.ListAPIView):
    queryset = TelephonyTariff.objects.filter(is_active=True)
    serializer_class = TelephonyTariffSerializer


class PopularServiceListView(generics.ListAPIView):
    queryset = News.objects.filter(is_active=True, trend__lte=2).order_by('-id')
    serializer_class = NewsSerializer


class TypeChannelListView(generics.ListAPIView):
    queryset = TypeChannel.objects.filter(is_active=True)
    serializer_class = TypeChannelSerializer


class ChannelListView(generics.ListAPIView):
    queryset = Channel.objects.filter(is_active=True, is_popular=True)
    serializer_class = ChannelSerializer


class CityAreaListView(generics.ListAPIView):
    queryset = CityArea.objects.filter(is_active=True).order_by('title')
    serializer_class = CityAreaSerializer


class DistrictAreaListView(generics.ListAPIView):
    queryset = DistrictArea.objects.filter(is_active=True).order_by('title')
    serializer_class = DistrictAreaSerializer

    def get_queryset(self):
        param = self.request.GET.get('city')
        queryset = self.queryset.all()
        if param:
            queryset = queryset.filter(city=param)
        return queryset


class StreetAreaListView(generics.ListAPIView):
    queryset = StreetArea.objects.filter(is_active=True).order_by('title')
    serializer_class = StreetAreaSerializer

    def get_queryset(self):
        param = self.request.GET.get('district')
        queryset = self.queryset.all()
        if param:
            queryset = queryset.filter(district=param)
        return queryset


class HomeAreaListView(generics.ListAPIView):
    queryset = HomeArea.objects.filter(is_active=True).order_by('title')
    serializer_class = HomeAreaSerializer

    def get_queryset(self):
        param = self.request.GET.get('street')
        queryset = self.queryset.all()
        if param:
            queryset = queryset.filter(street=param)
        return queryset


class RequestCreateView(generics.CreateAPIView):
    queryset = Request.objects.all()
    serializer_class = RequestSerializer
