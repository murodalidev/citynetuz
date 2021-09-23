from django.urls import path, include

urlpatterns = [
    path('v1/', include('apps.design.api.v1.urls')),
]