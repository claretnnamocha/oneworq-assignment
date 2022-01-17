from flask import Blueprint, request
from src.middlewares import authenticate, controller, validate
from src.modules.shop import service, validators

routes = Blueprint("shop", __name__, url_prefix="/shop")
itemRoutes = Blueprint("item", __name__, url_prefix="/item")
categoryRoutes = Blueprint("category", __name__, url_prefix="/category")


@itemRoutes.get("/search")
@validate(validators.searchShopItems)
@controller
def searchItems():
    return service.searchItems(request.form)


@itemRoutes.get("")
@validate(validators.getOne)
@controller
def getItem():
    return service.getItem(request.form)


@itemRoutes.post("/create")
@authenticate
@validate(validators.createShopItem)
@controller
def createItem():
    return service.createItem(request.form)


@itemRoutes.put("/update")
@authenticate
@validate(validators.updateShopItem)
@controller
def updateItem():
    return service.updateItem(request.form)


@itemRoutes.delete("/delete")
@authenticate
@validate(validators.getOne)
@controller
def deleteItem():
    return service.deleteItem(request.form)


@categoryRoutes.get("/search")
@validate(validators.searchItemCategories)
@controller
def searchCategories():
    return service.searchCategories(request.form)


@categoryRoutes.get("")
@validate(validators.getOne)
@controller
def getCategory():
    return service.getCategory(request.form)


@categoryRoutes.post("/create")
@authenticate
@validate(validators.createItemCategory)
@controller
def createCategory():
    return service.createCategory(request.form)


@categoryRoutes.put("/update")
@authenticate
@validate(validators.updateItemCategory)
@controller
def updateCategory():
    return service.updateCategory(request.form)


@categoryRoutes.delete("/delete")
@authenticate
@validate(validators.getOne)
@controller
def deleteCategory():
    return service.deleteCategory(request.form)


routes.register_blueprint(itemRoutes)
routes.register_blueprint(categoryRoutes)
