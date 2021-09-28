from django.db.models import Q
from rest_framework import generics

from ...models import Category, Product, Request
from .serializers import CategorySerializer, ProductSerializer, ContactSerializer


class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.filter(is_active=True).order_by('title')
    serializer_class = CategorySerializer


class ProductListView(generics.ListAPIView):
    queryset = Product.objects.filter(is_active=True).order_by('-id')
    serializer_class = ProductSerializer

    def get_queryset(self):
        qs = self.queryset.all()
        param = self.request.GET.get('search')
        cat = self.request.GET.get('category')

        param_condition = Q()
        if param:
            param_condition = Q(title__icontains=param)
        cat_condition = Q()
        if cat:
            cat_condition = Q(category=cat)

        qs = qs.filter(param_condition, cat_condition)
        return qs


class ProductDetailView(generics.RetrieveAPIView):
    queryset = Product.objects.filter(is_active=True)
    serializer_class = ProductSerializer


class NewProductListView(generics.ListAPIView):
    queryset = Product.objects.filter(is_active=True).order_by('-date_created')[:10]
    serializer_class = ProductSerializer


class PopularProductListView(generics.ListAPIView):
    queryset = Product.objects.filter(is_active=True, is_popular=True).order_by('-date_created')[:10]
    serializer_class = ProductSerializer


class LastCameraListView(generics.ListAPIView):
    queryset = Product.objects.filter(is_active=True, trend=3).order_by('-id')[:1]
    serializer_class = ProductSerializer


class LastPhoneListView(generics.ListAPIView):
    queryset = Product.objects.filter(is_active=True, trend=1).order_by('-id')[:1]
    serializer_class = ProductSerializer


class RequestCreateView(generics.CreateAPIView):
    queryset = Request.objects.all()
    serializer_class = ContactSerializer
