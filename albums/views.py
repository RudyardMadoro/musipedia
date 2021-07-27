from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import AlbumSerialier
from .models import Album



@api_view(['GET'])
def apiOverview(request):

    apiUrls = {
        'list': '/albums/list-albums',
        'create': '/albums/create-album',
        'edit':'/albums/edit-album/<str:pk>/',
        'details':'/albums/show-album/<str:pk>/',
        'delete':'/albums/delete-album/<str:pk>/'
    }

    return Response(apiUrls)

@api_view(['GET'])
def albumList(request):
    albums = Album.objects.all()
    serialier = AlbumSerialier(albums, many=True)
    return Response(serialier.data)

@api_view(['POST'])
def albumCreate(request):
    serializer = AlbumSerialier(data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def albumDetail(request, pk):
    albums = Album.objects.get(id = pk)
    serializer = AlbumSerialier(albums, many = False)
    return Response(serializer.data)

@api_view(['POST'])
def albumUpdate(request, pk):
    artist = Album.objects.get(id = pk)
    serializer = AlbumSerialier(instance= album, data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def albumDelete(request, pk):
    album = Album.objects.get(id = pk)
    album.delete();
    return Response("Deleted")

