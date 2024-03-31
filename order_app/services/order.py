from typing import List
from django.db import transaction
from django.core.exceptions import ObjectDoesNotExist
from order_app.models import (
    OrderStatus,
    Order,
    ItemOrder
)
from auth_app.models import User
from order_app.services.contract import contract_by_id
from catalog_app.services.good import good_by_id


def default_order_status() -> OrderStatus:
    return status_by_value("CR")


def status_by_value(value: str) -> OrderStatus:
    return OrderStatus.objects.filter(value=value).first()


def put_order_status(order: Order, status: OrderStatus) -> bool:
    try:
        order.status = status
        order.save()
        return True
    except Exception:
        return False


def new_orders() -> Order:
    status = default_order_status()
    return Order.objects.filter(status=status)


def order_by_id(order_id: str) -> Order:
    return Order.objects.filter(id=order_id).first()


def item_order_by_id(item_order_id: str) -> ItemOrder:
    return ItemOrder.objects.filter(id=item_order_id).first()


def handle_order(order_dir: dir, author: None | User) -> Order:
    changed = False
    order_id = order_dir.get('id', None)
    order = order_by_id(order_id)
    if order is None:
        if order_id:
            order = Order.objects.create(id=order_id)
        else:
            order = Order.objects.create()
        order.author = author
        changed = True
    key_name = 'contract_id'
    if key_name in order_dir:
        contract_id = order_dir.get(key_name)
        order.contract = None if contract_id is None else \
            contract_by_id(contract_id=contract_id)
        if not order.contract:
            raise ObjectDoesNotExist("contract does't exist")
        changed = True
    key_name = 'items'
    if key_name in order_dir:
        items = order_dir.get(key_name)
        handle_items_order(items, order=order)
    order.status = order_dir.get('status', order.status)
    if changed:
        order.save()
    return order


def handle_items_order(items_list: List, order: Order) -> None:
    changed = False
    for item_dir in items_list:
        item_order_id = item_dir.get("id", None)
        item_order = item_order_by_id(item_order_id=item_order_id)

        if item_order is None:
            item_order = ItemOrder.objects.create(
                id=item_order_id,
                order=order
            )
            changed = True

        key_name = 'good_id'
        if key_name in item_dir:
            good_id = item_dir.get(key_name)
            item_order.good = None if good_id is None else \
                good_by_id(good_id=good_id)
            changed = True

        key_name = 'quantity'
        if key_name in item_dir:
            setattr(item_order, key_name, item_dir.get(key_name))
            changed = True

        key_name = 'price'
        if key_name in item_dir:
            setattr(item_order, key_name, item_dir.get(key_name))
            changed = True

        key_name = 'summ'
        if key_name in item_dir:
            setattr(item_order, key_name, item_dir.get(key_name))
            changed = True
        if changed:
            item_order.save()


def handle_order_list(order_list: None, author: None) -> List[Order]:
    orders_id = []
    with transaction.atomic():
        for order_item in order_list:
            order = handle_order(order_dir=order_item, author=author)
            orders_id.append(order.id)
    return Order.objects.filter(id__in=orders_id)


def handle_order_status_list(items_list: List) -> None:
    for item in items_list:
        order = order_by_id(item.get("id"))
        status = status_by_value(item.get("value"))
        put_order_status(order, status)
