from django.db.models import QuerySet
from catalog_app.models import Filtering
from catalog_app.services import (
    object_by_id,
    object_by_id_list,
    handle_object,
    handle_object_list,
)


def filtering_by_id(id: str) -> Filtering:
    return object_by_id(Filtering, id=id)


def filtering_by_id_list(id: list[str]) -> QuerySet:
    return object_by_id_list(Filtering, ids=id)


def handle_filtering(filtering_dir: dict) -> Filtering:
    return handle_object(Filtering, object_dir=filtering_dir)


def handle_filtering_list(filtering_list: list[dict]) -> QuerySet:
    return handle_object_list(Filtering, object_list=filtering_list)
