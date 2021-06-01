from django.urls import path, include
from .views import index

urlpatterns = [
    path('', index, name='Index'),
    path('', include('django.contrib.auth.urls')),
]