from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, authentication
from catalog_app.models import Good

from cart_app.serializers import CartSerializer
from cart_app.services import (
    fetch_users_cart,
    add_to_cart,
    delete_from_cart,
    clear_cart
)


class CartView(APIView):
    authentication_classes = [authentication.BasicAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        queryset = fetch_users_cart(request.user)
        serializer = CartSerializer(queryset, many=True)
        response = {"data": serializer.data}
        return Response(response)


class CartAddView(APIView):
    authentication_classes = [authentication.BasicAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        good = get_object_or_404(Good, id=request.GET.get("id", 0))
        add_to_cart(user=request.user, good=good)

        queryset = fetch_users_cart(request.user)
        serializer = CartSerializer(queryset, many=True)
        response = {"data": serializer.data}
        return Response(response)

    def post(self, request):
        response = {"data": []}
        data = request.data.get("data", None)
        if not data:
            return Response(response)

        good = get_object_or_404(Good, id=request.GET.get("id", 0))
        add_to_cart(user=request.user, good=good)

        queryset = fetch_users_cart(request.user)
        serializer = CartSerializer(queryset, many=True)
        response = {"data": serializer.data}
        return Response(response)


class CartDeleteView(APIView):
    authentication_classes = [authentication.BasicAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        good = get_object_or_404(Good, id=request.GET.get("id", 0))
        delete_from_cart(user=request.user, good=good)

        queryset = fetch_users_cart(request.user)
        serializer = CartSerializer(queryset, many=True)
        response = {"data": serializer.data}
        return Response(response)


class CartClearView(APIView):
    authentication_classes = [authentication.BasicAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        clear_cart(user=request.user)

        queryset = fetch_users_cart(request.user)
        serializer = CartSerializer(queryset, many=True)
        response = {"data": serializer.data}
        return Response(response)
