from django.urls import path
from api_app.views import (
    UserView,
    CategoryView,
    GoodView,
    ContractView,
    OrderView
)
from api_app.views import (
    WishListView,
    WishListAddView,
    WishListDeleteView,
    WishListClearView
)


app_name = 'api_app'

urlpatterns = [
    path('user/', UserView.as_view(), name="user"),
    path('category/', CategoryView.as_view(), name="category"),
    path('good/', GoodView.as_view(), name="good"),
    path('contract/', ContractView.as_view(), name="contract"),
    path('order/', OrderView.as_view(), name="order"),
    path('wish/', WishListView.as_view(), name="wish"),
    path('wish/add/', WishListAddView.as_view(), name="add"),
    path('wish/delete/', WishListDeleteView.as_view(), name="delete"),
    path('wish/clear/', WishListClearView.as_view(), name="clear"),
]
