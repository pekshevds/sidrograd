from catalog_app.models import (
    Country
)
from django.db import transaction
import csv


def load_data():
    with open("oksm.csv", mode="+r", encoding="utf-8") as file:
        reader = csv.DictReader(file, fieldnames=[
            'name', 'code'], delimiter=';')

        with transaction.atomic():
            for row in reader:
                Country.objects.create(name=row['name'], code=row['code'])


if __name__ == "__main__":
    load_data()
