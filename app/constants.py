TORTOISE_ORM = {
    "connections": {
        "master": "postgres://steve:testpassword@localhost/fastapi5",
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
        "master": "postgres://steve:testpassword@localhost/fastapi5",
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

