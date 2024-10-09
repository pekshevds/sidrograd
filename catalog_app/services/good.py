from threading import Thread
from typing import Any
from django.db.models.query import QuerySet
from django.db.models import Q
from django.db import transaction
from catalog_app.models import (
    Good,
    Category,
    TradeMark,
    Manufacturer,
    Filtering,
    Gassing,
    # Pasteurization,
    Unit,
    Volume,
    Strength,
    Style,
    TypeOfFermentation,
    Country,
)

from catalog_app.services.category import handle_category
from catalog_app.services.trade_mark import handle_trade_mark
from catalog_app.services.gassing import handle_gassing

# from catalog_app.services.pasteurization import handle_pasteurization
from catalog_app.services.filtering import handle_filtering
from catalog_app.services.manufacturer import handle_manufacturer
from catalog_app.services.unit import handle_unit
from catalog_app.services.style import handle_style
from catalog_app.services.type_of_fermentation import handle_type_of_fermentation
from catalog_app.services.volume import handle_volume
from catalog_app.services.strength import handle_strength
from catalog_app.services.country import handle_country


def good_by_id(good_id: str) -> Good:
    return Good.objects.filter(id=good_id).first()


def handle_good(good_dir: dict) -> Good:
    good_id = good_dir.get("id")
    good, _ = Good.objects.get_or_create(id=good_id)
    good.full_name = good_dir.get("full_name", good.full_name)
    good.price = good_dir.get("price", good.price)
    good.balance = good_dir.get("balance", good.balance)
    good.art = good_dir.get("art", good.art)
    good.in_package = good_dir.get("in_package", good.in_package)
    good.expiration_date = good_dir.get("expiration_date", good.expiration_date)

    key_name = "volume"
    if key_name in good_dir:
        temp_dir = good_dir.get(key_name)
        good.volume = None if temp_dir is None else handle_volume(temp_dir)

    key_name = "strength"
    if key_name in good_dir:
        temp_dir = good_dir.get(key_name)
        good.strength = None if temp_dir is None else handle_strength(temp_dir)

    key_name = "category"
    if key_name in good_dir:
        temp_dir = good_dir.get(key_name)
        good.category = None if temp_dir is None else handle_category(temp_dir)

    key_name = "trade_mark"
    if key_name in good_dir:
        temp_dir = good_dir.get(key_name)
        good.trade_mark = None if temp_dir is None else handle_trade_mark(temp_dir)

    key_name = "gassing"
    if key_name in good_dir:
        temp_dir = good_dir.get(key_name)
        good.gassing = None if temp_dir is None else handle_gassing(temp_dir)

    """key_name = 'pasteurization'
    if key_name in good_dir:
        temp_dir = good_dir.get(key_name)
        good.pasteurization = None if temp_dir is None else \
            handle_pasteurization(temp_dir)"""

    key_name = "filtering"
    if key_name in good_dir:
        temp_dir = good_dir.get(key_name)
        good.filtering = None if temp_dir is None else handle_filtering(temp_dir)

    key_name = "manufacturer"
    if key_name in good_dir:
        temp_dir = good_dir.get(key_name)
        good.manufacturer = None if temp_dir is None else handle_manufacturer(temp_dir)

    key_name = "unit"
    if key_name in good_dir:
        temp_dir = good_dir.get(key_name)
        good.unit = None if temp_dir is None else handle_unit(temp_dir)

    key_name = "style"
    if key_name in good_dir:
        temp_dir = good_dir.get(key_name)
        good.unit = None if temp_dir is None else handle_style(temp_dir)

    key_name = "type_of_fermentation"
    if key_name in good_dir:
        temp_dir = good_dir.get(key_name)
        good.unit = None if temp_dir is None else handle_type_of_fermentation(temp_dir)

    key_name = "country"
    if key_name in good_dir:
        temp_dir = good_dir.get(key_name)
        good.unit = None if temp_dir is None else handle_country(temp_dir)

    good.save()
    return good


def handle_good_list(good_list: list[dict[str, Any]]) -> list[Good]:
    goods_id = []
    with transaction.atomic():
        for good_item in good_list:
            good = handle_good(good_dir=good_item)
            goods_id.append(good.id)

    return Good.objects.filter(id__in=goods_id)


