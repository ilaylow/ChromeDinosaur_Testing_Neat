from .Obstacle import Obstacle

class LargeCactus(Obstacle):
    def __init__(self, image):
        super().__init__(image)
        self.rect.y = 300