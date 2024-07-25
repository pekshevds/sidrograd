from django.http import HttpRequest
from django.http.request import HttpHeaders
from rest_framework.authtoken.models import Token


def user_by_token_exist(request: HttpRequest) -> bool:
    key = key_from_headers(request.headers)
    try:
        Token.objects.get(key=key)
        return True
    except Token.DoesNotExist:
        return False


def key_from_headers(headers: HttpHeaders) -> str | None:
    auth = headers.get("Authorization")
    if auth:
        token_word, key = auth.split(" ")
        return key
    return None
