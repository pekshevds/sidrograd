from dataclasses import dataclass
import hashlib
from django.db.models import Count


def secret_from_string(string: str) -> str:
    hash = hashlib.blake2s(digest_size=4)
    hash.update(string.encode('utf-8'))
    return hash.hexdigest()


def query_set(Class):
    @dataclass
    class Record:
        id: str
        name: str
        count: int

    categories = []
    qs = Class.objects.annotate(num_cat=Count("good", distinct=True))
    for _ in qs:
        if _.num_cat > 0:
            categories.append(
                Record(_.id, _.name, _.num_cat)
            )
    categories.sort(key=lambda obj: obj.count, reverse=True)
    return categories
