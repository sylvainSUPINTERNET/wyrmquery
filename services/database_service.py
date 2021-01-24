from db.db import get_client


async def insert(database_schema):
    result = await get_client().get_collection("databases").insert_one(database_schema)
    if result.inserted_id :
        return database_schema