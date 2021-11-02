from django.urls import path, include

urlpatterns = [
    path('v1/', include('apps.montage.api.v1.urls')),
]