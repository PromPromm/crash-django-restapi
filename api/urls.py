from django.urls import path
from . import views

urlpatterns = [
    path('', views.getmethod),
    path('add/', views.postmethod)
]
