from django.urls import path
from . import views

urlpatterns = [
    path('', views.apiOverview, name="api-overview"),
    path('list-songs', views.songList, name="songs-list"),
    path('create-song', views.songCreate, name="song-create"),
    path('show-song/<str:pk>/', views.songDetail, name="song-show"),
    path('update-song/<str:pk>/', views.songUpdate, name="song-update"),
    path('delete-song/<str:pk>/', views.songDelete, name="song-delete")


]