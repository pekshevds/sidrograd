from typing import Any
from decimal import Decimal
from django.utils.html import format_html
from django.contrib import admin
from catalog_app.models import (
    Category,
    Good,
    GoodsImage,
    TradeMark,
    Gassing,
    Filtering,
    # Pasteurization,
    Manufacturer,
    Unit,
    Strength,
    Volume,
    TypeOfFermentation,
    Style,
    Country,
)


admin.site.site_header = "Панель администрирования Сидроград"
admin.site.site_title = "Панель администрирования Сидроград"
admin.site.index_title = "Добро пожаловать!"


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = (
        "__str__",
        "code",
        "id",
    )
    ordering = ("-created_at",)
    search_fields = (
        "name",
        "code",
    )


@admin.register(TypeOfFermentation)
class TypeOfFermentationAdmin(admin.ModelAdmin):
    list_display = (
        "__str__",
        "id",
    )
    ordering = ("-created_at",)


@admin.register(Style)
class StyleAdmin(admin.ModelAdmin):
    list_display = (
        "__str__",
        "id",
    )
    ordering = ("-created_at",)


@admin.register(Volume)
class VolumeAdmin(admin.ModelAdmin):
    list_display = (
        "__str__",
        "id",
    )
    ordering = ("-created_at",)


@admin.register(Strength)
class StrengthAdmin(admin.ModelAdmin):
    list_display = (
        "__str__",
        "id",
    )
    ordering = ("-created_at",)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        "__str__",
        "id",
        "preview",
    )

    def preview(self, obj: Any) -> str | None:
        try:
            if obj.image:
                str = f"<img src={obj.image.url} style='max-height: 75px;'>"
                return format_html(str)
        except ValueError:
            return None
        return None

    preview.short_description = "Изображение 570х287"


@admin.register(TradeMark)
class TradeMarkAdmin(admin.ModelAdmin):
    list_display = (
        "__str__",
        "id",
    )
    search_fields = ("tags",)
    ordering = ("-created_at",)


@admin.register(Gassing)
class GassingAdmin(admin.ModelAdmin):
    list_display = (
        "__str__",
        "id",
    )
    ordering = ("-created_at",)


@admin.register(Filtering)
class FilteringAdmin(admin.ModelAdmin):
    list_display = (
        "__str__",
        "id",
    )
    ordering = ("-created_at",)


"""@admin.register(Pasteurization)
class PasteurizationAdmin(admin.ModelAdmin):
    list_display = ("__str__", 'id',)
    ordering = ("-created_at",)"""


@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    list_display = (
        "__str__",
        "id",
    )
    ordering = ("-created_at",)


@admin.register(Unit)
class UnitAdmin(admin.ModelAdmin):
    list_display = (
        "__str__",
        "id",
    )
    ordering = ("-created_at",)


class GoodsImageInLine(admin.TabularInline):
    model = GoodsImage
    fields = (
        "image",
        "preview",
    )
    readonly_fields = ("preview",)

    def preview(self, obj: Any) -> str | None:
        try:
            if obj.image:
                str = f"<img src={obj.image.image.url} style='max-height: 75px;'>"
                return format_html(str)
        except ValueError:
            return None
        return None

    preview.short_description = "Изображение (превью)"


@admin.register(Good)
class GoodAdmin(admin.ModelAdmin):
    inlines = [GoodsImageInLine]
    list_display_links = (
        "art",
        "full_name",
    )
    list_display = (
        "art",
        "full_name",
        "category",
        "country",
        "trade_mark",
        "is_active",
        "balance",
        "price",
        "price_by_liter",
        "preview",
        "comment",
    )
    exclude = ("full_name",)
    search_fields = (
        "art",
        "full_name",
        "tags",
        "trade_mark__tags",
    )

    def preview(self, obj: Any) -> str | None:
        try:
            if obj.image:
                str = f"<img src={obj.image.image.url} style='max-height: 75px;'>"
                return format_html(str)
        except ValueError:
            return None
        return None

    def price_by_liter(self, obj: Any) -> Decimal:
        return obj.price_by_liter

    preview.short_description = "Изображение (превью)"
    price_by_liter.short_description = "Цена за литр"
