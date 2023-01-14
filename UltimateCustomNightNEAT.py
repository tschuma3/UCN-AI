import neat
import numpy as np
import pygame
import os
import pickle
import random
from time import time
from datetime import datetime
pygame.font.init()

#Global Variables
GENERATION = 0

#Runs the main loop
def main(genomes, config):
    #Keeps track of generations and increments by 1
    global GENERATION
    GENERATION += 1
    
    #Set ups lists
    neural_Networks = [] #Keeps track of the neural networks
    genome = [] #Keeps track of the genome
    player = [] #Keeps track of the player/mouse

    #Keeps the neural networks, genome, and player together
    for ge_Id, ge in genomes:
        neural_Network = neat.nn.FeedForwardNetwork.create(ge, config) 
        neural_Networks.append(neural_Network)
        #  player.append(<--Something Goes Here-->)
        ge.fitness = 0
        genome.append(ge)
    pass

#Helps load the configuration file
def run(config_file):
    #Defining the subheadings from config-feedforward.txt
    config = neat.config.Config(neat.DefaultGenome, neat.DefaultReproduction,
                         neat.DefaultSpeciesSet, neat.DefaultStagnation,
                         config_file)
                        
    #Sets the population size
    p = neat.Population(config)

    #Showing the detailed report
    p.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    p.add_reporter(stats)

    #Uses the "main" function as the fitness function
    winner = p.run(main, 50)

    print("\nBest Genome: \n{!s}".format(winner))

#Helps load the configuration file
if __name__ == "__main__":
    local_dir = os.path.dirname(__file__) #Gets the file in the current folder
    config_path = os.path.join(local_dir, "config-feedforward.txt") #Gets the exact path
    run(config_path)