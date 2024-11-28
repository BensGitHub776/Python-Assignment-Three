from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='my_app'),
    path('home', views.home, name='my_app'),
]
