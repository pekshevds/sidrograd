from django.contrib import admin
from index_app.models import ContactInfo


@admin.register(ContactInfo)
class ContactInfoAdmin(admin.ModelAdmin):
    list_display = (
        "value",
        "type",
    )
    ordering = ["-updated_at"]
