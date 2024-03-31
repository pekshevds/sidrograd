from catalog_app.models import (
    Country,
    Good
)
from django.db import transaction
import csv


def load_data():
    with open("countries.csv", mode="+r", encoding="utf-8") as file:
        reader = csv.DictReader(file, fieldnames=[
            'barcode', 'country'], delimiter=';')

        with transaction.atomic():
            for row in reader:
                country_name = row['country'].upper().strip()
                good_art = row['barcode'].strip()
                country = Country.objects.filter(name=country_name).first()
                good = Good.objects.filter(art=good_art).first()
                if country and good:
                    good.country = country
                    good.save()
                # create(name=row['barcode'], code=row['country'])

"""def load_data():
    with open("oksm.csv", mode="+r", encoding="utf-8") as file:
        reader = csv.DictReader(file, fieldnames=[
            'name', 'code'], delimiter=';')

        with transaction.atomic():
            for row in reader:
                Country.objects.create(name=row['name'], code=row['code'])"""

if __name__ == "__main__":
    load_data()
