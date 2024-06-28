from django.db.models import QuerySet
from catalog_app.models import Country
from catalog_app.services import (
    object_by_id,
    object_by_id_list,
    handle_object,
    handle_object_list,
)


def country_by_id(id: str) -> Country:
    return object_by_id(Country, id=id)


def country_by_id_list(id: list[str]) -> QuerySet:
    return object_by_id_list(Country, ids=id)


def handle_country(country_dir: dict) -> Country:
    return handle_object(Country, object_dir=country_dir)


def handle_country_list(country_list: list[dict]) -> QuerySet:
    return handle_object_list(Country, object_list=country_list)
