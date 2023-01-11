from rest_framework import serializers
from .models import Image


class ImageSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    image = serializers.ImageField()

    geolocation = serializers.CharField(default=None)
    date = serializers.DateField(default=None)
    name = serializers.CharField(default=None)

    def create(self, data):
        return Image.objects.create(**data)
