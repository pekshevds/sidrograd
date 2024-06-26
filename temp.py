from dataclasses import dataclass
from collections import Counter
from django.db.models import QuerySet
from catalog_app.models import Good


@dataclass
class Record:
    def __init__(self,
                 trade_mark: Counter, gassing: Counter, filtering: Counter,
                 manufacturer: Counter, unit: Counter, style: Counter,
                 type_of_fermentation: Counter, strength: Counter,
                 volume: Counter, country: Counter) -> None:
        self.trade_mark = trade_mark
        self.gassing = gassing
        self.filtering = filtering
        self.manufacturer = manufacturer
        self.unit = unit
        self.style = style
        self.type_of_fermentation = type_of_fermentation
        self.strength = strength
        self.volume = volume
        self.country = country


def fetch_filters_by_goods(goods: QuerySet) -> Record:

    data = Record(
        trade_mark=Counter(), gassing=Counter(), filtering=Counter(),
        manufacturer=Counter(), unit=Counter(), style=Counter(),
        type_of_fermentation=Counter(), strength=Counter(),
        volume=Counter(), country=Counter())

    for item in goods:
        if item.trade_mark:
            data.trade_mark[item.trade_mark] += 1
        if item.gassing:
            data.gassing[item.gassing] += 1
        if item.filtering:
            data.filtering[item.filtering] += 1
        if item.manufacturer:
            data.manufacturer[item.manufacturer] += 1
        if item.unit:
            data.unit[item.unit] += 1
        if item.style:
            data.style[item.style] += 1
        if item.type_of_fermentation:
            data.type_of_fermentation[item.type_of_fermentation] += 1
        if item.strength:
            data.strength[item.strength] += 1
        if item.volume:
            data.volume[item.volume] += 1
        if item.country:
            data.country[item.country] += 1
    return data


def run(n: int) -> None:
    data = fetch_filters_by_goods(Good.objects.all()[:n])
    print(data.trade_mark)
