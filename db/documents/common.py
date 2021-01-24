import uuid


# created_at => from ObjectId (timestamp)
class Common:
    uuid = ""
    updated_at = ""
    shape = ""

    def __init__(self, updated_at, shape):
        self.updated_at = updated_at
        self.shape = shape
        self.uuid = str(uuid.uuid4())
