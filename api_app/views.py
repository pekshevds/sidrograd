from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator
from django.db.models import Q
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, authentication
from auth_app.models import User
from catalog_app.models import (
    Category,
    Good
)
from order_app.models import (
    Contract,
    Order
)
from auth_app.serializers import UserSerializer
from catalog_app.serializers import (
    CategorySerializer,
    GoodSerializer
)
from order_app.serializers import (
    ContractSerializer,
    OrderSerializer
)
from wish_list_app.serializers import WishListSerializer

from wish_list_app.services import (
    fetch_users_wish_list,
    add_to_wish_list,
    delete_from_wish_list,
    clear_wish_list
)
from catalog_app.services.good import handle_good_list


class UserView(APIView):
    authentication_classes = [authentication.BasicAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        username = request.GET.get("username", "")
        if username:
            queryset = User.objects.filter(username=username)
            serializer = UserSerializer(queryset, many=True)
        else:
            queryset = User.objects.filter(is_superuser=False)
            serializer = UserSerializer(queryset, many=True)
        response = {"data": serializer.data}
        return Response(response)


class CategoryView(APIView):

    authentication_classes = [authentication.BasicAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        pk = request.GET.get("id", 0)
        if pk:
            queryset = Category.objects.filter(id=id)
            serializer = CategorySerializer(queryset, many=True)
        else:
            queryset = Category.objects.all()
            serializer = CategorySerializer(queryset, many=True)
        response = {"data": serializer.data}
        return Response(response)


class GoodView(APIView):

    authentication_classes = [authentication.BasicAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        pk = request.GET.get("id", 0)
        if pk:
            queryset = Good.objects.filter(id=id)
            serializer = GoodSerializer(queryset, many=True)
        else:
            page_number = request.GET.get("page", 1)
            count = request.GET.get("count", 25)
            filter = request.GET.get("filter")
            if filter:
                queryset = Good.objects.filter(
                    Q(name__icontains=filter) |
                    Q(art__icontains=filter)
                    )
            else:
                queryset = Good.objects.all()
            paginator = Paginator(queryset, count)
            serializer = GoodSerializer(
                paginator.get_page(page_number), many=True
            )
        response = {"data": serializer.data}
        return Response(response)

    def post(self, request):
        response = {"data": []}
        data = request.data.get("data", None)
        if not data:
            return Response(response)
        serializer = GoodSerializer(data=data, many=True)
        if serializer.is_valid(raise_exception=True):
            queryset = handle_good_list(good_list=data)
            serializer = GoodSerializer(queryset, many=True)
            response["data"] = serializer.data
        return Response(response)


class ContractView(APIView):
    authentication_classes = [authentication.BasicAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        client = request.user.client
        queryset = Contract.objects.filter(client=client)
        serializer = ContractSerializer(queryset, many=True)
        response = {"data": serializer.data}
        return Response(response)


class OrderView(APIView):
    authentication_classes = [authentication.BasicAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        client = request.user.client
        queryset = Order.objects.filter(client=client)
        serializer = OrderSerializer(queryset, many=True)
        response = {"data": serializer.data}
        return Response(response)


class WishListView(APIView):
    authentication_classes = [authentication.BasicAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        queryset = fetch_users_wish_list(request.user)
        serializer = WishListSerializer(queryset, many=True)
        response = {"data": serializer.data}
        return Response(response)


class WishListAddView(APIView):
    authentication_classes = [authentication.BasicAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        good = get_object_or_404(Good, id=request.GET.get("id", 0))
        add_to_wish_list(user=request.user, good=good)

        queryset = fetch_users_wish_list(request.user)
        serializer = WishListSerializer(queryset, many=True)
        response = {"data": serializer.data}
        return Response(response)


class WishListDeleteView(APIView):
    authentication_classes = [authentication.BasicAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        good = get_object_or_404(Good, id=request.GET.get("id", 0))
        delete_from_wish_list(user=request.user, good=good)

        queryset = fetch_users_wish_list(request.user)
        serializer = WishListSerializer(queryset, many=True)
        response = {"data": serializer.data}
        return Response(response)


class WishListClearView(APIView):
    authentication_classes = [authentication.BasicAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        clear_wish_list(user=request.user)

        queryset = fetch_users_wish_list(request.user)
        serializer = WishListSerializer(queryset, many=True)
        response = {"data": serializer.data}
        return Response(response)
