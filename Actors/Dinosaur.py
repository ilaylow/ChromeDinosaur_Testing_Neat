import pygame
import random

from Constants import CROUCHING, JUMPING, RUNNING

class Dinosaur:
    X_POS = 80
    Y_POS = 310
    JUMP_VEL = 8.5

    def __init__(self, img = RUNNING[0]):
        self.image = img
        self.dino_run = True
        self.dino_jump = False
        self.dino_crouch = False
        self.jump_vel = self.JUMP_VEL
        self.rect = pygame.Rect(self.X_POS, self.Y_POS, img.get_width(), img.get_height())
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.step_index = 0

    def update(self):
        if self.dino_run:
            self.run()
        if self.dino_jump:
            self.jump()
        if self.dino_crouch:
            self.crouch()
        if self.step_index >= 10:
            self.step_index = 0
    
    def jump(self):
        self.image = JUMPING
        if self.dino_jump:
            self.rect.y -= self.jump_vel * 4
            self.jump_vel -= 0.8
        if self.jump_vel <= -self.JUMP_VEL:
            self.dino_jump = False
            self.dino_run = True
            self.jump_vel = self.JUMP_VEL
    
    def crouch(self):
        self.image = CROUCHING
        self.rect.y += 10

    def run(self):
        self.image = RUNNING[self.step_index // 5]
        self.rect.x = self.X_POS
        self.rect.y = self.Y_POS
        self.step_index += 1
    
    def draw(self, SCREEN, obstacles):
        SCREEN.blit(self.image, (self.rect.x, self.rect.y))
        pygame.draw.rect(SCREEN, self.color, (self.rect.x, self.rect.y, self.rect.width, self.rect.height), 2)
        
        X_OFFSET = 54
        Y_OFFSET = 12
        # Draw line of sight for current player
        for obstacle in obstacles:
            pygame.draw.line(SCREEN, self.color, (self.rect.x + X_OFFSET, self.rect.y + Y_OFFSET), obstacle.rect.center, 2)