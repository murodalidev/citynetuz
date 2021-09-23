from rest_framework.response import Response
from rest_framework import status, generics

from ...models import News, Partner, Object
from .serializers import NewsSerializer, PartnerSerializer, ObjectSerializer


class NewsAllListView(generics.ListAPIView):
    queryset = News.objects.filter(is_active=True)[::-1]
    serializer_class = NewsSerializer


class NewsLatestListView(generics.ListAPIView):
    queryset = News.objects.filter(is_active=True)[::-1][:3]
    serializer_class = NewsSerializer


class PartnerListView(generics.ListAPIView):
    queryset = Partner.objects.filter(is_active=True)[::-1]
    serializer_class = PartnerSerializer


class ObjectListView(generics.ListAPIView):
    queryset = Object.objects.filter(is_active=True)[::-1]
    serializer_class = ObjectSerializer