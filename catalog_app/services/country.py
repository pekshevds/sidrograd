from django.db import transaction
from catalog_app.models import (
    Country
)


def country_by_id(id: str) -> Country:
    return Country.objects.filter(id=id).first()


def country_by_id_list(id: [str]) -> [Country]:
    return list(Country.objects.filter(id__in=id))


def handle_country(item_dir: dir) -> Country:
    item_id = item_dir.get('id', "")
    item = country_by_id(id=item_id)
    if item is None:
        item = Country.objects.create(
            id=item_id
        )
    item.name = item_dir.get('name', item.name)
    item.code = item_dir.get('code', "")
    item.save()
    return item


def handle_country_list(item_list: [dir]) -> [Country]:
    items_id = []
    with transaction.atomic():
        for item_dir in item_list:
            item = handle_country(item_dir=item_dir)
            items_id.append(item.id)
    return Country.objects.filter(id__in=items_id)
