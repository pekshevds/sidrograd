from django.urls import path
from catalog_app.views import (
    ManufacturerView,
    UnitView,
    FilteringView,
    # PasteurizationView,
    GassingView,
    TradeMarkView,
    CategoryView,
    GoodView,
    VolumeView,
    StrengthView,
    DataView,
    StyleView,
    TypeOfFermentationView,
    CountryView,
    PricesView,
    СarouselView,
    LoadGoodsView,
)


app_name = "catalog_app"

urlpatterns = [
    path("country/", CountryView.as_view(), name="country"),
    path("style/", StyleView.as_view(), name="style"),
    path(
        "type-of-fermentation/",
        TypeOfFermentationView.as_view(),
        name="type-of-fermentation",
    ),
    path("volume/", VolumeView.as_view(), name="volume"),
    path("strength/", StrengthView.as_view(), name="strength"),
    path("unit/", UnitView.as_view(), name="init"),
    path("manufacturer/", ManufacturerView.as_view(), name="manufacturer"),
    path("filtering/", FilteringView.as_view(), name="filtering"),
    # path('pasteurization/', PasteurizationView.as_view(), name="pasteurization"),
    path("gassing/", GassingView.as_view(), name="gassing"),
    path("trade-mark/", TradeMarkView.as_view(), name="trade-mark"),
    path("category/", CategoryView.as_view(), name="category"),
    path("good/", GoodView.as_view(), name="good"),
    path("data/", DataView.as_view(), name="data"),
    path("carousel/", СarouselView.as_view(), name="carousel"),
    path("prices/", PricesView.as_view(), name="prices"),
    path("upload-goods/", LoadGoodsView.as_view(), name="upload-goods"),
]
