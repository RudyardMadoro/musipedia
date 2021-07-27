from django.urls import path
from . import views

urlpatterns = [
    path('', views.apiOverview, name="api-overview"),
    path('list-albums', views.albumList, name="album-list"),
    path('create-album', views.albumCreate, name="album-create"),
    path('show-album/<str:pk>/', views.albumDetail, name="album-show"),
    path('update-album/<str:pk>/', views.albumUpdate, name="album-update"),
    path('delete-album/<str:pk>/', views.albumDelete, name="album-delete"),


]