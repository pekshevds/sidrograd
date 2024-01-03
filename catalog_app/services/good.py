from django.db.models import Q
from django.db import transaction
from catalog_app.models import (
    Good,
    Category,
    TradeMark
)

from catalog_app.services.category import handle_category
from catalog_app.services.trade_mark import handle_trade_mark
from catalog_app.services.gassing import handle_gassing
from catalog_app.services.pasteurization import handle_pasteurization
from catalog_app.services.filtering import handle_filtering
from catalog_app.services.manufacturer import handle_manufacturer
from catalog_app.services.unit import handle_unit


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
    good.volume = good_dir.get('volume', good.volume)
    good.strength = good_dir.get('strength', good.strength)
    good.in_package = good_dir.get('in_package', good.in_package)
    good.expiration_date = good_dir.get('expiration_date',
                                        good.expiration_date)
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

    key_name = 'pasteurization'
    if key_name in good_dir:
        temp_dir = good_dir.get(key_name)
        good.pasteurization = None if temp_dir is None else \
            handle_pasteurization(temp_dir)

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

    good.save()
    return good


def handle_good_list(good_list: None) -> [Good]:
    goods_id = []
    with transaction.atomic():
        for good_item in good_list:
            good = handle_good(good_dir=good_item)
            goods_id.append(good.id)

    return Good.objects.filter(id__in=goods_id)


def fetch_goods_queryset_by_name_or_article(search: str):
    queryset = Good.objects.filter(
        Q(name__icontains=search) |
        Q(art__icontains=search)
        )
    return queryset


def fetch_goods_queryset_by_category(categories: [Category]):
    queryset = Good.objects.filter(category__in=categories)
    return queryset


def fetch_goods_queryset_by_trade_mark(trade_marks: [TradeMark]):
    queryset = Good.objects.filter(trade_mark__in=trade_marks)
    return queryset


def fetch_goods_queryset_by_filters(
        categories: [Category],
        trade_marks: [TradeMark]
        ):
    filters = Q()
    if categories:
        filters.add(Q(category__in=categories), Q.AND)

    if trade_marks:
        filters.add(Q(trade_mark__in=trade_marks), Q.AND)

    queryset = Good.objects.filter(filters)
    return queryset
