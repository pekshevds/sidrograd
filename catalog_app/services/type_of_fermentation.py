from django.db import transaction
from catalog_app.models import (
    TypeOfFermentation
)


def type_of_fermentation_by_id(id: str) -> TypeOfFermentation:
    return TypeOfFermentation.objects.filter(id=id).first()


def type_of_fermentation_by_id_list(id: [str]) -> [TypeOfFermentation]:
    return list(TypeOfFermentation.objects.filter(id__in=id))


def handle_type_of_fermentation(item_dir: dir) -> TypeOfFermentation:
    item_id = item_dir.get('id', "")
    item = type_of_fermentation_by_id(id=item_id)
    if item is None:
        item = TypeOfFermentation.objects.create(
            id=item_id
        )
    item.name = item_dir.get('name', item.name)
    item.save()
    return item


def handle_type_of_fermentation_list(item_list: [dir]) -> [TypeOfFermentation]:
    items_id = []
    with transaction.atomic():
        for item_dir in item_list:
            item = handle_type_of_fermentation(item_dir=item_dir)
            items_id.append(item.id)
    return TypeOfFermentation.objects.filter(id__in=items_id)
