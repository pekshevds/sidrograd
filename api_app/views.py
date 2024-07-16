from django.http import HttpRequest
from rest_framework.views import APIView
from rest_framework import permissions, authentication
from rest_framework.response import Response
from api_app.serializers import CallBackSerializer
from api_app.services import process_call_back_data


class CallBackView(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request: HttpRequest) -> Response:
        serializer = CallBackSerializer(data=request.data)
        success = False
        if serializer.is_valid(raise_exception=True):
            process_call_back_data(serializer.data)
            success = True
        response = {"data": None, "count": 0, "success": success}
        return Response(response)
