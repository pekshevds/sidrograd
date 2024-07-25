from django.db import models
from server.base import Directory


class Image(Directory):
    image = models.ImageField(
        verbose_name="Файл изображения", upload_to="images/", blank=True, null=True
    )

    class Meta:
        verbose_name = "Изображение"
        verbose_name_plural = "Изображения"
        ordering = ["-updated_at"]


class Carousel(Directory):
    image = models.ImageField(
        verbose_name="Файл изображения",
        upload_to="carousel_images/",
        blank=True,
        null=True,
    )
    order_by = models.SmallIntegerField(
        verbose_name="Порядок сортировки", null=True, blank=True, default=0
    )

    class Meta:
        verbose_name = "Элемент 1200х680"
        verbose_name_plural = "Карусель"
        ordering = ["order_by"]
