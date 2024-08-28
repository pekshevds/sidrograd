import hashlib
from django.db import models
from pytils.translit import slugify
from server.base import Directory
from image_app.models import Image
from catalog_app.services.good_events import after_save


def secret_from_string(string: str) -> str:
    hash = hashlib.blake2s(digest_size=4)
    hash.update(string.encode("utf-8"))
    return hash.hexdigest()


class Country(Directory):
    code = models.CharField(
        verbose_name="Код оп ОКСМ",
        max_length=3,
        blank=True,
        null=True,
        default="",
        db_index=True,
    )
    count = models.IntegerField(null=True, blank=True, default=0)

    class Meta:
        verbose_name = "Страна"
        verbose_name_plural = "Классификатор стран мира"
        ordering = ["name"]


class Category(Directory):
    image = models.ImageField(
        verbose_name="Файл изображения 570х570",
        upload_to="category_images/",
        blank=True,
        null=True,
    )
    order_by = models.SmallIntegerField(
        verbose_name="Порядок сортировки", null=True, blank=True, default=0
    )
    count = models.IntegerField(null=True, blank=True, default=0)

    class Meta:
        verbose_name = "Раздел каталога"
        verbose_name_plural = "Разделы каталога"
        ordering = ["order_by"]


class TradeMark(Directory):
    count = models.IntegerField(null=True, blank=True, default=0)

    class Meta:
        verbose_name = "Торговая марка"
        verbose_name_plural = "Торговые марки"
        ordering = ["name"]


class Gassing(Directory):
    count = models.IntegerField(null=True, blank=True, default=0)

    class Meta:
        verbose_name = "Газация"
        verbose_name_plural = "Виды газации"
        ordering = ["name"]


class Pasteurization(Directory):
    count = models.IntegerField(null=True, blank=True, default=0)

    class Meta:
        verbose_name = "Пастеризация"
        verbose_name_plural = "Виды пастеризации"
        ordering = ["name"]


class Filtering(Directory):
    count = models.IntegerField(null=True, blank=True, default=0)

    class Meta:
        verbose_name = "Фильрация"
        verbose_name_plural = "Виды фильтрации"
        ordering = ["name"]


class Manufacturer(Directory):
    count = models.IntegerField(null=True, blank=True, default=0)

    description = models.TextField(verbose_name="Описание", null=True, blank=True)

    class Meta:
        verbose_name = "Производитель"
        verbose_name_plural = "Производители"
        ordering = ["name"]


class Unit(Directory):
    count = models.IntegerField(null=True, blank=True, default=0)

    class Meta:
        verbose_name = "Единица измерения"
        verbose_name_plural = "Единицы измерения"
        ordering = ["name"]


class TypeOfFermentation(Directory):
    count = models.IntegerField(null=True, blank=True, default=0)

    class Meta:
        verbose_name = "Тип ферментации"
        verbose_name_plural = "Типы ферментации"
        ordering = ["name"]


class Style(Directory):
    count = models.IntegerField(null=True, blank=True, default=0)

    class Meta:
        verbose_name = "Спиль"
        verbose_name_plural = "Стили"
        ordering = ["name"]


class Volume(Directory):
    count = models.IntegerField(null=True, blank=True, default=0)
    value = models.DecimalField(
        verbose_name="Значение",
        max_digits=15,
        decimal_places=3,
        blank=True,
        null=True,
        default=0,
    )

    class Meta:
        verbose_name = "Объем, л"
        verbose_name_plural = "Классификатор объемов"
        ordering = ["value"]


class Strength(Directory):
    count = models.IntegerField(null=True, blank=True, default=0)
    value = models.DecimalField(
        verbose_name="Значение",
        max_digits=15,
        decimal_places=3,
        blank=True,
        null=True,
        default=0,
    )

    class Meta:
        verbose_name = "Крепость, %"
        verbose_name_plural = "Классификатор крепостей"
        ordering = ["value"]


class ActeveGoodManaget(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)


