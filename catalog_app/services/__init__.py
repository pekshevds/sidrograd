from typing import List
from django.db.models import QuerySet, Model
from django.db import transaction


def object_by_id(_class, id: str) -> Model:
    return _class.objects.filter(id=id).first()


def object_by_id_list(_class, ids: List[str]) -> QuerySet:
    return _class.objects.filter(id__in=ids)


def handle_object(_class, object_dir: dir) -> Model:
    key_list = ["name", "comment"]
    obj, created = _class.objects.get_or_create(id=object_dir.get("id"))
    for key in key_list:
        if hasattr(obj, key):
            setattr(obj, key, getattr(obj, key) or object_dir.get(key))
    obj.save()
    return obj


def handle_object_list(_class, object_list: List[dir]) -> QuerySet:
    ids = []
    with transaction.atomic():
        for object_item in object_list:
            obj = handle_object(_class, object_dir=object_item)
            ids.append(obj.id)
    return object_by_id_list(_class, ids=ids)
