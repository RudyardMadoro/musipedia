from rest_framework  import serializers
from .models import Album

class AlbumSerialier(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = '__all__'