def fetch_goods_queryset_by_name_or_article(
    search: str, only_active: bool = False
) -> QuerySet:
    if only_active:
        queryset = Good.active_goods.filter(
            Q(art__icontains=search) | Q(full_name__icontains=search)
        )
    else:
        queryset = Good.objects.filter(
            Q(art__icontains=search) | Q(full_name__icontains=search)
        )
    return queryset


def fetch_goods_queryset_by_category(
    categories: list[Category], only_active: bool = False
) -> QuerySet:
    if only_active:
        queryset = Good.active_goods.filter(category__in=categories)
    else:
        queryset = Good.objects.filter(category__in=categories)
    return queryset


def fetch_goods_queryset_by_trade_mark(
    trade_marks: list[TradeMark], only_active: bool = False
) -> QuerySet:
    if only_active:
        queryset = Good.active_goods.filter(trade_mark__in=trade_marks)
    else:
        queryset = Good.objects.filter(trade_mark__in=trade_marks)
    return queryset


def fetch_goods_queryset_by_filters(
    categories: list[Category],
    trade_marks: list[TradeMark],
    manufacturers: list[Manufacturer],
    filterings: list[Filtering],
    gassings: list[Gassing],
    units: list[Unit],
    styles: list[Style],
    types_of_fermentation: list[TypeOfFermentation],
    volumes: list[Volume],
    strengths: list[Strength],
    countryes: list[Country],
    only_active: bool = False,
) -> QuerySet | None:
    filters = Q()
    if categories:
        filters.add(Q(category__in=categories), Q.AND)

    if trade_marks:
        filters.add(Q(trade_mark__in=trade_marks), Q.AND)

    if manufacturers:
        filters.add(Q(manufacturer__in=manufacturers), Q.AND)

    if filterings:
        filters.add(Q(filtering__in=filterings), Q.AND)

    if gassings:
        filters.add(Q(gassing__in=gassings), Q.AND)

    """if pasteurizations:
        filters.add(Q(pasteurization__in=pasteurizations), Q.AND)"""

    if units:
        filters.add(Q(unit__in=units), Q.AND)

    if styles:
        filters.add(Q(style__in=styles), Q.AND)

    if types_of_fermentation:
        filters.add(Q(type_of_fermentation__in=types_of_fermentation), Q.AND)

    if volumes:
        filters.add(Q(volume__in=volumes), Q.AND)

    if strengths:
        filters.add(Q(strength__in=strengths), Q.AND)

    if countryes:
        filters.add(Q(country__in=countryes), Q.AND)

    if len(filters) > 0:
        if only_active:
            return Good.active_goods.filter(filters)
        else:
            return Good.objects.filter(filters)
    return None


def run_update_prices(new_prices: list[dict]) -> bool:
    thread = Thread(target=update_prices, kwargs={"new_prices": new_prices})
    thread.start()
    thread.join()
    return True


def update_prices(new_prices: list[dict]) -> bool:
    goods_for_update = []
    for record in new_prices:
        good = Good.objects.filter(art=record.get("barcode")).first()
        if good:
            good.price = record.get("price", good.price)
            good.balance = record.get("balance", good.balance)
            goods_for_update.append(good)
    Good.objects.bulk_update(goods_for_update, ["price", "balance"], batch_size=100)
    return True


def handle_new_goods(data: list[dict[str, Any]]) -> None:
    goods_for_update = []
    for record in data:
        good, _ = Good.objects.get_or_create(art=record.get("art"))
        good.name = record.get("name", good.name)
        good.unit = Unit.objects.filter(name=record.get("unit")).first()
        good.country = Country.objects.filter(name=record.get("country")).first()
        good.volume = Volume.objects.filter(name=record.get("volume")).first()
        good.trade_mark = TradeMark.objects.filter(
            name=record.get("trade_mark")
        ).first()
        good.strength = Strength.objects.filter(name=record.get("strength")).first()
        good.category = Category.objects.filter(name=record.get("category")).first()
        goods_for_update.append(good)
    Good.objects.bulk_update(
        goods_for_update,
        ["name", "unit", "country", "volume", "trade_mark", "strength", "category"],
        batch_size=100,
    )
