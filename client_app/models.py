from django.db import models
from server.base import Directory


class Client(Directory):
    class Meta:
        verbose_name = "Клиент"
        verbose_name_plural = "Клиенты"


class Point(Directory):
    client = models.ForeignKey(
        Client,
        verbose_name="Клиент",
        on_delete=models.PROTECT,
        related_name="addresses",
    )
    address = models.TextField(verbose_name="Адрес", null=True, blank=True, default="")

    class Meta:
        verbose_name = "Адрес доставки "
        verbose_name_plural = "Адреса доставки"
