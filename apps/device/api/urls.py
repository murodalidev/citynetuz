from django.urls import path, include

urlpatterns = [
    path('v1/', include('apps.device.api.v1.urls')),
]