from .Obstacle import Obstacle

class SmallCactus(Obstacle):
    def __init__(self, image):
        super().__init__(image)
        self.rect.y = 325

