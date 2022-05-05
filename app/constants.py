DATABASE_URL = "postgres://steve:testpassword@localhost/fastapi6"
TORTOISE_ORM = {
    "connections": {
        "master": DATABASE_URL,
        # "slave": "postgres://steve:testpassword@localhost/fastapi2"
    },
    "apps": {
        "models": {
            # "models": ["__main__"],
            "models": ["aerich.models", "app.models"],
            "default_connection": "master",
        }
    },
    "use_tz": False,
    "timezone": "UTC",
}
TORTOISE_ORM_APP = {
    "connections": {
        "master": DATABASE_URL,
        # "slave": "postgres://steve:testpassword@localhost/fastapi2"
    },
    "apps": {
        "models": {
            # "models": ["__main__"],
            "models": ["aerich.models", "models"],
            "default_connection": "master",
        }
    },
    "use_tz": False,
    "timezone": "UTC",
}

