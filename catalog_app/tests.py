from django.test import TestCase
from catalog_app.models import Category
from catalog_app.services import (
    handle_object,
    handle_object_list
)
from random import choices
from string import printable


def generating_category_name():
    return choices(printable)


class CategoryTestCase(TestCase):
    def setUp(self) -> None:
        pass

    def test_creating_new_category(self) -> None:
        category_name = generating_category_name()
        new_category = Category.objects.create(name=category_name)
        found_category = Category.objects.get(name=category_name)
        self.assertEqual(found_category, new_category)

    def test_handle_object(self) -> None:
        obj = handle_object(Category, {
            "id": None,
            "name": "test1",
            "comment": "comment1"
            })
        # print(f"{obj.id} {obj.name} {obj.comment}")
        self.assertEqual(obj is None, False)

    def test_handle_object_list(self) -> None:
        queryset = handle_object_list(Category, [
            {
                "id": None,
                "name": "test1",
                "comment": "comment1"
            },
            {
                "id": None,
                "name": "test2",
                "comment": "comment2"
            },
            {
                "id": None,
                "name": "test3",
                "comment": "comment3"
            }
            ])
        # print(queryset)
        self.assertEqual(queryset is None, False)

# https://docs.djangoproject.com/en/4.2/topics/testing/overview/
