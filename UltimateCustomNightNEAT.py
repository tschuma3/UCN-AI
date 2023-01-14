import neat
import numpy as np
import pygame
import os
import pickle
import random
from time import time
from datetime import datetime

#Runs the main loop
def main(genomes, config):
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