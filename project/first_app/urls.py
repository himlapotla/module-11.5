from . import views
from django.urls import path

urlpatterns = [
    path('mealsss/', views.index),
]
