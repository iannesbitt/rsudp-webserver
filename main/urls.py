from django.urls import path
from . import views

urlpatterns = [
    path('', views.img_list, name='img_list'),
]
