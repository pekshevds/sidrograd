from typing import List
from django.db.models import QuerySet
from catalog_app.models import Gassing
from catalog_app.services import (
    object_by_id,
    object_by_id_list,
    handle_object,
    handle_object_list
)


def gassing_by_id(id: str) -> Gassing:
    return object_by_id(Gassing, id=id)


def gassing_by_id_list(id: List[str]) -> QuerySet:
    return object_by_id_list(Gassing, ids=id)


def handle_gassing(gassing_dir: dir) -> Gassing:
    return handle_object(Gassing, object_dir=gassing_dir)


def handle_gassing_list(gassing_list: None) -> QuerySet:
    return handle_object_list(Gassing, object_list=gassing_list)
