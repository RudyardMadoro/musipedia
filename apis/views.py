from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import ArtistSerialier
from .models import Artist



@api_view(['GET'])
def apiOverview(request):

    apiUrls = {
        'list': '/apis/list',
        'create': '/apis/create',
        'edit':'/apis/edit/<str:pk>/',
        'details':'/apis/show/<str:pk>/',
        'delete':'/apis/delete/<str:pk>/'
    }

    return Response(apiUrls)

@api_view(['GET'])
def artistList(request):
    artists = Artist.objects.all()
    serialier = ArtistSerialier(artists, many=True)
    return Response(serialier.data)

@api_view(['POST'])
def artistCreate(request):
    serializer = ArtistSerialier(data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def artistDetail(request, pk):
    artist = Artist.objects.get(id = pk)
    serializer = ArtistSerialier(artist, many = False)
    return Response(serializer.data)

@api_view(['POST'])
def artistUpdate(request, pk):
    artist = Artist.objects.get(id = pk)
    serializer = ArtistSerialier(instance= artist, data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def artistDelete(request, pk):
    artist = Artist.objects.get(id = pk)
    artist.delete();
    return Response("Deleted")

