from .Obstacle import Obstacle

class Bird(Obstacle):
    def __init__(self, image):
        super().__init__(image)
        self.rect.y = 240

