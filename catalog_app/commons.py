from dataclasses import dataclass
from collections import Counter
from typing import Tuple, List
import hashlib
from django.http import HttpRequest
from django.db.models import Count
from django.db.models import QuerySet

from catalog_app.services.category import category_by_id_list
from catalog_app.services.trade_mark import trade_mark_by_id_list
from catalog_app.services.manufacturer import manufacturer_by_id_list
from catalog_app.services.filtering import filtering_by_id_list
from catalog_app.services.gassing import gassing_by_id_list
from catalog_app.services.unit import unit_by_id_list
from catalog_app.services.volume import volume_by_id_list
from catalog_app.services.strength import strength_by_id_list
from catalog_app.services.style import style_by_id_list
from catalog_app.services.country import country_by_id_list
from catalog_app.services.type_of_fermentation import (
    type_of_fermentation_by_id_list
)
from catalog_app.services.good import fetch_goods_queryset_by_filters


def secret_from_string(string: str) -> str:
    hash = hashlib.blake2s(digest_size=4)
    hash.update(string.encode('utf-8'))
    return hash.hexdigest()


@dataclass
class Data:
    def __init__(self,
                 trade_mark: Counter, gassing: Counter, filtering: Counter,
                 manufacturer: Counter, unit: Counter, style: Counter,
                 type_of_fermentation: Counter, strength: Counter,
                 volume: Counter, country: Counter) -> None:
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


def fetch_filters_by_goods(goods: QuerySet) -> Data:
    data = Data(
        trade_mark=Counter(), gassing=Counter(), filtering=Counter(),
        manufacturer=Counter(), unit=Counter(), style=Counter(),
        type_of_fermentation=Counter(), strength=Counter(),
        volume=Counter(), country=Counter())

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


def prepare_query_set(data: Counter) -> Tuple[Record]:
    query_set = list()
    for _ in data:
        query_set.append(Record(_.id, _.name, _.count))
    return tuple(query_set)


def fetch_filters(request: HttpRequest) -> tuple:
    categories = None
    category_id = request.GET.get("category_id")
    if category_id:
        categories = category_by_id_list(category_id.split(","))

    trade_marks = None
    trade_mark_id = request.GET.get("trade_mark_id")
    if trade_mark_id:
        trade_marks = trade_mark_by_id_list(
            trade_mark_id.split(",")
        )

    manufacturers = None
    manufacturer_id = request.GET.get("manufacturer_id")
    if manufacturer_id:
        manufacturers = manufacturer_by_id_list(
            manufacturer_id.split(",")
        )

    filterings = None
    filtering_id = request.GET.get("filtering_id")
    if filtering_id:
        filterings = filtering_by_id_list(
            filtering_id.split(",")
        )

    gassings = None
    gassing_id = request.GET.get("gassing_id")
    if gassing_id:
        gassings = gassing_by_id_list(
            gassing_id.split(",")
        )

    units = None
    unit_id = request.GET.get("unit_id")
    if unit_id:
        units = unit_by_id_list(
            unit_id.split(",")
        )

    styles = None
    style_id = request.GET.get("style_id")
    if style_id:
        styles = style_by_id_list(
            style_id.split(",")
        )

    types_of_fermentation = None
    type_of_fermentation_id = \
        request.GET.get("type_of_fermentation_id")
    if type_of_fermentation_id:
        types_of_fermentation = type_of_fermentation_by_id_list(
            type_of_fermentation_id.split(",")
        )

    volumes = None
    volume_id = request.GET.get("volume_id")
    if volume_id:
        volumes = volume_by_id_list(
            volume_id.split(",")
        )

    strengths = None
    strength_id = request.GET.get("strength_id")
    if strength_id:
        strengths = strength_by_id_list(
            strength_id.split(",")
        )

    countryes = None
    country_id = request.GET.get("country_id")
    if country_id:
        countryes = country_by_id_list(
            country_id.split(",")
        )
    return categories, trade_marks, manufacturers, \
        filterings, gassings, units, styles, \
        types_of_fermentation, volumes, strengths, \
        countryes


def fetch_goods_by_filters(*args) -> QuerySet:

    queryset = fetch_goods_queryset_by_filters(
        args[0], args[1], args[2],
        args[3], args[4], args[5],
        args[6], args[7], args[8],
        args[9], args[10]
    )
    return queryset


def query_set(Class) -> List[Record]:
    categories = []
    qs = Class.objects.annotate(num_cat=Count("good", distinct=True))
    for _ in qs:
        if _.num_cat > 0:
            categories.append(
                Record(_.id, _.name, _.num_cat)
            )
    categories.sort(key=lambda obj: obj.count, reverse=True)
    return categories
