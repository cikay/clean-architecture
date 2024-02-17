from tortoise import Tortoise


async def setup_db():
    await Tortoise.init(
        config={
            "connections": {
                "default": {
                    "engine": "tortoise.backends.asyncpg",
                    "credentials": {
                        "host": "db",
                        "port": "5432",
                        "user": "reber",
                        "password": "reber",
                        "database": "reber",
                    },
                },
            },
            "apps": {
                "my_app": {
                    "models": ["models.__init__"],
                    "default_connection": "default",
                }
            },
            "use_tz": False,
        },
    )

    await Tortoise.generate_schemas()
