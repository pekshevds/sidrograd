from catalog_app.models import (
    Unit,
    Category,
    TradeMark,
    Good,
    Volume,
    Strength,
    Country,
)

# from django.db import transaction
from decimal import Decimal
import csv


def load_data() -> None:
    with open("data1.csv", mode="+r", encoding="utf-8") as file:
        reader = csv.DictReader(
            file,
            fieldnames=[
                "unit",
                "art",
                "country",
                "strength",
                "volume",
                "category",
                "trade_mark",
                "name",
            ],
            delimiter=";",
        )
        is_first_row = True
        for row in reader:
            if is_first_row:
                is_first_row = False
                continue
            unit, _ = Unit.objects.get_or_create(name=row["unit"])
            volume, _ = Volume.objects.get_or_create(
                name=row["volume"], value=Decimal(row["volume"].replace(",", "."))
            )
            country, _ = Country.objects.get_or_create(name=row["country"])
            trade_mark, _ = TradeMark.objects.get_or_create(name=row["trade_mark"])
            strength, _ = Strength.objects.get_or_create(
                name=row["strength"], value=Decimal(row["strength"].replace(",", "."))
            )
            category, _ = Category.objects.get_or_create(name=row["category"])
            good, _ = Good.objects.get_or_create(art=row["art"])
            good.name = row["name"]
            good.unit = unit
            good.country = country
            good.volume = volume
            good.trade_mark = trade_mark
            good.strength = strength
            good.category = category
            good.save()
            print(unit)


if __name__ == "__main__":
    load_data()
