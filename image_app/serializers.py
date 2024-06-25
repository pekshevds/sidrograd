from rest_framework import serializers


class ImageSerializer(serializers.Serializer):
    url = serializers.ImageField(use_url=True, source="image")


class CarouselImageSerializer(serializers.Serializer):
   image = ImageSerializer(required=False, allow_null=True)


class CarouselSerializer(serializers.Serializer):
    id = serializers.UUIDField()
    name = serializers.CharField(max_length=150)
    image = CarouselImageSerializer()
