from tortoise import Tortoise


async def setup_db():
    await Tortoise.init(
        db_url="postgres://reber:reber@db:5432/reber",
        modules={"models": ["models.__init__"]},
    )

    await Tortoise.generate_schemas()
