from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="sports-home"),
    path('rugby/', views.rugby, name="sports-rugby"),
    path('cricket/', views.cricket, name="sports-cricket"),
    path('supercars/', views.supercars, name='sports-cars'),
]
