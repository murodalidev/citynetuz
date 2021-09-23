from django.urls import path
from .views import CategoryListView, ProductListView, RequestCreateView, LastCameraListView, LastPhoneListView, \
    NewProductListView, PopularProductListView

urlpatterns = [
    path('category/', CategoryListView.as_view(), name='device-category'),
    path('product/', ProductListView.as_view(), name='device-product'),
    path('product/popular/', PopularProductListView.as_view(), name='device-product-popular'),
    path('product/new/', NewProductListView.as_view(), name='device-product-new'),
    path('product/latest-camera/', LastCameraListView.as_view(), name='device-product-latest-camera'),
    path('product/latest-telephone/', LastPhoneListView.as_view(), name='device-product-latest-telephone'),
    path('request/', RequestCreateView.as_view(), name='device-request'),
]
