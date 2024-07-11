from django.contrib import admin
from auth_app.models import User
from client_app.models import Client, Point


class UserInLine(admin.TabularInline):
    model = User
    fields = ("username",)
    extra = 1


class PointInLine(admin.TabularInline):
    model = Point
    fields = (
        "name",
        "address",
    )
    extra = 1


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    inlines = [UserInLine, PointInLine]
    list_display = (
        "name",
        "id",
    )
    ordering = ["-updated_at"]
