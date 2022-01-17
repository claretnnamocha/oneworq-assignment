from src.helpers import pluck
from src.models import ItemCategory, ShopItem, db


def createItem(params):
    (categories, description, price, title, userId) = pluck(
        params, "categories", "description", "price", "title", "userId"
    )

    price = float(price)

    if price < 1:
        return {
            "status": False,
            "message": "Validation Error",
            "data": {"price": ["must be greater than 1"]},
        }

    categories = list(set(categories))

    shopItem = ShopItem(
        description=description,
        price=price,
        title=title,
        owner_id=userId,
        categories=categories,
    )

    db.session.add(shopItem)
    db.session.commit()

    return {
        "status": True,
        "message": "Product created",
    }


def getItem(params):
    (id,) = pluck(params, "id")
    shopItem = (
        ShopItem.query.filter_by(isDeleted=False)
        .filter_by(id=id, isDeleted=False)
        .first()
    )

    if not shopItem:
        return {
            "status": False,
            "message": "Product not found",
        }

    return {
        "status": True,
        "message": "Product details",
        "data": shopItem.serialize(),
    }


def searchItems(params):
    (q, minPrice, maxPrice, categories, page, pageSize) = pluck(
        params, "q", "minPrice", "maxPrice", "categories", "page", "pageSize"
    )

    items = ShopItem.query.filter_by(isDeleted=False)

    # todo: search with categories
    # categories = categories.split(",") if categories else []
    # categories = list(set([item.strip() for item in categories]))

    # if len(categories):
    #     items = items.filter(any(item in ShopItem.categories for item in categories))

    if q:
        items = items.filter(
            ShopItem.title.ilike(f"%{q}%") | ShopItem.description.ilike(f"%{q}%")
        )

    if minPrice:
        items = items.filter(ShopItem.price >= float(minPrice))

    if maxPrice:
        items = items.filter(ShopItem.price <= float(maxPrice))

    total = items.count()

    items = (
        items.order_by(ShopItem.createdAt.desc())
        .paginate(int(page), int(pageSize), error_out=False)
        .items
    )

    return {
        "status": True,
        "message": "Product details",
        "data": [item.serialize() for item in items],
        "metadata": {
            "total": total,
            "page": page,
            "pageSize": pageSize,
        },
    }


def updateItem(params):
    (id, categories, description, price, title) = pluck(
        params, "id", "categories", "description", "price", "title", "userId"
    )

    price = float(price)

    if price < 1:
        return {
            "status": False,
            "message": "Validation Error",
            "data": {"price": ["must be greater than 1"]},
        }

    item = (
        ShopItem.query.filter_by(isDeleted=False)
        .filter_by(id=id, isDeleted=False)
        .first()
    )

    if not item:
        return {
            "status": False,
            "message": "Product category not found",
        }

    item.description = description
    item.price = price
    item.title = title

    if categories:
        categories = categories.split(",")
        categories = [item.strip() for item in categories]
        item.categories = categories

    db.session.add(item)
    db.session.commit()

    return {
        "status": True,
        "message": "Product updated",
    }


def deleteItem(params):
    (id) = pluck(params, "id")

    itemCategory = ShopItem.query.filter_by(isDeleted=False).filter_by(
        id=id, isDeleted=False
    )

    if not itemCategory:
        return {
            "status": False,
            "message": "Product category not found",
        }

    itemCategory.isDeleted = True

    db.session.add(itemCategory)
    db.session.commit()

    return {
        "status": True,
        "message": "Product category deleted",
    }


def createCategory(params):
    (description, title) = pluck(params, "description", "title")

    itemCategory = ItemCategory(description=description, title=title)

    db.session.add(itemCategory)
    db.session.commit()

    return {
        "status": True,
        "message": "Product category created",
    }


def getCategory(params):
    (id,) = pluck(params, "id")

    print("id", id)

    itemCategory = ItemCategory.query.filter_by(
        id=id,
    ).first()

    if not itemCategory:
        return {
            "status": False,
            "message": "Product Category not found",
        }

    return {
        "status": True,
        "message": "Product Category details",
        "data": itemCategory.serialize(),
    }


def searchCategories(params):
    (q, page, pageSize) = pluck(params, "q", "page", "pageSize")

    categories = ItemCategory.query

    if q:
        categories = categories.filter(
            ItemCategory.title.ilike(f"%{q}%")
            | ItemCategory.description.ilike(f"%{q}%")
        )

    total = categories.count()

    categories = (
        categories.order_by(ItemCategory.createdAt.desc())
        .paginate(int(page), int(pageSize), error_out=False)
        .items
    )

    return {
        "status": True,
        "message": "Product categories",
        "data": [item.serialize() for item in categories],
        "metadata": {
            "total": total,
            "page": page,
            "pageSize": pageSize,
        },
    }


def updateCategory(params):
    (id, description, title) = pluck(params, "id", "description", "title")

    itemCategory = ItemCategory.query.filter_by(id=id, isDeleted=False).first()

    if not itemCategory:
        return {
            "status": False,
            "message": "Product category not found",
        }

    itemCategory.description = description
    itemCategory.title = title

    db.session.add(itemCategory)
    db.session.commit()

    return {
        "status": True,
        "message": "Product category updated",
    }


def deleteCategory(params):
    (id) = pluck(params, "id")

    itemCategory = ItemCategory.query.filter_by(id=id, isDeleted=False)

    if not itemCategory:
        return {
            "status": False,
            "message": "Product category not found",
        }

    itemCategory.isDeleted = True

    db.session.add(itemCategory)
    db.session.commit()

    return {
        "status": True,
        "message": "Product category deleted",
    }
