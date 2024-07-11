from rest_framework import serializers


class PointSerializer(serializers.Serializer):
    id = serializers.UUIDField()
    name = serializers.CharField(max_length=150)
    address = serializers.TimeField(required=False)


class ClientSerializer(serializers.Serializer):
    id = serializers.UUIDField()
    name = serializers.CharField(max_length=150)
    addresses = PointSerializer(many=True, required=False)
