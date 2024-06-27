def before_save(good):
    pass


def after_save(good):
    if good.category:
        good.category.count = good.category.goods.count()
        good.category.save()

    if good.volume:
        good.volume.count = good.volume.goods.count()
        good.volume.save()

    if good.strength:
        good.strength.count = good.strength.goods.count()
        good.strength.save()

    if good.trade_mark:
        good.trade_mark.count = good.trade_mark.goods.count()
        good.trade_mark.save()

    if good.gassing:
        good.gassing.count = good.gassing.goods.count()
        good.gassing.save()

    if good.pasteurization:
        good.pasteurization.count = good.pasteurization.goods.count()
        good.pasteurization.save()

    if good.filtering:
        good.filtering.count = good.filtering.goods.count()
        good.filtering.save()

    if good.manufacturer:
        good.manufacturer.count = good.manufacturer.goods.count()
        good.manufacturer.save()

    if good.unit:
        good.unit.count = good.unit.goods.count()
        good.unit.save()

    if good.type_of_fermentation:
        good.type_of_fermentation.count = good.type_of_fermentation.goods.count()
        good.type_of_fermentation.save()

    if good.style:
        good.style.count = good.style.goods.count()
        good.style.save()

    if good.country:
        good.country.count = good.country.goods.count()
        good.country.save()
