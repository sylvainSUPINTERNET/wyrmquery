import uuid


# created_at => from ObjectId (timestamp)
class Common:
    uuid = uuid.uuid4()
    updated_at = ""
    shape = ""

    def __init__(self, updated_at, shape):
        self.updated_at = updated_at
        self.shape = shape
