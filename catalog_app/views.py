from django.core.paginator import Paginator
from rest_framework import permissions, authentication
from rest_framework.views import APIView
from rest_framework.response import Response
from catalog_app.models import (
    Manufacturer,
    Unit,
    Filtering,
    Pasteurization,
    Gassing,
    TradeMark,
    Category,
    Good
)
from catalog_app.serializers import (
    ManufacturerSerializer,
    UnitSerializer,
    FilteringSerializer,
    PasteurizationSerializer,
    GassingSerializer,
    TradeMarkSerializer,
    CategorySerializer,
    GoodSerializer
)
from catalog_app.services.good import (
    handle_good_list,
    fetch_goods_queryset_by_name_or_article,
)

from catalog_app.services.category import category_by_id_list
from catalog_app.services.trade_mark import trade_mark_by_id_list
from catalog_app.services.good import fetch_goods_queryset_by_filters


class ManufacturerView(APIView):

    permission_classes = [permissions.AllowAny]

    def get(self, request):
        id = request.GET.get("id")
        if id:
            queryset = Manufacturer.objects.filter(id=id)
            serializer = ManufacturerSerializer(queryset, many=True)
        else:
            queryset = Manufacturer.objects.all()
            serializer = ManufacturerSerializer(queryset, many=True)
        response = {"data": serializer.data}
        return Response(response)


class UnitView(APIView):

    permission_classes = [permissions.AllowAny]

    def get(self, request):
        id = request.GET.get("id")
        if id:
            queryset = Unit.objects.filter(id=id)
            serializer = UnitSerializer(queryset, many=True)
        else:
            queryset = Unit.objects.all()
            serializer = UnitSerializer(queryset, many=True)
        response = {"data": serializer.data}
        return Response(response)


class FilteringView(APIView):

    permission_classes = [permissions.AllowAny]

    def get(self, request):
        id = request.GET.get("id")
        if id:
            queryset = Filtering.objects.filter(id=id)
            serializer = FilteringSerializer(queryset, many=True)
        else:
            queryset = Filtering.objects.all()
            serializer = FilteringSerializer(queryset, many=True)
        response = {"data": serializer.data}
        return Response(response)


class PasteurizationView(APIView):

    permission_classes = [permissions.AllowAny]

    def get(self, request):
        id = request.GET.get("id")
        if id:
            queryset = Pasteurization.objects.filter(id=id)
            serializer = PasteurizationSerializer(queryset, many=True)
        else:
            queryset = Pasteurization.objects.all()
            serializer = PasteurizationSerializer(queryset, many=True)
        response = {"data": serializer.data}
        return Response(response)


class GassingView(APIView):

    permission_classes = [permissions.AllowAny]

    def get(self, request):
        id = request.GET.get("id")
        if id:
            queryset = Gassing.objects.filter(id=id)
            serializer = GassingSerializer(queryset, many=True)
        else:
            queryset = Gassing.objects.all()
            serializer = GassingSerializer(queryset, many=True)
        response = {"data": serializer.data}
        return Response(response)


class TradeMarkView(APIView):

    permission_classes = [permissions.AllowAny]

    def get(self, request):
        id = request.GET.get("id", 0)
        if id:
            queryset = TradeMark.objects.filter(id=id)
            serializer = TradeMarkSerializer(queryset, many=True)
        else:
            queryset = TradeMark.objects.all()
            serializer = TradeMarkSerializer(queryset, many=True)
        response = {"data": serializer.data}
        return Response(response)


class CategoryView(APIView):

    permission_classes = [permissions.AllowAny]

    def get(self, request):
        id = request.GET.get("id", 0)
        if id:
            queryset = Category.objects.filter(id=id)
            serializer = CategorySerializer(queryset, many=True)
        else:
            queryset = Category.objects.all()
            serializer = CategorySerializer(queryset, many=True)
        response = {"data": serializer.data}
        return Response(response)


class GoodView(APIView):

    authentication_classes = [authentication.BasicAuthentication]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request):
        id = request.GET.get("id", 0)
        if id:
            queryset = Good.objects.filter(id=id)
            serializer = GoodSerializer(queryset, many=True)
        else:
            page_number = request.GET.get("page", 1)
            count = request.GET.get("count", 25)
            queryset = None

            search = request.GET.get("search")
            if search:
                queryset = fetch_goods_queryset_by_name_or_article(search)
            else:
                categories = None
                category_id = request.GET.get("category_id")
                if category_id:
                    categories = category_by_id_list(category_id.split(","))

                trade_marks = None
                trade_mark_id = request.GET.get("trade_mark_id")
                if trade_mark_id:
                    trade_marks = trade_mark_by_id_list(
                        trade_mark_id.split(",")
                    )
                queryset = fetch_goods_queryset_by_filters(
                    categories,
                    trade_marks
                )

            if queryset is None:
                queryset = Good.objects.all()

            paginator = Paginator(queryset, count)
            serializer = GoodSerializer(
                paginator.get_page(page_number), many=True
            )
        response = {
            "data": serializer.data,
            "count": len(queryset)
            }
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
