from django.urls import path
from .views import NewsAllListView, NewsLatestListView, NewsDetailView, ObjectListView, PartnerListView

urlpatterns = [
    path('news-list/', NewsAllListView.as_view(), name='news-list'),
    path('news-list/latest/', NewsLatestListView.as_view(), name='news-list-latest'),
    path('news-list/<int:pk>/', NewsDetailView.as_view(), name='news-detail'),
    path('objects/', ObjectListView.as_view(), name='objects'),
    path('partners/', PartnerListView.as_view(), name='partners'),
]
