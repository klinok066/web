from django.urls import path
from . import views


urlpatterns = [
    path(r'^$', views.index, name="home"),
    path('about', views.about, name="about"),
    path('form', views.form, name="form"),
    path('invalid_data', views.invalid_data, name="invalid_data"),
    path('success', views.success, name="success"),
    path('records', views.records, name="records"),
]

