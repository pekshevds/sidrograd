from rest_framework import serializers


class CategorySerializer(serializers.Serializer):
    id = serializers.UUIDField()
    name = serializers.CharField(max_length=150)


class TradeMarkSerializer(serializers.Serializer):
    id = serializers.UUIDField()
    name = serializers.CharField(max_length=150)


class PasteurizationSerializer(serializers.Serializer):
    id = serializers.UUIDField()
    name = serializers.CharField(max_length=150)


class FilteringSerializer(serializers.Serializer):
    id = serializers.UUIDField()
    name = serializers.CharField(max_length=150)


class GassingSerializer(serializers.Serializer):
    id = serializers.UUIDField()
    name = serializers.CharField(max_length=150)


class ManufacturerSerializer(serializers.Serializer):
    id = serializers.UUIDField()
    name = serializers.CharField(max_length=150)


class UnitSerializer(serializers.Serializer):
    id = serializers.UUIDField()
    name = serializers.CharField(max_length=150)


class GoodSerializer(serializers.Serializer):
    id = serializers.UUIDField()
    name = serializers.CharField(max_length=150)
    full_name = serializers.CharField(
        max_length=1024, required=False)
    art = serializers.CharField(
        max_length=25, required=False, allow_blank=True)
    balance = serializers.DecimalField(
        max_digits=15, decimal_places=3, required=False)
    price = serializers.DecimalField(
        max_digits=15, decimal_places=2, required=False)
    volume = serializers.DecimalField(
        max_digits=15, decimal_places=3, required=False)
    strength = serializers.DecimalField(
        max_digits=15, decimal_places=3, required=False)
    in_package = serializers.DecimalField(
        max_digits=15, decimal_places=0, required=False)
    expiration_date = serializers.DecimalField(
        max_digits=15, decimal_places=0, required=False)
    category = CategorySerializer(required=False, allow_null=True)
    trade_mark = TradeMarkSerializer(required=False, allow_null=True)
    gassing = GassingSerializer(required=False, allow_null=True)
    pasteurization = PasteurizationSerializer(required=False, allow_null=True)
    filtering = FilteringSerializer(required=False, allow_null=True)
    manufacturer = ManufacturerSerializer(required=False, allow_null=True)
    unit = UnitSerializer(required=False, allow_null=True)


class SimpleGoodSerializer(serializers.Serializer):
    id = serializers.UUIDField()
    name = serializers.CharField(max_length=150)
    full_name = serializers.CharField(
        max_length=1024, required=False)
    art = serializers.CharField(
        max_length=25, required=False, allow_blank=True)
    balance = serializers.DecimalField(
        max_digits=15, decimal_places=3, required=False)
    price = serializers.DecimalField(
        max_digits=15, decimal_places=2, required=False)
    volume = serializers.DecimalField(
        max_digits=15, decimal_places=3, required=False)
    strength = serializers.DecimalField(
        max_digits=15, decimal_places=3, required=False)
    in_package = serializers.DecimalField(
        max_digits=15, decimal_places=0, required=False)
    expiration_date = serializers.DecimalField(
        max_digits=15, decimal_places=0, required=False)
    category_id = serializers.UUIDField(required=False, allow_null=True)
    trade_mark_id = serializers.UUIDField(required=False, allow_null=True)
    gassing_id = serializers.UUIDField(required=False, allow_null=True)
    pasteurization_id = serializers.UUIDField(required=False, allow_null=True)
    filtering_id = serializers.UUIDField(required=False, allow_null=True)
    manufacturer_id = serializers.UUIDField(required=False, allow_null=True)
    unit_id = serializers.UUIDField(required=False, allow_null=True)
