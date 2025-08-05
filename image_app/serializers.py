from rest_framework import serializers


class ImageSerializer(serializers.Serializer):
    url = serializers.ImageField(use_url=True, source="image")


class CarouselSerializer(serializers.Serializer):
    id = serializers.UUIDField()
    name = serializers.CharField(max_length=150)
    link = serializers.CharField(max_length=512)
    image = serializers.ImageField(required=False, allow_null=True, use_url=True)
