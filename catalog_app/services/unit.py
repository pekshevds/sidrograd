from django.db import transaction
from catalog_app.models import (
    Unit
)


def unit_by_id(id: str) -> Unit:
    return Unit.objects.filter(id=id).first()


def unit_by_id_list(id: [str]) -> [Unit]:
    return list(Unit.objects.filter(id__in=id))


def handle_unit(item_dir: dir) -> Unit:
    item_id = item_dir.get('id', "")
    item = unit_by_id(id=item_id)
    if item is None:
        item = Unit.objects.create(
            id=item_id
        )
    item.name = item_dir.get('name', item.name)
    item.save()
    return item


def handle_unit_list(item_list: [dir]) -> [Unit]:
    items_id = []
    with transaction.atomic():
        for item_dir in item_list:
            item = handle_unit(item_dir=item_dir)
            items_id.append(item.id)
    return Unit.objects.filter(id__in=items_id)
