from django.http import HttpRequest
from django.core.paginator import Paginator
from rest_framework import permissions, authentication
from rest_framework.views import APIView
from rest_framework.response import Response
from catalog_app.models import (
    Manufacturer,
    Unit,
    Filtering,
    # Pasteurization,
    Gassing,
    TradeMark,
    Category,
    Good,
    Volume,
    Strength,
    Style,
    TypeOfFermentation,
    Country
)
from catalog_app.serializers import (
    ManufacturerSerializer,
    UnitSerializer,
    FilteringSerializer,
    # PasteurizationSerializer,
    GassingSerializer,
    TradeMarkSerializer,
    CategorySerializer,
    GoodSerializer,
    VolumeSerializer,
    StrengthSerializer,
    # SimpleGoodSerializer,
    StyleSerializer,
    TypeOfFermentationSerializer,
    CountrySerializer
)
from catalog_app.services.good import (
    handle_good_list,
    fetch_goods_queryset_by_name_or_article,
    fetch_goods_queryset_by_filters,
    update_prices
)

from catalog_app.services.category import category_by_id_list
from catalog_app.services.trade_mark import trade_mark_by_id_list
from catalog_app.services.manufacturer import manufacturer_by_id_list
from catalog_app.services.filtering import filtering_by_id_list
from catalog_app.services.gassing import gassing_by_id_list
# from catalog_app.services.pasteurization import pasteurization_by_id_list
from catalog_app.services.unit import unit_by_id_list
from catalog_app.services.volume import volume_by_id_list
from catalog_app.services.strength import strength_by_id_list
from catalog_app.services.style import style_by_id_list
from catalog_app.services.country import country_by_id_list
from catalog_app.services.type_of_fermentation import (
    type_of_fermentation_by_id_list
)


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
            "success": True
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
            "success": True
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
            "success": True
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
            "success": True
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
            "success": True
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
            "success": True
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
            "success": True
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
            "success": True
            }
        return Response(response)


"""class PasteurizationView(APIView):

    permission_classes = [permissions.AllowAny]

    def get(self, request):
        id = request.GET.get("id")
        if id:
            queryset = Pasteurization.objects.filter(id=id)
            serializer = PasteurizationSerializer(queryset, many=True)
        else:
            queryset = Pasteurization.objects.all()
            serializer = PasteurizationSerializer(queryset, many=True)
        response = {
            "data": serializer.data,
            "params": request.GET
            }
        return Response(response)"""


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
            "success": True
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
            "success": True
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
            "success": True
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

                manufacturers = None
                manufacturer_id = request.GET.get("manufacturer_id")
                if manufacturer_id:
                    manufacturers = manufacturer_by_id_list(
                        manufacturer_id.split(",")
                    )

                filterings = None
                filtering_id = request.GET.get("filtering_id")
                if filtering_id:
                    filterings = filtering_by_id_list(
                        filtering_id.split(",")
                    )

                gassings = None
                gassing_id = request.GET.get("gassing_id")
                if gassing_id:
                    gassings = gassing_by_id_list(
                        gassing_id.split(",")
                    )

                """pasteurizations = None
                pasteurization_id = request.GET.get("pasteurization_id")
                if pasteurization_id:
                    pasteurizations = pasteurization_by_id_list(
                        pasteurization_id.split(",")
                    )"""

                units = None
                unit_id = request.GET.get("unit_id")
                if unit_id:
                    units = unit_by_id_list(
                        unit_id.split(",")
                    )

                styles = None
                style_id = request.GET.get("style_id")
                if style_id:
                    styles = style_by_id_list(
                        style_id.split(",")
                    )

                types_of_fermentation = None
                type_of_fermentation_id = \
                    request.GET.get("type_of_fermentation_id")
                if type_of_fermentation_id:
                    types_of_fermentation = type_of_fermentation_by_id_list(
                        type_of_fermentation_id.split(",")
                    )

                volumes = None
                volume_id = request.GET.get("volume_id")
                if volume_id:
                    volumes = volume_by_id_list(
                        volume_id.split(",")
                    )

                strengths = None
                strength_id = request.GET.get("strength_id")
                if strength_id:
                    strengths = strength_by_id_list(
                        strength_id.split(",")
                    )

                countryes = None
                country_id = request.GET.get("country_id")
                if country_id:
                    countryes = country_by_id_list(
                        country_id.split(",")
                    )

                queryset = fetch_goods_queryset_by_filters(
                    categories,
                    trade_marks,
                    manufacturers,
                    filterings,
                    gassings,
                    # pasteurizations,
                    units,
                    styles,
                    types_of_fermentation,
                    volumes,
                    strengths,
                    countryes
                )

            if queryset is None:
                queryset = Good.objects.all()

            paginator = Paginator(queryset, count)
            serializer = GoodSerializer(
                paginator.get_page(page_number), many=True
            )
        response = {
            "data": serializer.data,
            "count": len(queryset),
            "params": request.GET,
            "success": True
            }
        return Response(response)

    def post(self, request: HttpRequest) -> Response:
        response = {
            "data": [],
            "count": 0,
            "params": {},
            "success": True
            }
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

    permission_classes = [permissions.AllowAny]

    def get(self, request: HttpRequest) -> Response:
        category = CategorySerializer(
            Category.objects.all(), many=True
            )
        trade_mark = TradeMarkSerializer(
            TradeMark.objects.all(), many=True
            )
        gassing = GassingSerializer(
            Gassing.objects.all(),  many=True
            )
        """pasteurization = PasteurizationSerializer(
            Pasteurization.objects.all(), many=True
            )"""
        filtering = FilteringSerializer(
            Filtering.objects.all(), many=True
            )
        manufacturer = ManufacturerSerializer(
            Manufacturer.objects.all(), many=True
            )
        unit = UnitSerializer(
            Unit.objects.all(), many=True
            )
        style = StyleSerializer(
            Style.objects.all(), many=True
            )
        type_of_fermentation = TypeOfFermentationSerializer(
            TypeOfFermentation.objects.all(), many=True
            )
        strength = StrengthSerializer(
            Strength.objects.all(), many=True
            )
        volume = VolumeSerializer(
            Volume.objects.all(), many=True
            )
        country = CountrySerializer(
            Country.objects.all(), many=True
            )
        # countryes = [good.country for good in Good.objects.exclude(country=None)]
        response = {
            "data": {
                "category": category.data,
                "trade_mark": trade_mark.data,
                "gassing": gassing.data,
                # "pasteurization": pasteurization.data,
                "filtering": filtering.data,
                "manufacturer": manufacturer.data,
                "unit": unit.data,
                "style": style.data,
                "type_of_fermentation": type_of_fermentation.data,
                "strength": strength.data,
                "volume": volume.data,
                "country": country.data,
                # "good": good.data
            },
            "params": request.GET,
            "success": True
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
        return Response({"success": update_prices(data)})
