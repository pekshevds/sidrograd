from django.db.models import QuerySet
from catalog_app.models import Good


def fetch_all_goods() -> QuerySet[Good]:
    queryset = Good.objects.all()
    return queryset
