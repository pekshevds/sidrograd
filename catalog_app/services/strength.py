from django.db import transaction
from catalog_app.models import (
    Strength
)


def strength_by_id(item_id: str) -> Strength:
    return Strength.objects.filter(id=item_id).first()


def strength_by_id_list(id: [str]) -> [Strength]:
    return list(Strength.objects.filter(id__in=id))


def handle_strength(item_dir: dir) -> Strength:
    item_id = item_dir.get('id', "")
    item_name = item_dir.get('name', "")
    item_value = item_dir.get('value', 0)
    item = strength_by_id(item_id)
    if item is None:
        item = Strength.objects.create(
            id=item_id,
            name=item_name,
            value=item_value
        )
    return item


def handle_strength_list(item_list: None) -> [Strength]:
    item_id = []
    with transaction.atomic():
        for item_dir in item_list:
            item = handle_strength(item_dir=item_dir)
            item_id.append(item.id)
    return Strength.objects.filter(id__in=item_id)
