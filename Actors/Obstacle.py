import sys
sys.path.append("..\TestingNeat")

import random
from Constants import SCREEN_WIDTH

class Obstacle:
    def __init__(self, image):
        self.image = image
        self.type = random.randint(0, len(image) - 1)
        self.rect = self.image[self.type].get_rect()
        self.rect.x = SCREEN_WIDTH
    
    def update(self, obstacles, game_speed):
        self.rect.x -= game_speed
        if self.rect.x <= -self.rect.width:
            obstacles.pop()

    def draw(self, SCREEN):
        SCREEN.blit(self.image[self.type], self.rect)