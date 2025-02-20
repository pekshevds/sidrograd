from django.contrib import admin
from order_app.models import Customer
from order_app.models import Organization
from order_app.models import Contract
from order_app.models import OrderStatus
from order_app.models import Order
from order_app.models import ItemOrder


@admin.register(OrderStatus)
class OrderStatusAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "value",
        "id",
    )


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "inn",
        "id",
    )
    ordering = ["-updated_at"]


@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "inn",
        "id",
    )
    ordering = ["-updated_at"]


@admin.register(Contract)
class ContractAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "number",
        "date",
        "client",
        "customer",
        "organization",
        "id",
    )
    search_fields = ("number",)
    list_filter = (
        "client",
        "customer",
        "organization",
    )
    date_hierarchy = "date"
    ordering = ["-updated_at"]


class ItemOrderInLine(admin.TabularInline):
    model = ItemOrder
    raw_id_fields = ["good"]


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    inlines = [ItemOrderInLine]
    list_display = (
        "__str__",
        "number",
        "date",
        "contract",
        "client",
        "customer",
        "organization",
        "author",
        "comment",
        "address",
        "id",
        "status",
    )
    search_fields = ("number",)
    list_filter = (
        "client",
        "customer",
        "organization",
        "author",
        "status",
    )
    # date_hierarchy = "date"
