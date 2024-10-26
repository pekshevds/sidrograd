from rest_framework import serializers
from image_app.serializers import ImageSerializer


class CountrySerializer(serializers.Serializer):
    id = serializers.UUIDField()
    name = serializers.CharField(max_length=150)
    code = serializers.CharField(max_length=3, required=False, allow_blank=True)
    count = serializers.IntegerField(required=False, allow_null=True)


class CategorySerializer(serializers.Serializer):
    id = serializers.UUIDField()
    name = serializers.CharField(max_length=150)
    # image = ImageSerializer(required=False, allow_null=True)
    image = serializers.ImageField(required=False, allow_null=True, use_url=True)
    count = serializers.IntegerField(required=False, allow_null=True)


class ObjectFilterSerializer(serializers.Serializer):
    id = serializers.UUIDField()
    name = serializers.CharField(max_length=150)
    count = serializers.IntegerField(required=False, allow_null=True)


class TradeMarkSerializer(serializers.Serializer):
    id = serializers.UUIDField()
    name = serializers.CharField(max_length=150)
    count = serializers.IntegerField(required=False, allow_null=True)
    tags = serializers.CharField(max_length=256, required=False, allow_null=True)


"""class PasteurizationSerializer(serializers.Serializer):
    id = serializers.UUIDField()
    name = serializers.CharField(max_length=150)"""


class FilteringSerializer(serializers.Serializer):
    id = serializers.UUIDField()
    name = serializers.CharField(max_length=150)
    count = serializers.IntegerField(required=False, allow_null=True)


class GassingSerializer(serializers.Serializer):
    id = serializers.UUIDField()
    name = serializers.CharField(max_length=150)
    count = serializers.IntegerField(required=False, allow_null=True)


class ManufacturerSerializer(serializers.Serializer):
    id = serializers.UUIDField()
    name = serializers.CharField(max_length=150)
    description = serializers.CharField(required=False, allow_blank=True)
    count = serializers.IntegerField(required=False, allow_null=True)


class UnitSerializer(serializers.Serializer):
    id = serializers.UUIDField()
    name = serializers.CharField(max_length=150)
    count = serializers.IntegerField(required=False, allow_null=True)


class TypeOfFermentationSerializer(serializers.Serializer):
    id = serializers.UUIDField()
    name = serializers.CharField(max_length=150)
    count = serializers.IntegerField(required=False, allow_null=True)


class StyleSerializer(serializers.Serializer):
    id = serializers.UUIDField()
    name = serializers.CharField(max_length=150)
    count = serializers.IntegerField(required=False, allow_null=True)


class VolumeSerializer(serializers.Serializer):
    id = serializers.UUIDField()
    name = serializers.CharField(max_length=150)
    value = serializers.DecimalField(
        max_digits=15, decimal_places=3, required=False, allow_null=True
    )
    count = serializers.IntegerField(required=False, allow_null=True)


class StrengthSerializer(serializers.Serializer):
    id = serializers.UUIDField()
    name = serializers.CharField(max_length=150)
    value = serializers.DecimalField(
        max_digits=15, decimal_places=3, required=False, allow_null=True
    )
    count = serializers.IntegerField(required=False, allow_null=True)


class GoodsImageSerializer(serializers.Serializer):
    image = ImageSerializer(required=False, allow_null=True)


class GoodSerializer(serializers.Serializer):
    id = serializers.UUIDField()
    name = serializers.CharField(max_length=150)
    full_name = serializers.CharField(max_length=1024, required=False)
    art = serializers.CharField(max_length=25, required=False, allow_blank=True)
    tags = serializers.CharField(max_length=256, required=False, allow_null=True)
    balance = serializers.DecimalField(max_digits=15, decimal_places=3, required=False)
    price = serializers.DecimalField(max_digits=15, decimal_places=2, required=False)
    price_by_liter = serializers.DecimalField(
        max_digits=15, decimal_places=2, required=False
    )
    show_price_by_liter = serializers.BooleanField(required=False)
    in_package = serializers.DecimalField(
        max_digits=15, decimal_places=0, required=False
    )
    expiration_date = serializers.DecimalField(
        max_digits=15, decimal_places=0, required=False
    )
    category = CategorySerializer(required=False, allow_null=True)
    trade_mark = TradeMarkSerializer(required=False, allow_null=True)
    gassing = GassingSerializer(required=False, allow_null=True)
    # pasteurization = PasteurizationSerializer(required=False, allow_null=True)
    filtering = FilteringSerializer(required=False, allow_null=True)
    manufacturer = ManufacturerSerializer(required=False, allow_null=True)
    unit = UnitSerializer(required=False, allow_null=True)
    style = StyleSerializer(required=False, allow_null=True)
    type_of_fermentation = TypeOfFermentationSerializer(required=False, allow_null=True)
    volume = VolumeSerializer(required=False, allow_null=True)
    strength = StrengthSerializer(required=False, allow_null=True)
    country = CountrySerializer(required=False, allow_null=True)
    description = serializers.CharField(required=False, allow_blank=True)
    preview = ImageSerializer(
        required=False, allow_null=True, source="image", read_only=True
    )
    images = GoodsImageSerializer(
        required=False, allow_null=True, many=True, read_only=True
    )


class SimpleGoodSerializer(serializers.Serializer):
    id = serializers.UUIDField()
    name = serializers.CharField(max_length=150)
    full_name = serializers.CharField(max_length=1024, required=False)
    art = serializers.CharField(max_length=25, required=False, allow_blank=True)
    tags = serializers.CharField(max_length=256, required=False, allow_null=True)
    balance = serializers.DecimalField(max_digits=15, decimal_places=3, required=False)
    price = serializers.DecimalField(max_digits=15, decimal_places=2, required=False)
    price_by_liter = serializers.DecimalField(
        max_digits=15, decimal_places=2, required=False
    )
    show_price_by_liter = serializers.BooleanField(required=False)
    in_package = serializers.DecimalField(
        max_digits=15, decimal_places=0, required=False
    )
    expiration_date = serializers.DecimalField(
        max_digits=15, decimal_places=0, required=False
    )
    category_id = serializers.UUIDField(required=False, allow_null=True)
    trade_mark_id = serializers.UUIDField(required=False, allow_null=True)
    gassing_id = serializers.UUIDField(required=False, allow_null=True)
    # pasteurization_id = serializers.UUIDField(required=False, allow_null=True)
    filtering_id = serializers.UUIDField(required=False, allow_null=True)
    manufacturer_id = serializers.UUIDField(required=False, allow_null=True)
    unit_id = serializers.UUIDField(required=False, allow_null=True)
    style_id = serializers.UUIDField(required=False, allow_null=True)
    type_of_fermentationt_id = serializers.UUIDField(required=False, allow_null=True)
    volume_id = serializers.UUIDField(required=False, allow_null=True)
    strength_id = serializers.UUIDField(required=False, allow_null=True)
    country_id = serializers.UUIDField(required=False, allow_null=True)
    description = serializers.CharField(required=False, allow_blank=True)
    preview = ImageSerializer(
        required=False, allow_null=True, source="image", read_only=True
    )
    images = GoodsImageSerializer(
        required=False, allow_null=True, many=True, read_only=True
    )
