from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, authentication
from order_app.models import (
    Contract,
    Order,
    ItemOrder
)
from order_app.serializers import (
    SimpleContractSerializer,
    ContractSerializer,
    SimpleOrderSerializer,
    OrderSerializer,
    ItemOrderSerializer,
    SimpleItemOrderSerializer
)


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
        serializer = SimpleOrderSerializer(queryset, many=True)
        response = {"data": serializer.data}
        return Response(response)


class OrderItemView(APIView):
    authentication_classes = [authentication.BasicAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        order = Order.objects.filter(
            id=request.GET.get("order_id", None)
        ).first()

        if order:
            queryset = ItemOrder.objects.filter(order=order)
        else:
            client = request.user.client
            queryset = ItemOrder.objects.filter(
                order__in=Order.objects.filter(client=client)
            )

        serializer = SimpleItemOrderSerializer(queryset, many=True)
        response = {"data": serializer.data}
        return Response(response)


class OrderItemAddView(APIView):
    authentication_classes = [authentication.BasicAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        response = {"data": []}
        data = request.data.get("data", None)
        if not data:
            return Response(response)

        """for item in data:
            order = Order.objects.filter("id", item.get("order_id", None)).first()
            if order:
                order.items.all().delete()
            else
                order = Order.objects.create(request.user.)
            for item_order in 
                good_id = item.get("good_id", None)
                quantity = item.get("quantity", 0)
                good = get_object_or_404(Good, id=good_id)

        serializer = ItemOrderSerializer(queryset, many=True)
        response = {"data": serializer.data}
        return Response(response)"""


class OrderItemDeleteView(APIView):
    authentication_classes = [authentication.BasicAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        item = get_object_or_404(ItemOrder, id=request.GET.get("id", None))
        order = item.order
        if item:
            item.delete()
        queryset = Order.objects.filter(order=order)
        serializer = ItemOrderSerializer(queryset, many=True)
        response = {"data": serializer.data}
        return Response(response)
