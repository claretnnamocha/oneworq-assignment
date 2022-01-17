signIn = {
    "email": {
        "required": True,
        "type": "string",
        "regex": "^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$",
    },
    "password": {"type": "string", "required": True},
}


signUp = {
    "email": {
        "required": True,
        "type": "string",
        "regex": "^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$",
    },
    "password": {
        "required": True,
        "type": "string",
        "regex": "^(?=.*[A-Z])+(?=.*[!@#$%^&*()\-__+.])+(?=.*[0-9])+(?=.*[a-z])+.{8,}$",
    },
    "firstname": {
        "required": True,
        "type": "string",
    },
    "lastname": {
        "required": True,
        "type": "string",
    },
}
