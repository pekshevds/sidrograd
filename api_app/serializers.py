from rest_framework import serializers


class CallBackSerializer(serializers.Serializer):
    subject = serializers.CharField(required=True)
    tel = serializers.CharField(required=True)
    link = serializers.CharField(required=False)
