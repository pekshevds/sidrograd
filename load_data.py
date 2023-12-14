from catalog_app.models import Unit, Category, TradeMark, Good
from django.db import transaction
import csv


units = []
categories = []
trade_marks = []
goods = []


def find_good(art: str) -> Good:
    result = [item for item in goods if item.get("art", "") == art]
    if result:
        return result[0].get('obj')
    return None


def find(content: list[dict], target: str) -> object:
    result = [item for item in content if item.get("name", "") == target]
    if result:
        return result[0].get('obj')
    return None


def load_unit(name: str) -> Unit:
    obj = find(units, name)
    if not obj:
        obj = Unit.objects.create(name=name)
        units.append({
            'name': name,
            'obj': obj
        })
    return obj


def load_category(name: str) -> None:
    obj = find(categories, name)
    if not obj:
        obj = Category.objects.create(name=name)
        categories.append({
            'name': name,
            'obj': obj
        })
    return obj


def load_trade_mark(name: str) -> None:
    obj = find(trade_marks, name)
    if not obj:
        obj = TradeMark.objects.create(name=name)
        trade_marks.append({
            'name': name,
            'obj': obj
        })
    return obj


def load_data():
    with open("data.txt", mode="+r", encoding="utf-16") as file:
        reader = csv.DictReader(file, fieldnames=[
            'unit', 'price', 'strength',
            'volume', 'category', 'trade_mark',
            'art', 'name'], delimiter='\t')

        with transaction.atomic():
            is_first_row = True
            for row in reader:
                if is_first_row:
                    is_first_row = False
                    continue
                unit = load_unit(name=row['unit'])
                category = load_category(name=row['category'])
                trade_mark = load_trade_mark(name=row['trade_mark'])

                good = find_good(row['art'])
                if not good:
                    good = Good.objects.create(
                        name=row['name'],
                        art=row['art'],
                        price=float(row['price']
                                    .replace(',', '.').replace(' ', '')),
                        strength=float(row['strength']
                                       .replace(',', '.').replace(' ', '')),
                        volume=float(row['volume']
                                     .replace(',', '.').replace(' ', '')),
                        unit=unit,
                        category=category,
                        trade_mark=trade_mark
                    )
                    goods.append({
                        'art': row['art'],
                        'obj': good
                    })


if __name__ == "__main__":
    load_data()
