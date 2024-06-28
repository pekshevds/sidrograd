from django.db.models import QuerySet
from catalog_app.models import Manufacturer
from catalog_app.services import (
    object_by_id,
    object_by_id_list,
    handle_object,
    handle_object_list,
)


def manufacturer_by_id(manufacturer_id: str) -> Manufacturer:
    return object_by_id(Manufacturer, id=manufacturer_id)


def manufacturer_by_id_list(id: list[str]) -> QuerySet:
    return object_by_id_list(Manufacturer, ids=id)


def handle_manufacturer(manufacturer_dir: dict) -> Manufacturer:
    return handle_object(Manufacturer, object_dir=manufacturer_dir)


def handle_manufacturer_list(manufacturer_list: list[dict]) -> QuerySet:
    return handle_object_list(Manufacturer, object_list=manufacturer_list)
