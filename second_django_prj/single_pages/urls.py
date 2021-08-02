from django.urls import path
from . import views

urlpatterns = [
    path('news/', views.news),
    path('announcement/', views.ann),
    path('', views.landing),
    path('b/', views.geomap),
    path('a/', views.algo),
]
