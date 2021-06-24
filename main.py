from neat import genome
import pygame
import os
import math
import random
import sys
import neat
import pickle

from Actors.Dinosaur import Dinosaur
from Actors.SmallCactus import SmallCactus
from Actors.LargeCactus import LargeCactus
from Actors.Bird import Bird

pygame.init()

from Constants import BACKGROUND, SMALL_CACTI, LARGE_CACTI, BIRD
from Constants import SCREEN_HEIGHT, SCREEN_WIDTH
from Constants import INITIAL_GAME_SPEED

# Initialise Screen
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Font Name
FONT = pygame.font.Font("freesansbold.ttf", 20)

def score():
    global points, game_speed
    points += 1
    if points % 100 == 0:
        game_speed += 1
    
    text_score = FONT.render(f'Points: {str(points)}', True, (0, 0, 0))
    SCREEN.blit(text_score, (950, 50))

def background():
    global x_pos_bg, y_pos_bg
    img_width = BACKGROUND.get_width()
    SCREEN.blit(BACKGROUND, (x_pos_bg, y_pos_bg))
    SCREEN.blit(BACKGROUND, (img_width + x_pos_bg, y_pos_bg))
    if x_pos_bg <= -img_width:
        x_pos_bg = 0
    x_pos_bg -= game_speed

def kill_player(player_index):
    players.pop(player_index)
    ge.pop(player_index)
    nets.pop(player_index)

def display_statistics():
    NUM_GENS = FONT.render(f'Generation: {pop.generation + 1}', True, (0, 0, 0))
    DINOS_ALIVE = FONT.render(f'Dinosaurs Alive: {len(players)}', True, (0, 0, 0))
    
    SCREEN.blit(NUM_GENS, (50, 450))
    SCREEN.blit(DINOS_ALIVE, (50, 480))

# Was previously our main function
def eval_genomes(genomes, config):

    global game_speed, x_pos_bg, y_pos_bg, obstacles, players, points, ge, nets
    clock = pygame.time.Clock()
    
    obstacles = []
    players = []
    ge = [] # List of dictionaries which contain information for each player (GE short for Genomes)
    nets = [] # List of Neural Network Objects for each player

    for genome_id, genome in genomes:
        players.append(Dinosaur())
        ge.append(genome)
        net = neat.nn.FeedForwardNetwork.create(genome, config) # Create a Neural Net based on genome and config
        nets.append(net)
        genome.fitness = 0

    # Initialise Some Global Variables
    game_speed = INITIAL_GAME_SPEED
    x_pos_bg = 0
    y_pos_bg = 380
    points = 0

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        SCREEN.fill((255, 255, 255)) # Fill screen with white

        for player in players:
            player.update()
            player.draw(SCREEN, obstacles)
        
        # If all players are dead then we end the game (or essentially if our one player dies)
        if (len(players)) == 0:
            break

        if (len(obstacles) == 0):
            randint = random.randint(0, 3) # Returns either 0 or 1 or 2 (33.33% chance)
            # Want to randomly spawn either a small cactus or a large cactus or a bird (crouching)
            if randint == 0:
                # Spawn any small cactus from the 3 images
                obstacles.append(SmallCactus(SMALL_CACTI))
            elif randint == 1:
                # Spawn any large cactus from the 3 images
                obstacles.append(LargeCactus(LARGE_CACTI))
            elif randint == 2:
                obstacles.append(Bird(BIRD))

        for obstacle in obstacles:
            obstacle.draw(SCREEN)
            obstacle.update(obstacles, game_speed)
            for i, player in enumerate(players): # Generates a list of tuples [(1, player1), (2, player2), ...]
                if player.rect.colliderect(obstacle.rect):
                    ge[i].fitness -= 1 # Decrease the fitness for each player that dies
                    kill_player(i)

        user_input = pygame.key.get_pressed()
        
        for i, player in enumerate(players):
            if len(obstacles) != 0:
                obstacle = obstacles[-1]
                output_val = nets[i].activate((player.rect.y, round(math.dist((player.rect.x, player.rect.y), obstacle.rect.midtop))))

                print(round(math.dist((player.rect.x, player.rect.y), obstacle.rect.midtop)))
                # If player is currently not jumping and neural net says to jump, then jump
                if output_val[0] > 0.5 and player.rect.y == player.Y_POS:
                    player.dino_jump = True
                    player.dino_crouch = False
                    player.dino_run = False
                
                elif output_val[1] > 0.5 and player.rect.y == player.Y_POS:
                    player.dino_crouch = True
                
                else:
                    player.dino_crouch = False

            """ if user_input[pygame.K_SPACE]:
                player.dino_jump = True
                player.dino_run = False """

        display_statistics()
        score()
        background()
        clock.tick(30)  
        pygame.display.update()


# Setup the NEAT AI
def run(config_path):
    global pop
    config = neat.config.Config(
        neat.DefaultGenome,
        neat.DefaultReproduction,
        neat.DefaultSpeciesSet,
        neat.DefaultStagnation,
        config_path
    )

    pop = neat.Population(config)
    best_genome = pop.run(eval_genomes, 20)

    # Want to save the best genome into a pickle object
    file_obj = open("best_model_genome.pkl", 'wb')
    pickle.dump(best_genome, file_obj)
    file_obj.close()

if __name__ == "__main__":
    local_dir = os.path.dirname(__file__) # Get the current directory of the file
    config_path = os.path.join(local_dir, 'config.txt')
    run(config_path)

    model_file = open("best_model_genome.pkl", 'rb')
    best_genome = pickle.load(model_file)
    model_file.close()

    eval_genomes([best_genome], config_path)
