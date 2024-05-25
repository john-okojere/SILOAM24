from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="register"),
    path('card', views.cards, name="card"),
    path('success/<uuid:uid>/', views.success, name="card"),
]
