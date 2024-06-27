from typing import List
from django.db.models import QuerySet
from catalog_app.models import Category
from catalog_app.services import (
    object_by_id,
    object_by_id_list,
    handle_object,
    handle_object_list
)


def category_by_id(id: str) -> Category:
    return object_by_id(Category, id=id)


def category_by_id_list(id: List[str]) -> QuerySet:
    return object_by_id_list(Category, ids=id)


def handle_category(category_dir: dir) -> Category:
    handle_object(Category, object_dir=category_dir)


def handle_category_list(category_list: None) -> QuerySet:
    handle_object_list(Category, object_list=category_list)
