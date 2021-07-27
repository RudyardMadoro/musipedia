from django.urls import path
from . import views

urlpatterns = [
    path('', views.apiOverview, name="api-overview"),
    path('list', views.artistList, name="artisit-list"),
    path('create', views.artistCreate, name="artist-create"),
    path('show/<str:pk>/', views.artistDetail, name="artist-show"),
    path('update/<str:pk>/', views.artistUpdate, name="artist-update"),
    path('delete/<str:pk>/', views.artistDelete, name="artist-delete"),


]