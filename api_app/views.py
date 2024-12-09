import requests
from django.http import HttpRequest
from rest_framework.views import APIView
from rest_framework import permissions  # , authentication
from rest_framework.response import Response
from api_app.serializers import CallBackSerializer
from api_app.services import process_call_back_data


class CheckMarkView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request: HttpRequest) -> Response:
        response = {"data": None, "count": 0, "success": False}
        code = request.GET.get("code")
        if code:
            result = requests.get(
                f"https://mobile.api.crpt.ru/mobile/check?code={code}&codeType=datamatrix"
            ).json()
            response = {"data": result, "count": 1, "success": True}
        return Response(response)


class CallBackView(APIView):
    # authentication_classes = [authentication.TokenAuthentication]
    # permission_classes = [permissions.IsAuthenticated]
    permission_classes = [permissions.AllowAny]

    def post(self, request: HttpRequest) -> Response:
        serializer = CallBackSerializer(data=request.data)
        success = False
        if serializer.is_valid(raise_exception=True):
            process_call_back_data(serializer.data)
            success = True
        response = {"data": None, "count": 0, "success": success}
        return Response(response)
