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

    def preview(self, obj):
        if obj.image:
            str = f"<img src={obj.image.url} style='max-height: 75px;'>"
            return format_html(str)

    preview.short_description = "Изображение 570х287"


@admin.register(TradeMark)
class TradeMarkAdmin(admin.ModelAdmin):
    list_display = (
        "__str__",
        "id",
    )
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

    def preview(self, obj):
        if obj.image:
            str = f"<img src={obj.image.image.url} style='max-height: 75px;'>"
            return format_html(str)

    preview.short_description = "Изображение (превью)"


@admin.register(Good)
class GoodAdmin(admin.ModelAdmin):
    inlines = [GoodsImageInLine]
    list_display = (
        "name",
        "full_name",
        "art",
        "category",
        "country",
        "is_active",
        "balance",
        "price",
        "preview",
    )
    exclude = ("full_name",)
    search_fields = (
        "art",
        "full_name",
    )

    def preview(self, obj):
        if obj.image:
            str = f"<img src={obj.image.image.url} style='max-height: 75px;'>"
            return format_html(str)

    preview.short_description = "Изображение (превью)"
