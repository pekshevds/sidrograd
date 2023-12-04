from django.urls import path
from cart_app.views import (
    CartView,
    CartAddView,
    CartDeleteView,
    CartClearView
)

app_name = 'cart_app'

urlpatterns = [
    path('', CartView.as_view(), name="list"),
    path('add/', CartAddView.as_view(), name="add"),
    path('delete/', CartDeleteView.as_view(), name="delete"),
    path('clear/', CartClearView.as_view(), name="clear"),
]
