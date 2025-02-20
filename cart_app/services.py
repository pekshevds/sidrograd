from django.db.models import Model, QuerySet
from cart_app.models import Cart


def fetch_users_cart(user: Model) -> QuerySet:
    """Возвращает выборку элементов корзины пользователя user"""
    return user.cart_items.order_by("good__trade_mark__name", "good__volume__value")


def add_to_cart(user: Model, good: Model, quantity: float = 1) -> None:
    """Добавляет в корзину пользователя user элемент good"""
    record = Cart.objects.filter(user=user, good=good).first()
    if not record:
        Cart.objects.create(user=user, good=good, quantity=quantity)
    else:
        record.quantity += quantity
        record.save()


def delete_from_cart(user: Model, good: Model, quantity: float = 1) -> None:
    """Удаляет из корзины пользователя user элемент good"""
    record = Cart.objects.filter(user=user, good=good).first()
    if record:
        if quantity >= record.quantity:
            record.delete()
        else:
            record.quantity -= quantity
            record.save()


def set_quantity_into_cart(user: Model, good: Model, quantity: float = 1) -> None:
    """Удаляет из корзины пользователя user элемент good"""
    record = Cart.objects.filter(user=user, good=good).first()
    if record:
        record.quantity = quantity
        record.save()


def clear_cart(user: Model) -> None:
    """Очищает корзину пользователя user"""
    queryset = Cart.objects.filter(user=user)
    queryset.delete()
