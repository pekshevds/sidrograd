import logging
from django.http import HttpRequest
from django.core.paginator import Paginator
from rest_framework import permissions, authentication
from rest_framework.views import APIView
from rest_framework.response import Response
from catalog_app.models import (
    Manufacturer,
    Unit,
    Filtering,
    Gassing,
    TradeMark,
    Category,
    Good,
    Volume,
    Strength,
    Style,
    TypeOfFermentation,
    Country,
)
from catalog_app.serializers import (
    ManufacturerSerializer,
    UnitSerializer,
    FilteringSerializer,
    GassingSerializer,
    TradeMarkSerializer,
    CategorySerializer,
    GoodSerializer,
    VolumeSerializer,
    StrengthSerializer,
    StyleSerializer,
    TypeOfFermentationSerializer,
    CountrySerializer,
)
from catalog_app.services.good import (
    handle_good_list,
    fetch_goods_queryset_by_name_or_article,
    run_update_prices,
    handle_new_goods,
)
from catalog_app.services.token import user_by_token_exist
from image_app.models import Carousel
from image_app.serializers import CarouselSerializer
from catalog_app.commons import (
    fetch_goods_by_filters,
    fetch_filters,
    fetch_filters_by_goods,
    prepare_query_set,
)
# from catalog_app.services.update_count_in_filters import fetch_filters_by_goods

logger = logging.getLogger(__name__)


class CountryView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request: HttpRequest) -> Response:
        id = request.GET.get("id")
        if id:
            queryset = Country.objects.filter(id=id)
            serializer = CountrySerializer(queryset, many=True)
        else:
            queryset = Country.objects.all()
            serializer = CountrySerializer(queryset, many=True)
        response = {
            "data": serializer.data,
            "count": len(queryset),
            "params": request.GET,
            "success": True,
        }
        return Response(response)


class StyleView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request: HttpRequest) -> Response:
        id = request.GET.get("id")
        if id:
            queryset = Style.objects.filter(id=id)
            serializer = StyleSerializer(queryset, many=True)
        else:
            queryset = Style.objects.all()
            serializer = StyleSerializer(queryset, many=True)
        response = {
            "data": serializer.data,
            "count": len(queryset),
            "params": request.GET,
            "success": True,
        }
        return Response(response)


class TypeOfFermentationView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request: HttpRequest) -> Response:
        id = request.GET.get("id")
        if id:
            queryset = TypeOfFermentation.objects.filter(id=id)
            serializer = TypeOfFermentationSerializer(queryset, many=True)
        else:
            queryset = TypeOfFermentation.objects.all()
            serializer = TypeOfFermentationSerializer(queryset, many=True)
        response = {
            "data": serializer.data,
            "count": len(queryset),
            "params": request.GET,
            "success": True,
        }
        return Response(response)


class StrengthView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request: HttpRequest) -> Response:
        id = request.GET.get("id")
        if id:
            queryset = Strength.objects.filter(id=id)
            serializer = StrengthSerializer(queryset, many=True)
        else:
            queryset = Strength.objects.all()
            serializer = StrengthSerializer(queryset, many=True)
        response = {
            "data": serializer.data,
            "count": len(queryset),
            "params": request.GET,
            "success": True,
        }
        return Response(response)


class VolumeView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request: HttpRequest) -> Response:
        id = request.GET.get("id")
        if id:
            queryset = Volume.objects.filter(id=id)
            serializer = VolumeSerializer(queryset, many=True)
        else:
            queryset = Volume.objects.all()
            serializer = VolumeSerializer(queryset, many=True)
        response = {
            "data": serializer.data,
            "count": len(queryset),
            "params": request.GET,
            "success": True,
        }
        return Response(response)


class ManufacturerView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request: HttpRequest) -> Response:
        id = request.GET.get("id")
        if id:
            queryset = Manufacturer.objects.filter(id=id)
            serializer = ManufacturerSerializer(queryset, many=True)
        else:
            queryset = Manufacturer.objects.all()
            serializer = ManufacturerSerializer(queryset, many=True)
        response = {
            "data": serializer.data,
            "count": len(queryset),
            "params": request.GET,
            "success": True,
        }
        return Response(response)


class UnitView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request: HttpRequest) -> Response:
        id = request.GET.get("id")
        if id:
            queryset = Unit.objects.filter(id=id)
            serializer = UnitSerializer(queryset, many=True)
        else:
            queryset = Unit.objects.all()
            serializer = UnitSerializer(queryset, many=True)
        response = {
            "data": serializer.data,
            "count": len(queryset),
            "params": request.GET,
            "success": True,
        }
        return Response(response)


class FilteringView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request: HttpRequest) -> Response:
        id = request.GET.get("id")
        if id:
            queryset = Filtering.objects.filter(id=id)
            serializer = FilteringSerializer(queryset, many=True)
        else:
            queryset = Filtering.objects.all()
            serializer = FilteringSerializer(queryset, many=True)
        response = {
            "data": serializer.data,
            "count": len(queryset),
            "params": request.GET,
            "success": True,
        }
        return Response(response)


class GassingView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request: HttpRequest) -> Response:
        id = request.GET.get("id")
        if id:
            queryset = Gassing.objects.filter(id=id)
            serializer = GassingSerializer(queryset, many=True)
        else:
            queryset = Gassing.objects.all()
            serializer = GassingSerializer(queryset, many=True)
        response = {
            "data": serializer.data,
            "count": len(queryset),
            "params": request.GET,
            "success": True,
        }
        return Response(response)


