from django.urls import path, include
from rest_framework.authtoken import views
from api_app.views import CallBackView, CheckMarkView


app_name = "api_app"

urlpatterns = [
    path("user/", include("auth_app.urls", namespace="auth_app")),
    path("catalog/", include("catalog_app.urls", namespace="catalog_app")),
    path("wish/", include("wish_list_app.urls", namespace="wish_list_app")),
    path("cart/", include("cart_app.urls", namespace="cart_app")),
    path("order/", include("order_app.urls", namespace="order_app")),
    path("call-back/", CallBackView.as_view(), name="call-back"),
    path("api-token-auth/", views.obtain_auth_token),
    path("check-mark/", CheckMarkView.as_view(), name="check-mark"),
]
