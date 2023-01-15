import neat
import numpy as np
import pygame
import os
import pickle
import random
import pyautogui
from time import time
from datetime import datetime
import LearningTheAnimatronics
pygame.font.init()

"""
This program trains an ai to learn to play the game Ultimate Custom Night
"""


#Global Variables
GENERATION = 0

#Gets the screen width and height
SCREEN_WIDTH, SCREEN_HEIGHT = pyautogui.size()

#FNAF
#May not need this
FREDDY = []
CHICA = []
BONNIE = []
FOXY = []
GOLDEN_FREDDY = []
PHONE_GUY = []

#Takes care of the player
class Player:
    
    def __init__(self, x, y):
        self.x_Mouse = x
        self.y_Mouse = y

    #Finds the mouse position
    #May not need this
    def mouse_Position(self):
        pass

    #Allows the mouse to click in a certain x and y postion
    def click(self, x, y):
        pyautogui.click(x, y, button="left")

    #Presses the correct button
    def press_Key(self, key):
        pyautogui.keyDown(key)

#Takes care of the Animatronics
class Animatronics:

    def __init__(self, x, y, pixel_Color, animatronic_Knowledge):
        self.x = x
        self.y =  y
        self.pixel_Color = pixel_Color
        self.animatronic_Knowledge = animatronic_Knowledge

    #Finds the location of each animatronic
    def animatronic_Location(self, pixel_Color, animatronic_Knowledge):
        pass

    #What to do for each animatronic
    def animatronic_Defense(self, animatronic):

        #For Freddy

        #For Chica

        #For Bonnie

        #For Foxy

        #For Golden Freddy

        #For Phone Guy

        pass

#Runs the main loop
def main(self, genomes, config):
    #Keeps track of generations and increments by 1
    global GENERATION
    GENERATION += 1

    run = True

    #Sets the knowledge of each animatronic
    animatronic_Knowledge = LearningTheAnimatronics()

    #Set ups lists
    neural_Networks = [] #Keeps track of the neural networks
    genome = [] #Keeps track of the genome
    player = [] #Keeps track of the player/mouse

    #Keeps the neural networks, genome, and player together
    for ge_Id, ge in genomes:
        neural_Network = neat.nn.FeedForwardNetwork.create(ge, config) 
        neural_Networks.append(neural_Network)
        player.append(Player)
        ge.fitness = 0
        genome.append(ge)
    pass

    while run:
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