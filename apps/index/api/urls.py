from django.urls import path, include

urlpatterns = [
    path('v1/', include('apps.index.api.v1.urls')),
]