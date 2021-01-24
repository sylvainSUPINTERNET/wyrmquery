from .common import Common


class Database(Common):
    name = ""
    position_x = 0
    position_y = 0
    width = 100
    height = 100

    def __init__(self, updated_at, shape, name, position_x, position_y, width, height):
        super().__init__(updated_at, shape)
        self.name = name
        self.position_x = position_x
        self.position_y = position_y
        self.width = width
        self.height = height
