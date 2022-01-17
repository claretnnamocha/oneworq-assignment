from unicodedata import name
from sqlalchemy import true


swagger_template = {
    "swagger": "2.0",
    "info": {
        "title": "Oneworq Ecommerce API - Claret Nnamocha",
        "description": "Ecommerce API test for Oneworq",
        "contact": {
            "responsibleOrganization": "Oneworq",
            "responsibleDeveloper": "Claret Nnamocha",
            "email": "devclareo@gmail.com",
            "url": "https://claretnnamocha.com",
        },
        "version": "1.0",
    },
    "basePath": "/api",
    "schemes": ["http", "https"],
    "securityDefinitions": {
        "Bearer": {
            "type": "apiKey",
            "name": "Authorization",
            "in": "header",
            "description": 'JWT Authorization header using the Bearer scheme. Example: "Authorization: {token}"',
        }
    },
    "paths": {
        "/auth/sign-in": {
            "post": {
                "produces": ["application/json"],
                "tags": ["Authentication"],
                "responses": {
                    "200": {
                        "description": "Success",
                    }
                },
                "parameters": [
                    {
                        "in": "body",
                        "required": True,
                        "name": "request",
                        "schema": {
                            "$ref": "#/definitions/signIn",
                        },
                    }
                ],
            }
        },
        "/auth/sign-up": {
            "post": {
                "produces": ["application/json"],
                "tags": ["Authentication"],
                "responses": {
                    "200": {
                        "description": "Success",
                    }
                },
                "parameters": [
                    {
                        "in": "body",
                        "required": True,
                        "name": "request",
                        "schema": {
                            "$ref": "#/definitions/signUp",
                        },
                    }
                ],
            }
        },
        "/shop/item": {
            "get": {
                "produces": ["application/json"],
                "tags": ["Shop"],
                "responses": {
                    "200": {
                        "description": "Success",
                    }
                },
                "parameters": [
                    {
                        "name": "id",
                        "in": "query",
                        "required": True,
                        "type": "string",
                    }
                ],
            }
        },
        "/shop/item/search": {
            "get": {
                "produces": ["application/json"],
                "tags": ["Shop"],
                "responses": {
                    "200": {
                        "description": "Success",
                    }
                },
                "parameters": [
                    {
                        "in": "query",
                        "name": "q",
                        "type": "string",
                    },
                    # {
                    #     "in": "query",
                    #     "name": "categories",
                    #     "type": "string",
                    # },
                    {
                        "in": "query",
                        "name": "minPrice",
                        "type": "integer",
                    },
                    {
                        "in": "query",
                        "name": "maxPrice",
                        "type": "integer",
                    },
                    {
                        "in": "query",
                        "required": True,
                        "name": "page",
                        "type": "integer",
                        "default": 1,
                    },
                    {
                        "in": "query",
                        "required": True,
                        "name": "pageSize",
                        "type": "integer",
                        "default": 10,
                    },
                ],
            }
        },
        "/shop/item/create": {
            "post": {
                "produces": ["application/json"],
                "tags": ["Shop"],
                "responses": {
                    "200": {
                        "description": "Success",
                    }
                },
                "parameters": [
                    {
                        "in": "body",
                        "required": True,
                        "name": "request",
                        "schema": {
                            "$ref": "#/definitions/createItem",
                        },
                    }
                ],
            }
        },
        "/shop/item/update": {
            "put": {
                "produces": ["application/json"],
                "security": [{"Bearer": []}],
                "tags": ["Shop"],
                "responses": {
                    "200": {
                        "description": "Success",
                    }
                },
                "parameters": [
                    {
                        "in": "body",
                        "required": True,
                        "name": "request",
                        "schema": {
                            "$ref": "#/definitions/updateItem",
                        },
                    }
                ],
            }
        },
        "/shop/item/delete": {
            "delete": {
                "produces": ["application/json"],
                "tags": ["Shop"],
                "responses": {
                    "200": {
                        "description": "Success",
                    }
                },
                "parameters": [
                    {
                        "in": "body",
                        "required": True,
                        "name": "request",
                        "schema": {
                            "$ref": "#/definitions/getOne",
                        },
                    }
                ],
            }
        },
        "/shop/category": {
            "get": {
                "produces": ["application/json"],
                "tags": ["Shop"],
                "responses": {
                    "200": {
                        "description": "Success",
                    }
                },
                "parameters": [
                    {
                        "in": "query",
                        "required": True,
                        "name": "id",
                    }
                ],
            }
        },
        "/shop/category/search": {
            "get": {
                "produces": ["application/json"],
                "tags": ["Shop"],
                "responses": {
                    "200": {
                        "description": "Success",
                    }
                },
                "parameters": [
                    {
                        "in": "query",
                        "name": "q",
                        "type": "string",
                    },
                    {
                        "in": "query",
                        "required": True,
                        "name": "page",
                        "type": "integer",
                        "default": 1,
                    },
                    {
                        "in": "query",
                        "required": True,
                        "name": "pageSize",
                        "type": "integer",
                        "default": 10,
                    },
                ],
            }
        },
        "/shop/category/create": {
            "post": {
                "produces": ["application/json"],
                "tags": ["Shop"],
                "responses": {
                    "200": {
                        "description": "Success",
                    }
                },
                "parameters": [
                    {
                        "in": "body",
                        "required": True,
                        "name": "request",
                        "schema": {
                            "$ref": "#/definitions/createCat",
                        },
                    }
                ],
            }
        },
        "/shop/category/update": {
            "put": {
                "produces": ["application/json"],
                "security": [{"Bearer": []}],
                "tags": ["Shop"],
                "responses": {
                    "200": {
                        "description": "Success",
                    }
                },
                "parameters": [
                    {
                        "in": "body",
                        "required": True,
                        "name": "request",
                        "schema": {
                            "$ref": "#/definitions/updateCat",
                        },
                    }
                ],
            }
        },
        "/shop/category/delete": {
            "delete": {
                "produces": ["application/json"],
                "tags": ["Shop"],
                "responses": {
                    "200": {
                        "description": "Success",
                    }
                },
                "parameters": [
                    {
                        "in": "body",
                        "required": True,
                        "name": "request",
                        "schema": {
                            "$ref": "#/definitions/getOne",
                        },
                    }
                ],
            }
        },
    },
    "definitions": {
        "signIn": {
            "type": "object",
            "properties": {
                "email": {
                    "type": "string",
                    "required": True,
                },
                "password": {
                    "type": "string",
                    "required": True,
                },
            },
        },
        "signUp": {
            "type": "object",
            "properties": {
                "firstname": {
                    "type": "string",
                    "required": True,
                },
                "lastname": {
                    "type": "string",
                    "required": True,
                },
                "email": {
                    "type": "string",
                    "required": True,
                },
                "password": {
                    "type": "string",
                    "required": True,
                },
            },
        },
        "createItem": {
            "type": "object",
            "properties": {
                "title": {
                    "type": "string",
                    "required": True,
                },
                "description": {
                    "type": "string",
                    "required": True,
                },
                "categories": {
                    "type": "array",
                    "items": {"type": "string"},
                    "required": True,
                },
                "price": {
                    "type": "integer",
                    "required": True,
                },
            },
        },
        "createCat": {
            "type": "object",
            "properties": {
                "title": {
                    "type": "string",
                    "required": True,
                },
                "description": {
                    "type": "string",
                    "required": True,
                },
            },
        },
        "updateItem": {
            "type": "object",
            "properties": {
                "id": {
                    "type": "string",
                    "required": True,
                },
                "title": {"type": "string"},
                "description": {"type": "string"},
                "categories": {"type": "array", "items": {"type": "string"}},
                "price": {"type": "integer"},
            },
        },
        "updateCat": {
            "type": "object",
            "properties": {
                "id": {
                    "type": "string",
                    "required": True,
                },
                "title": {"type": "string"},
                "description": {"type": "string"},
            },
        },
        "getOne": {
            "type": "object",
            "properties": {
                "id": {"type": "string", "required": True},
            },
        },
    },
}

swagger_config = {
    "headers": [],
    "specs": [
        {
            "endpoint": "apispec_1",
            "route": "/apispec_1.json",
            "rule_filter": lambda rule: True,
            "model_filter": lambda rule: True,
        }
    ],
    "static_url_path": "/flasgger_static",
    "swagger_ui": True,
    "specs_route": "/api-docs",
}
