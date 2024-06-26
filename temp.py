from dataclasses import dataclass
from collections import namedtuple
from django.db.models import QuerySet
from catalog_app.models import Good


@dataclass
class Record:
    id: str
    name: str
    count: int


def fetch_filters_by_goods(goods: QuerySet) -> namedtuple:
    data = namedtuple(
        "Data",
        [
            "trade_mark", "gassing",
            "filtering", "manufacturer", "unit",
            "style", "type_of_fermentation", "strength",
            "volume", "country"
        ],
        defaults=[]
    )
    for item in goods:
        item.trade_mark
        data.trade_mark
    return data
