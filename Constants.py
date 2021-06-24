import pygame
import os
# Screen Constants

SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100

# Dino Path
DINO_PATH = "Assets/Player"

# Other Path
OTHER_PATH = "Assets/Other"

# Obstacle Path
CACTI_PATH = "Assets/Cactus"

# Bird Path
BIRD_PATH = "Assets/Bird"

# Initial Game Speed (Basically how fast the Dinosaur moves)
INITIAL_GAME_SPEED = 20

# Load in Background
BACKGROUND = pygame.image.load(os.path.join(OTHER_PATH, "Track.png"))

# Load in Running Images
RUNNING = (pygame.image.load(os.path.join(DINO_PATH, "DinoRun1.png")),
           pygame.image.load(os.path.join(DINO_PATH, "DinoRun2.png")))

# Load in Jumping Images
JUMPING = pygame.image.load(os.path.join(DINO_PATH, "DinoJump.png"))

# Load in Crouching Images
CROUCHING = pygame.image.load(os.path.join(DINO_PATH, "DinoCrouch.png"))

# Load in Obstacles (Cacti) Images
SMALL_CACTI = [pygame.image.load(os.path.join(CACTI_PATH, "SmallCactus1.png")),
               pygame.image.load(os.path.join(CACTI_PATH, "SmallCactus2.png")),
               pygame.image.load(os.path.join(CACTI_PATH, "SmallCactus3.png"))]

LARGE_CACTI = [pygame.image.load(os.path.join(CACTI_PATH, "LargeCactus1.png")),
               pygame.image.load(os.path.join(CACTI_PATH, "LargeCactus2.png")),
               pygame.image.load(os.path.join(CACTI_PATH, "LargeCactus3.png"))]

BIRD = [pygame.image.load(os.path.join(BIRD_PATH, "Bird1.png"))]