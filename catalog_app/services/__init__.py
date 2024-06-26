from typing import List
from django.db.models import QuerySet, Model


def object_by_id_list(_class: Model, id: List[str]) -> QuerySet:
    return _class.objects.filter(id__in=id)
