import arrow
import asyncio

from db.db import loop

from services.database_service import insert
from db.documents.database import Database

"""
Kind of switch, returns full dico, but we use name from parameter to retrieve only one key we need
"""
def actions(name, params, description_positions) :
    return {
        'CREATE_DB': create_database(params=params, params_positions=description_positions)
    }[name]


def create_database(params, params_positions):
    db_name_schema = params[params_positions]
    now = arrow.utcnow().format('YYYY-MM-DDTHH:mm:ss.SSS')

    new_db_schema = Database(name=db_name_schema,
                             position_y=100,
                             position_x=100,
                             width=100,
                             height=100,
                             updated_at=now,
                             shape="rectangle")


    return loop.run_until_complete(insert(database_schema=new_db_schema.__dict__))
