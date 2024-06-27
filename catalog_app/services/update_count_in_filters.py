from dataclasses import dataclass
from django.db.models import QuerySet
from catalog_app.models import (
    Category,
    TradeMark,
    Manufacturer,
    Filtering,
    Gassing,
    Unit,
    Volume,
    Strength,
    Style,
    TypeOfFermentation,
    Country
)


@dataclass
class Data:
    def __init__(self,
                 trade_mark: QuerySet, gassing: QuerySet, filtering: QuerySet,
                 manufacturer: QuerySet, unit: QuerySet, style: QuerySet,
                 type_of_fermentation: QuerySet, strength: QuerySet,
                 volume: QuerySet, country: QuerySet) -> None:
        self.trade_mark = trade_mark
        self.gassing = gassing
        self.filtering = filtering
        self.manufacturer = manufacturer
        self.unit = unit
        self.style = style
        self.type_of_fermentation = type_of_fermentation
        self.strength = strength
        self.volume = volume
        self.country = country


def update_count_in_filter(_class):
    obj_for_update = []
    for obj in _class.objects.all():
        obj.count = obj.goods.count()
        obj_for_update.append(obj)
    _class.objects.bulk_update(
        obj_for_update,
        ["count"],
        batch_size=100
    )


def update_count_in_filters():
    update_count_in_filter(Category)
    update_count_in_filter(TradeMark)
    update_count_in_filter(Manufacturer)
    update_count_in_filter(Filtering)
    update_count_in_filter(Gassing)
    update_count_in_filter(Unit)
    update_count_in_filter(Volume)
    update_count_in_filter(Strength)
    update_count_in_filter(Style)
    update_count_in_filter(TypeOfFermentation)
    update_count_in_filter(Country)


def fetch_filters_by_goods(goods: QuerySet) -> object:
    return Data(
        trade_mark=TradeMark.objects.filter(count__gt=0).order_by("-count"),
        gassing=Gassing.objects.filter(count__gt=0).order_by("-count"),
        filtering=Filtering.objects.filter(count__gt=0).order_by("-count"),
        manufacturer=Filtering.objects.filter(count__gt=0).order_by("-count"),
        unit=Unit.objects.filter(count__gt=0).order_by("-count"),
        style=Style.objects.filter(count__gt=0).order_by("-count"),
        type_of_fermentation=TypeOfFermentation.objects.filter(count__gt=0).order_by("-count"),
        strength=Strength.objects.filter(count__gt=0).order_by("-count"),
        volume=Volume.objects.filter(count__gt=0).order_by("-count"),
        country=Country.objects.filter(count__gt=0).order_by("-count"),
    )
