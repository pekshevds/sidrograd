from catalog_app.models import Unit
import csv


def load_units():
    with open("data.txt", mode="+r", encoding="oem") as file:
        reader = csv.DictReader(file, fieldnames=[
            'unit', 'price', 'strength',
            'volume', 'category', 'trade_mark',
            'art', 'name'], delimiter=chr(112))
        for row in reader:
            print(row['unit'], float(row['art']))
