import asyncio
import os
# https://dev.to/svenvarkel/async-await-mongodb-in-python-25bk

from motor.motor_asyncio import AsyncIOMotorClient

uri = os.getenv('MONGO_DB_URL')
db_name = os.getenv('DB_NAME')

loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)

client = AsyncIOMotorClient(uri, io_loop=loop)


def get_client():
    return client.get_database(db_name)