class Good(Directory):
    full_name = models.CharField(
        verbose_name="Наименование полное",
        max_length=1024,
        blank=True,
        null=True,
        default="",
    )
    art = models.CharField(
        verbose_name="Артикул",
        max_length=25,
        blank=True,
        null=True,
        default="",
        db_index=True,
    )
    balance = models.DecimalField(
        verbose_name="Остаток",
        max_digits=15,
        decimal_places=3,
        blank=True,
        null=True,
        default=0,
    )
    price = models.DecimalField(
        verbose_name="Цена",
        max_digits=15,
        decimal_places=2,
        blank=True,
        null=True,
        default=0,
    )
    volume = models.ForeignKey(
        Volume,
        on_delete=models.PROTECT,
        verbose_name="Объем, л",
        related_name="goods",
        blank=True,
        null=True,
    )
    strength = models.ForeignKey(
        Strength,
        on_delete=models.PROTECT,
        verbose_name="Крепость, %",
        related_name="goods",
        blank=True,
        null=True,
    )
    in_package = models.DecimalField(
        verbose_name="В упаковке, шт",
        max_digits=15,
        decimal_places=0,
        blank=True,
        null=True,
        default=0,
    )
    expiration_date = models.DecimalField(
        verbose_name="Срок годности, мес",
        max_digits=15,
        decimal_places=0,
        blank=True,
        null=True,
        default=0,
    )
    slug = models.SlugField(max_length=250, null=True, blank=True, unique=True)
    image = models.ForeignKey(
        Image,
        on_delete=models.PROTECT,
        verbose_name="Изображение (превью)",
        blank=True,
        null=True,
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
        verbose_name="Раздел каталога",
        related_name="goods",
        blank=True,
        null=True,
    )
    is_active = models.BooleanField(verbose_name="Активен", default=False)
    trade_mark = models.ForeignKey(
        TradeMark,
        on_delete=models.PROTECT,
        verbose_name="Торговая марка",
        related_name="goods",
        blank=True,
        null=True,
    )
    gassing = models.ForeignKey(
        Gassing,
        on_delete=models.PROTECT,
        verbose_name="Газация",
        related_name="goods",
        blank=True,
        null=True,
    )
    pasteurization = models.ForeignKey(
        Pasteurization,
        on_delete=models.PROTECT,
        verbose_name="Пастеризация",
        related_name="goods",
        blank=True,
        null=True,
        editable=False,
    )
    filtering = models.ForeignKey(
        Filtering,
        on_delete=models.PROTECT,
        verbose_name="Фильтрация",
        related_name="goods",
        blank=True,
        null=True,
    )
    manufacturer = models.ForeignKey(
        Manufacturer,
        on_delete=models.PROTECT,
        verbose_name="Производитель",
        related_name="goods",
        blank=True,
        null=True,
    )
    unit = models.ForeignKey(
        Unit,
        on_delete=models.PROTECT,
        verbose_name="Единица измерения",
        related_name="goods",
        blank=True,
        null=True,
    )
    type_of_fermentation = models.ForeignKey(
        TypeOfFermentation,
        on_delete=models.PROTECT,
        verbose_name="Тип ферментации",
        related_name="goods",
        blank=True,
        null=True,
    )
    style = models.ForeignKey(
        Style,
        on_delete=models.PROTECT,
        verbose_name="Стиль",
        related_name="goods",
        blank=True,
        null=True,
    )
    country = models.ForeignKey(
        Country,
        on_delete=models.PROTECT,
        verbose_name="Страна",
        related_name="goods",
        blank=True,
        null=True,
    )
    description = models.TextField(verbose_name="Описание", null=True, blank=True)

    objects = models.Manager()
    active_goods = ActeveGoodManaget()

    def save(self, *args, **kwargs) -> None:
        if not self.slug:
            self.slug = slugify(f"{self.name}-{secret_from_string(str(self.id))}")
        self.full_name = f"{self.category} {self.trade_mark} {self.name}"
        super().save(*args, **kwargs)
        if kwargs.get("update_count", True):
            after_save(self)

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
        ordering = ["trade_mark", "name"]


class GoodsImage(models.Model):
    good = models.ForeignKey(
        Good,
        on_delete=models.PROTECT,
        verbose_name="Номенклатура",
        related_name="images",
    )
    image = models.ForeignKey(
        Image, on_delete=models.PROTECT, verbose_name="Изображение"
    )

    class Meta:
        verbose_name = "Изображение"
        verbose_name_plural = "Изображения товара"
