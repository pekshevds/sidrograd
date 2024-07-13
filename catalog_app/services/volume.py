from django.db import transaction
from django.db.models import QuerySet
from catalog_app.models import Volume


def volume_by_id(item_id: str) -> Volume:
    return Volume.objects.filter(id=item_id).first()


def volume_by_id_list(id: list[str]) -> QuerySet[Volume]:
    return Volume.objects.filter(id__in=id)


def handle_volume(item_dict: dict) -> Volume:
    item_id = item_dict.get("id", "")
    item, _ = Volume.objects.get_or_create(id=item_id)
    item.name = item_dict.get("name", item.name)
    item.value = item_dict.get("value", item.value)
    item.save()
    return item


def handle_volume_list(item_list: list) -> QuerySet[Volume]:
    item_id = []
    with transaction.atomic():
        for item_dict in item_list:
            item = handle_volume(item_dict=item_dict)
            item_id.append(item.id)
    return Volume.objects.filter(id__in=item_id)
