from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.data_home, name="data_home"),
]