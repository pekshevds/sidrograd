from django.db import transaction
from catalog_app.models import (
    Volume
)


def volume_by_id(item_id: str) -> Volume:
    return Volume.objects.filter(id=item_id).first()


def volume_by_id_list(id: [str]) -> [Volume]:
    return list(Volume.objects.filter(id__in=id))


def handle_volume(item_dir: dir) -> Volume:
    item_id = item_dir.get('id', "")
    item_name = item_dir.get('name', "")
    item_value = item_dir.get('value', 0)
    item = volume_by_id(item_id)
    if item is None:
        item = Volume.objects.create(
            id=item_id,
            name=item_name,
            value=item_value
        )
    return item


def handle_volume_list(item_list: None) -> [Volume]:
    item_id = []
    with transaction.atomic():
        for item_dir in item_list:
            item = handle_volume(item_dir=item_dir)
            item_id.append(item.id)
    return Volume.objects.filter(id__in=item_id)