class TradeMarkView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request: HttpRequest) -> Response:
        id = request.GET.get("id", 0)
        if id:
            queryset = TradeMark.objects.filter(id=id)
            serializer = TradeMarkSerializer(queryset, many=True)
        else:
            queryset = TradeMark.objects.all()
            serializer = TradeMarkSerializer(queryset, many=True)
        response = {
            "data": serializer.data,
            "count": len(queryset),
            "params": request.GET,
            "success": True,
        }
        return Response(response)


class CategoryView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request: HttpRequest) -> Response:
        id = request.GET.get("id", 0)
        if id:
            queryset = Category.objects.filter(id=id)
            serializer = CategorySerializer(queryset, many=True)
        else:
            queryset = Category.objects.all()
            serializer = CategorySerializer(queryset, many=True)
        response = {
            "data": serializer.data,
            "count": len(queryset),
            "params": request.GET,
            "success": True,
        }
        return Response(response)


class GoodView(APIView):
    authentication_classes = [authentication.BasicAuthentication]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request: HttpRequest) -> Response:
        id = request.GET.get("id", 0)
        if id:
            queryset = Good.objects.filter(id=id)
            serializer = GoodSerializer(queryset, many=True)
        else:
            page_number = request.GET.get("page", 1)
            count = request.GET.get("count", 25)
            queryset = None
            only_active = not user_by_token_exist(request)

            logger.info({"only_active": only_active, "headers": request.headers})

            search = request.GET.get("search")
            if search:
                queryset = fetch_goods_queryset_by_name_or_article(search, only_active)
            else:
                filters = fetch_filters(request=request)
                queryset = fetch_goods_by_filters(filters, only_active)
            if queryset is None:
                if only_active:
                    queryset = Good.active_goods.all()
                else:
                    queryset = Good.objects.all()
            paginator = Paginator(queryset, count)
            serializer = GoodSerializer(paginator.get_page(page_number), many=True)
        response = {
            "data": serializer.data,
            "count": len(queryset),
            "params": request.GET,
            "success": True,
        }
        return Response(response)

    def post(self, request: HttpRequest) -> Response:
        response = {"data": [], "count": 0, "params": {}, "success": True}
        data = request.data.get("data", None)
        if not data:
            return Response(response)
        serializer = GoodSerializer(data=data, many=True)
        if serializer.is_valid(raise_exception=True):
            queryset = handle_good_list(good_list=data)
            serializer = GoodSerializer(queryset, many=True)
            response["data"] = serializer.data
            response["count"] = len(queryset)
        return Response(response)


class DataView(APIView):
    authentication_classes = [authentication.BasicAuthentication]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request: HttpRequest) -> Response:
        # Вернуть, если нужно уменьшать количество фильтров
        queryset = None
        search = request.GET.get("search")
        only_active = not user_by_token_exist(request)
        if search:
            queryset = fetch_goods_queryset_by_name_or_article(search, only_active)
        else:
            filters = fetch_filters(request)
            if any(filters):
                queryset = fetch_goods_by_filters(filters, only_active)
        if queryset is None:
            if only_active:
                queryset = Good.active_goods.all()
            else:
                queryset = Good.objects.all()
        prepared_data = fetch_filters_by_goods(queryset)
        # filters = fetch_filters_by_goods()

        category = CategorySerializer(Category.objects.all(), many=True)
        trade_mark = TradeMarkSerializer(
            prepare_query_set(prepared_data.trade_mark), many=True
        )
        gassing = GassingSerializer(prepare_query_set(prepared_data.gassing), many=True)
        filtering = FilteringSerializer(
            prepare_query_set(prepared_data.filtering), many=True
        )
        manufacturer = ManufacturerSerializer(
            prepare_query_set(prepared_data.manufacturer), many=True
        )
        unit = UnitSerializer(prepare_query_set(prepared_data.unit), many=True)
        style = StyleSerializer(prepare_query_set(prepared_data.style), many=True)
        type_of_fermentation = TypeOfFermentationSerializer(
            prepare_query_set(prepared_data.type_of_fermentation), many=True
        )
        strength = StrengthSerializer(
            prepare_query_set(prepared_data.strength), many=True
        )
        volume = VolumeSerializer(prepare_query_set(prepared_data.volume), many=True)
        country = CountrySerializer(prepare_query_set(prepared_data.country), many=True)

        response = {
            "data": {
                "category": category.data,
                "trade_mark": trade_mark.data,
                "gassing": gassing.data,
                "filtering": filtering.data,
                "manufacturer": manufacturer.data,
                "unit": unit.data,
                "style": style.data,
                "type_of_fermentation": type_of_fermentation.data,
                "strength": strength.data,
                "volume": volume.data,
                "country": country.data,
                "more_than_zero": False
                if request.GET.get("more_than_zero") is None
                else True,
            },
            "params": request.GET,
            "success": True,
        }
        return Response(response)


class СarouselView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request: HttpRequest) -> Response:
        сarousel = CarouselSerializer(Carousel.objects.all(), many=True)
        response = {
            "data": сarousel.data,
            "count": len(сarousel.data),
            "params": request.GET,
            "success": True,
        }
        return Response(response)


class PricesView(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request: HttpRequest) -> Response:
        response = {"success": True}
        data = request.data.get("data", None)
        if not data:
            return Response(response)
        return Response({"success": run_update_prices(data)})


class LoadGoodsView(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request: HttpRequest) -> Response:
        response = {"data": [], "count": 0, "success": False}
        data = request.data.get("data")
        if not data:
            return Response(response)
        handle_new_goods(data)
        response["success"] = True
        return Response(response)
