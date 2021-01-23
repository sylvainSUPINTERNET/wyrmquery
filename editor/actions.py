
"""
Kind of switch, returns full dico, but we use name from parameter to retrieve only one key we need
"""
def actions(name, params) :
    return {
        'CREATE_DB': create_database(params=params)
    }[name]


def create_database(params):
    return f"ok create db with name : {params}"