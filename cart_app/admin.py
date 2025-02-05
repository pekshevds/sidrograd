from django.contrib import admin
from django.db.models import Model
from cart_app.models import Cart


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ("good", "user", "quantity", "id", "trade_mark", "volume")

    def trade_mark(self, obj: Model) -> Model:
        return obj.good.trade_mark

    trade_mark.short_description = "Торговая марка"

    def volume(self, obj: Model) -> Model:
        return obj.good.volume

    volume.short_description = "Объем"
