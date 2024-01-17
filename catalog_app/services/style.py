from django.db import transaction
from catalog_app.models import (
    Style
)


def style_by_id(id: str) -> Style:
    return Style.objects.filter(id=id).first()


def style_by_id_list(id: [str]) -> [Style]:
    return list(Style.objects.filter(id__in=id))


def handle_style(item_dir: dir) -> Style:
    item_id = item_dir.get('id', "")
    item = style_by_id(id=item_id)
    if item is None:
        item = Style.objects.create(
            id=item_id
        )
    item.name = item_dir.get('name', item.name)
    item.save()
    return item


def handle_style_list(item_list: [dir]) -> [Style]:
    items_id = []
    with transaction.atomic():
        for item_dir in item_list:
            item = handle_style(item_dir=item_dir)
            items_id.append(item.id)
    return Style.objects.filter(id__in=items_id)
