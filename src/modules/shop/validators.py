searchShopItems = {
    "q": {
        "type": "string",
        "minlength": 4,
    },
    "categories": {
        "type": "string",
    },
    "minPrice": {"type": "string", "regex": "\d+"},
    "maxPrice": {"type": "string", "regex": "\d+"},
    "page": {
        "type": "string",
        "required": True,
        "regex": "^[0-9]+$",
        "default": "1",
    },
    "pageSize": {
        "type": "string",
        "required": True,
        "regex": "^[0-9]+$",
        "default": "10",
    },
}


searchItemCategories = {
    "q": {
        "type": "string",
        "minlength": 5,
    },
    "page": {
        "type": "string",
        "required": True,
        "regex": "^[0-9]+$",
        "default": "1",
    },
    "pageSize": {
        "type": "string",
        "required": True,
        "regex": "^[0-9]+$",
        "default": "10",
    },
}


createItemCategory = {
    "title": {
        "type": "string",
        "required": True,
    },
    "description": {
        "type": "string",
        "required": True,
    },
}


createShopItem = {
    "title": {
        "type": "string",
        "required": True,
    },
    "description": {
        "type": "string",
        "required": True,
    },
    "categories": {
        "type": "list",
        "schema": {"type": "integer"},
        "required": True,
    },
    "price": {
        "type": "number",
        "required": True,
    },
}


updateItemCategory = {
    "id": {
        "type": "string",
        "required": True,
        "regex": "^[0-9]+$",
    },
    "title": {
        "type": "string",
    },
    "description": {
        "type": "string",
    },
}


updateShopItem = {
    "id": {
        "type": "string",
        "required": True,
        "regex": "^[0-9]+$",
    },
    "title": {
        "type": "string",
    },
    "description": {
        "type": "string",
    },
    "categories": {
        "type": "list",
        "schema": {"type": "number"},
    },
    "price": {
        "type": "string",
        "required": True,
        "regex": "^(0|([1-9][0-9]*))(\\.[0-9]+)?$",
    },
}


getOne = {
    "id": {
        "type": "string",
        "required": True,
        "regex": "^[0-9]+$",
    },
}
