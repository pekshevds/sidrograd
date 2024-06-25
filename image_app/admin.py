from django.utils.html import format_html
from django.contrib import admin
from image_app.models import Image, Carousel


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    fields = ("name", "image", "preview",)
    list_display = ("name", "id", "preview",)
    readonly_fields = ("preview",)

    def preview(self, obj):
        if obj.image:
            str = f"<img src={obj.image.url} style='max-height: 75px;'>"
            return format_html(str)
        return ""

    preview.short_description = "Изображение"


@admin.register(Carousel)
class CarouselAdmin(admin.ModelAdmin):
    fields = ("name", "image", "preview", "order_by", )
    list_display = ("name", "id", "preview", "order_by",)
    readonly_fields = ("preview",)

    def preview(self, obj):
        try:
            return format_html(f"<img src={obj.image.image.url} style='max-height: 75px;'>")
        except ValueError:
            return ""
        """if obj.image:
            str = f"<img src={obj.image.image.url} style='max-height: 75px;'>"
            return format_html(str)
        return """""

    preview.short_description = "Изображение"
