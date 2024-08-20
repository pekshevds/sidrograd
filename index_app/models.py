from django.utils.translation import gettext_lazy as _
from django.db.models import Q
from django.db import models
from server.base import Directory


class TypeOfContactInfo(models.TextChoices):
    PH = "PH", _("Телефон")
    EM = "EM", _("Почта")


class AvailablePhonesManager(models.Manager):
    def get_queryset(self):
        filters = Q()
        filters.add(Q(type=TypeOfContactInfo.PH), Q.AND)
        filters.add(Q(marked=False), Q.AND)
        return super().get_queryset().filter(filters)


class AvailableEmailsManager(models.Manager):
    def get_queryset(self):
        filters = Q()
        filters.add(Q(type=TypeOfContactInfo.EM), Q.AND)
        filters.add(Q(marked=False), Q.AND)
        return super().get_queryset().filter(filters)


class ContactInfo(Directory):
    type = models.CharField(
        max_length=150,
        verbose_name="Тип",
        choices=TypeOfContactInfo.choices,
        default=TypeOfContactInfo.PH,
    )
    value = models.CharField(max_length=150, verbose_name="Значение")
    objects = models.Manager()
    available_phones = AvailablePhonesManager()
    available_emails = AvailableEmailsManager()

    class Meta:
        verbose_name = "Запись"
        verbose_name_plural = "Контактная информация для информирования"
