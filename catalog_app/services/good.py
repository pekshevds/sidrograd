from typing import List
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
    Country
)

from catalog_app.services.category import handle_category
from catalog_app.services.trade_mark import handle_trade_mark
from catalog_app.services.gassing import handle_gassing
# from catalog_app.services.pasteurization import handle_pasteurization
from catalog_app.services.filtering import handle_filtering
from catalog_app.services.manufacturer import handle_manufacturer
from catalog_app.services.unit import handle_unit
from catalog_app.services.style import handle_style
from catalog_app.services.type_of_fermentation import \
    handle_type_of_fermentation
from catalog_app.services.volume import handle_volume
from catalog_app.services.strength import handle_strength
from catalog_app.services.country import handle_country


def good_by_id(good_id: str) -> Good:
    return Good.objects.filter(id=good_id).first()


def handle_good(good_dir: dir) -> Good:
    good_id = good_dir.get('id', None)
    good = good_by_id(good_id)
    if good is None:
        good = Good.objects.create(
            id=good_id
        )
    good.full_name = good_dir.get('full_name', good.full_name)
    good.price = good_dir.get('price', good.price)
    good.balance = good_dir.get('balance', good.balance)
    good.art = good_dir.get('art', good.art)
    good.in_package = good_dir.get('in_package', good.in_package)
    good.expiration_date = good_dir.get('expiration_date',
                                        good.expiration_date)

    key_name = 'volume'
    if key_name in good_dir:
        temp_dir = good_dir.get(key_name)
        good.volume = None if temp_dir is None else \
            handle_volume(temp_dir)

    key_name = 'strength'
    if key_name in good_dir:
        temp_dir = good_dir.get(key_name)
        good.strength = None if temp_dir is None else \
            handle_strength(temp_dir)

    key_name = 'category'
    if key_name in good_dir:
        temp_dir = good_dir.get(key_name)
        good.category = None if temp_dir is None else \
            handle_category(temp_dir)

    key_name = 'trade_mark'
    if key_name in good_dir:
        temp_dir = good_dir.get(key_name)
        good.trade_mark = None if temp_dir is None else \
            handle_trade_mark(temp_dir)

    key_name = 'gassing'
    if key_name in good_dir:
        temp_dir = good_dir.get(key_name)
        good.gassing = None if temp_dir is None else \
            handle_gassing(temp_dir)

    """key_name = 'pasteurization'
    if key_name in good_dir:
        temp_dir = good_dir.get(key_name)
        good.pasteurization = None if temp_dir is None else \
            handle_pasteurization(temp_dir)"""

    key_name = 'filtering'
    if key_name in good_dir:
        temp_dir = good_dir.get(key_name)
        good.filtering = None if temp_dir is None else \
            handle_filtering(temp_dir)

    key_name = 'manufacturer'
    if key_name in good_dir:
        temp_dir = good_dir.get(key_name)
        good.manufacturer = None if temp_dir is None else \
            handle_manufacturer(temp_dir)

    key_name = 'unit'
    if key_name in good_dir:
        temp_dir = good_dir.get(key_name)
        good.unit = None if temp_dir is None else \
            handle_unit(temp_dir)

    key_name = 'style'
    if key_name in good_dir:
        temp_dir = good_dir.get(key_name)
        good.unit = None if temp_dir is None else \
            handle_style(temp_dir)

    key_name = 'type_of_fermentation'
    if key_name in good_dir:
        temp_dir = good_dir.get(key_name)
        good.unit = None if temp_dir is None else \
            handle_type_of_fermentation(temp_dir)

    key_name = 'country'
    if key_name in good_dir:
        temp_dir = good_dir.get(key_name)
        good.unit = None if temp_dir is None else \
            handle_country(temp_dir)

    good.save()
    return good


def handle_good_list(good_list: None) -> List[Good]:
    goods_id = []
    with transaction.atomic():
        for good_item in good_list:
            good = handle_good(good_dir=good_item)
            goods_id.append(good.id)

    return Good.objects.filter(id__in=goods_id)


def fetch_goods_queryset_by_name_or_article(search: str):
    queryset = Good.objects.filter(
        # Q(name__icontains=search) |
        Q(art__icontains=search) |
        Q(full_name__icontains=search)
        )
    return queryset


def fetch_goods_queryset_by_category(categories: List[Category]):
    queryset = Good.objects.filter(category__in=categories)
    return queryset


def fetch_goods_queryset_by_trade_mark(trade_marks: List[TradeMark]):
    queryset = Good.objects.filter(trade_mark__in=trade_marks)
    return queryset


def fetch_goods_queryset_by_filters(
        categories: List[Category],
        trade_marks: List[TradeMark],
        manufacturers: List[Manufacturer],
        filterings: List[Filtering],
        gassings: List[Gassing],
        units: List[Unit],
        styles: List[Style],
        types_of_fermentation: List[TypeOfFermentation],
        volumes: List[Volume],
        strengths: List[Strength],
        countryes: List[Country],
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
        return Good.objects.filter(filters)
    return None


def update_prices(new_prices: list[dir]):
    goods_for_update = []
    for record in new_prices:
        good = Good.objects.filter(art=record["barcode"]).first()
        if good:
            good.price = record.get("price", good.price)
            good.balance = record.get("balance", good.balance)
            goods_for_update.append(good)
    Good.objects.bulk_update(
        goods_for_update,
        ["price", "balance"],
        batch_size=100
    )
    return True
