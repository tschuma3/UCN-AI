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
TIME = 0
TEMPERATURE = 0
NOISE_LEVEL = 0

#Gets the screen width and height
SCREEN_WIDTH, SCREEN_HEIGHT = pyautogui.size()

#Finds the animatronic's location
#Can locate the animatronic and click by using
#x, y = pyautogui.locateCenterOnScreen('.png')
#pyautogui.click(x, y)
ANIMATRONIC_LOCATION = pyautogui.locationOnScreen('.png', confidence=0.9) 

#FNAF
#May not need this
FREDDY = []
CHICA = []
BONNIE = []
FOXY = []
GOLDEN_FREDDY = []
PHONE_GUY = []
#FNAF World
OLD_MAN_CONSEQUENCES = []
DEE_DEE = []

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
        
        #Dictionary of all the keys
        key_Dictionary = {
            1: "Power Generator",
            2: "Silent Ventilation",
            3: "Heater",
            4: "Power AC",
            5: "Global Music Box",
            6: "All off",
            Z: "Flashlight",
            W: "Close Forward Vent",
            A: "Close Left Door",
            S: "Monitor",
            D: "Close Right Door",
            F: "Close Side Vent",
            C: "Catch Fish (Old Man Con.)",
            Enter: "Close Ad (El Chip)",
            Spacebar: "Toggle Desk Fan"
        }

        #Presses the right key
        if key_Dictionary.keys() == key:
            return pyautogui.keyDown(key)

    #What to do for each animatronic
    def animatronic_Defense(self, animatronic):

        #region FNAF

        #For Freddy
        #Location: Left side, Action: Shut the door, Tips: Hotter temperature causes him to move faster
        if animatronic == "Freddy":
            press_Key("A")

        #For Chica
        #Location: Kitchen, Action: Change the music box when she stops making noise

        #For Bonnie
        #Location: Cove, Action: Figure on the desk means no camera on cove

        #For Foxy
        #Location: Office, Action: , Tips: Will scare next time the monitor is brought up if all 4 pieces are in the office

        #Golden Freddy
        #Location: Office, Action: Move the Camera
        if animatronic == "Golden Freddy":
            x, y = pyautogui.locateCenterOnScreen(r'D:\GitHub Repos\UCN-AI\UCN Reference Images\Mask (Red Button).png', confidence=1)
            pyautogui.moveTo(x, y)

        #For Phone Guy
        #Location: Office, Action: Click the mute button, Tips: Wants to mute due to audio
        if pyautogui.locateOnScreen(r'D:\GitHub Repos\UCN-AI\UCN Reference Images\Phone Guy (Mute Button).png'):
            x, y = pyautogui.locateCenterOnScreen(r'D:\GitHub Repos\UCN-AI\UCN Reference Images\Phone Guy (Mute Button).png')
            pyautogui.click(x, y)

        #endregion

        #region FNAF 2



        #endregion
        
        #region FNAF 3


        
        #endregion

        #region FNAF 3



        #endregion

        #region FNAF 4



        #endregion

        #region FNAF World

        #For Old Man Consequences
        #Location: Office, Action: Catch the fish with "c" key
        elif animatronic == "Old Man Consequences":
            if pyautogui.locateOnScreen(r'D:\GitHub Repos\UCN-AI\UCN Reference Images\Old Man Consequences (Catching FIsh).png', confidence=0.9):
                press_Key("C")

        #For Dee Dee
        #Location: Office, Action: None, Tips: Adds a new animatronic

        #endregion

        #region FNAF: Sister Location



        #endregion

        #region FNAF: Pizzeria Simulator



        #endregion

        pass

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