from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import SongSerialier
from .models import Song



@api_view(['GET'])
def apiOverview(request):

    songsUrls = {
        'list': '/songs/list',
        'create': '/songs/create',
        'edit':'/songs/edit/<str:pk>/',
        'details':'/songs/show/<str:pk>/',
        'delete':'/songs/delete/<str:pk>/'
    }

    return Response(songsUrls)

@api_view(['GET'])
def songList(request):
    songs = Song.objects.all()
    serialier = SongSerialier(songs, many=True)
    return Response(serialier.data)

@api_view(['POST'])
def songCreate(request):
    serializer = SongSerialier(data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def songDetail(request, pk):
    song = Song.objects.get(id = pk)
    serializer = SongSerialier(song, many = False)
    return Response(serializer.data)

@api_view(['POST'])
def songUpdate(request, pk):
    song = Song.objects.get(id = pk)
    serializer = SongSerialier(instance= song, data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def songDelete(request, pk):
    song = Song.objects.get(id = pk)
    song.delete();
    return Response("Deleted")

