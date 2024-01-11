from django.contrib import admin
from catalog_app.models import (
    Category,
    Good,
    GoodsImage,
    TradeMark,
    Gassing,
    Filtering,
    Pasteurization,
    Manufacturer,
    Unit,
    Strength,
    Volume
)


@admin.register(Volume)
class VolumeAdmin(admin.ModelAdmin):
    list_display = ("__str__", 'id',)


@admin.register(Strength)
class StrengthAdmin(admin.ModelAdmin):
    list_display = ("__str__", 'id',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("__str__", 'id',)


@admin.register(TradeMark)
class TradeMarkAdmin(admin.ModelAdmin):
    list_display = ("__str__", 'id',)


@admin.register(Gassing)
class GassingAdmin(admin.ModelAdmin):
    list_display = ("__str__", 'id',)


@admin.register(Filtering)
class FilteringAdmin(admin.ModelAdmin):
    list_display = ("__str__", 'id',)


@admin.register(Pasteurization)
class PasteurizationAdmin(admin.ModelAdmin):
    list_display = ("__str__", 'id',)


@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ("__str__", 'id',)


@admin.register(Unit)
class UnitAdmin(admin.ModelAdmin):
    list_display = ("__str__", 'id',)


class GoodsImageInLine(admin.TabularInline):
    model = GoodsImage


@admin.register(Good)
class GoodAdmin(admin.ModelAdmin):
    inlines = [GoodsImageInLine]
    list_display = (
        "name", "art", "category",
        "is_active", "balance", "price",
    )
    search_fields = ("name", "art",)
