from dataclasses import dataclass
from collections import Counter
from typing import List
from django.http import HttpRequest
from django.db.models import Count
from django.db.models import QuerySet
from django.db.models import Q

from catalog_app.services.category import category_by_id_list
from catalog_app.services.trade_mark import trade_mark_by_id_list
from catalog_app.services.manufacturer import manufacturer_by_id_list
from catalog_app.services.filtering import filtering_by_id_list
from catalog_app.services.gassing import gassing_by_id_list
from catalog_app.services.unit import unit_by_id_list
from catalog_app.services.style import style_by_id_list
from catalog_app.services.type_of_fermentation import type_of_fermentation_by_id_list
from catalog_app.services.volume import volume_by_id_list
from catalog_app.services.strength import strength_by_id_list
from catalog_app.services.country import country_by_id_list

from catalog_app.models import Good
# from catalog_app.services import object_by_id_list


@dataclass
class Data:
    def __init__(
        self,
        trade_mark: Counter,
        gassing: Counter,
        filtering: Counter,
        manufacturer: Counter,
        unit: Counter,
        style: Counter,
        type_of_fermentation: Counter,
        strength: Counter,
        volume: Counter,
        country: Counter,
    ) -> None:
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


@dataclass
class Record:
    id: str
    name: str
    count: int


def fetch_goods_queryset_by_filters(
    categories: List[object],
    trade_marks: List[object],
    manufacturers: List[object],
    filterings: List[object],
    gassings: List[object],
    units: List[object],
    styles: List[object],
    types_of_fermentation: List[object],
    volumes: List[object],
    strengths: List[object],
    countryes: List[object],
) -> QuerySet | None:
    filters = Q()
    condition = Q.OR
    if categories:
        filters.add(Q(category__in=categories), condition)

    if trade_marks:
        filters.add(Q(trade_mark__in=trade_marks), condition)

    if manufacturers:
        filters.add(Q(manufacturer__in=manufacturers), condition)

    if filterings:
        filters.add(Q(filtering__in=filterings), condition)

    if gassings:
        filters.add(Q(gassing__in=gassings), condition)

    if units:
        filters.add(Q(unit__in=units), condition)

    if styles:
        filters.add(Q(style__in=styles), condition)

    if types_of_fermentation:
        filters.add(Q(type_of_fermentation__in=types_of_fermentation), condition)

    if volumes:
        filters.add(Q(volume__in=volumes), condition)

    if strengths:
        filters.add(Q(strength__in=strengths), condition)

    if countryes:
        filters.add(Q(country__in=countryes), condition)

    if len(filters) > 0:
        return Good.objects.filter(filters)
    return None


def fetch_filters_by_goods(goods: QuerySet) -> Data:
    data = Data(
        trade_mark=Counter(),
        gassing=Counter(),
        filtering=Counter(),
        manufacturer=Counter(),
        unit=Counter(),
        style=Counter(),
        type_of_fermentation=Counter(),
        strength=Counter(),
        volume=Counter(),
        country=Counter(),
    )

    for item in goods:
        if item.trade_mark:
            data.trade_mark[item.trade_mark] += 1
        if item.gassing:
            data.gassing[item.gassing] += 1
        if item.filtering:
            data.filtering[item.filtering] += 1
        if item.manufacturer:
            data.manufacturer[item.manufacturer] += 1
        if item.unit:
            data.unit[item.unit] += 1
        if item.style:
            data.style[item.style] += 1
        if item.type_of_fermentation:
            data.type_of_fermentation[item.type_of_fermentation] += 1
        if item.strength:
            data.strength[item.strength] += 1
        if item.volume:
            data.volume[item.volume] += 1
        if item.country:
            data.country[item.country] += 1
    return data


def prepare_query_set(data: Counter) -> tuple:
    query_set = [Record(key.id, key.name, value) for key, value in data]
    # for key, value in data:
    #     query_set.append(Record(key.id, key.name, value))
    return tuple(query_set)


def fetch_filters(request: HttpRequest) -> list:
    categories = None
    obj_id = request.GET.get("category_id")
    if obj_id:
        categories = category_by_id_list(obj_id.split(","))

    trade_marks = None
    obj_id = request.GET.get("trade_mark_id")
    if obj_id:
        trade_marks = trade_mark_by_id_list(obj_id.split(","))

    manufacturers = None
    obj_id = request.GET.get("manufacturer_id")
    if obj_id:
        manufacturers = manufacturer_by_id_list(obj_id.split(","))

    filterings = None
    obj_id = request.GET.get("filtering_id")
    if obj_id:
        filterings = filtering_by_id_list(obj_id.split(","))

    gassings = None
    obj_id = request.GET.get("gassing_id")
    if obj_id:
        gassings = gassing_by_id_list(obj_id.split(","))

    units = None
    obj_id = request.GET.get("unit_id")
    if obj_id:
        units = unit_by_id_list(obj_id.split(","))

    styles = None
    obj_id = request.GET.get("style_id")
    if obj_id:
        styles = style_by_id_list(obj_id.split(","))

    types_of_fermentation = None
    obj_id = request.GET.get("type_of_fermentation_id")
    if obj_id:
        types_of_fermentation = type_of_fermentation_by_id_list(obj_id.split(","))

    volumes = None
    obj_id = request.GET.get("volume_id")
    if obj_id:
        volumes = volume_by_id_list(obj_id.split(","))

    strengths = None
    obj_id = request.GET.get("strength_id")
    if obj_id:
        strengths = strength_by_id_list(obj_id.split(","))

    countryes = None
    obj_id = request.GET.get("country_id")
    if obj_id:
        countryes = country_by_id_list(obj_id.split(","))
    return [
        categories,
        trade_marks,
        manufacturers,
        filterings,
        gassings,
        units,
        styles,
        types_of_fermentation,
        volumes,
        strengths,
        countryes,
    ]


def fetch_goods_by_filters(args) -> QuerySet:
    queryset = fetch_goods_queryset_by_filters(
        args[0],
        args[1],
        args[2],
        args[3],
        args[4],
        args[5],
        args[6],
        args[7],
        args[8],
        args[9],
        args[10],
    )
    return queryset


def query_set(Class) -> List[Record]:
    categories = []
    qs = Class.objects.annotate(num_cat=Count("good", distinct=True))
    for _ in qs:
        if _.num_cat > 0:
            categories.append(Record(_.id, _.name, _.num_cat))
    categories.sort(key=lambda obj: obj.count, reverse=True)
    return categories
