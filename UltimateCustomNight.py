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

#Dictionary of all the animatronics with their names as elements
#May not need this
animatronics = {
#FNAF
Freddy: "Freddy",
Chica: "Chica",
Bonnie: "Bonnie",
Foxy: "Foxy",
Golden_Freddy: "Golden_Freddy",
Phone_Guy: "Phone_Guy",
#FNAF 2
Toy_Freddy: "Toy_Freddy",
Toy_Chica: "Toy_Chica",
Toy_Bonnie: "Toy_Bonnie",
Mangle: "Mangle",
Marionette: "Marionette",
BB: "BB",
JJ: "JJ",
Withered_Chica: "Withered_Chica",
Withered_Bonnie: "Withered_Bonnie",
#FNAF 3
Nightmare_Freddy: "Nightmare_Freddy",
Nightmare_Chica: "Nightmare_Chica",
Nightmare_Bonnie: "Nightmare_Bonnie",
Nightmare_Mangle: "Nightmare_Mangle",
Nightmare_Marionette: "Nightmare_Marionette",
Nightmare_BB: "Nightmare_BB",
Nightmare_Fredbear: "Nightmare_Fredbear",
Phantom_Freddy: "Phantom_Freddy",
Phantom_Mangle: "Phantom_Mangle",
Phantom_BB: "Phantom_BB",
Springtrap: "Springtrap",
Plushtrap: "Plushtrap",
#FNAF World
Old_Man_Consequences: "Old_Man_Consequences",
Dee_Dee: "Dee_Dee",
#FNAF: Sister Location
Funtime_Foxy: "Funtime_Foxy",
Baby: "Baby",
Ballora: "Ballora",
Minireena: "Minireena",
Bonnet: "Bonnet",
Lolbit: "Lolbit",
Ennard: "Ennard",
#FNAF: Pizzeria Simulator
Rockstar_Freddy: "Rockstar_Freddy",
Rockstar_Chica: "Rockstar_Chica",
Rockstar_Bonnie: "Rockstar_Bonnie",
Happy_Frog: "Happy_Frog",
Mr_Hippo: "Mr_Hippo",
Pig_Patch: "Pig_Patch",
Nedd_Bear: "Nedd_Bear",
Orville_Elephant: "Orville_Elephant",
Helpy: "Helpy",
Lefty: "Lefty",
El_Chip: "El_Chip",
Trash_and_the_Gang: "Trash_and_the_Gang",
Molten_Freddy: "Molten_Freddy",
Funtime_Chica: "Funtime_Chica",
Shadow_Bonnie: "Shadow_Bonnie",
Scrap_Baby: "Scrap_Baby",
Fredbear: "Fredbear",
William_Afton: "William_Afton"
}
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
    #May not need this function
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
            Spacebar: "Toggle Desk Fan",
            L: "LoL",
            O: "lOl"
        }
        #Dictionary of all the cameras
        camera_Dictionary = {
            Cam1: r"D:\GitHub Repos\UCN-AI\UCN Reference Images\Camera Up Images\Cam1.png",
            Cam2: r"D:\GitHub Repos\UCN-AI\UCN Reference Images\Camera Up Images\Cam2.png",
            Cam3: r"D:\GitHub Repos\UCN-AI\UCN Reference Images\Camera Up Images\Cam3.png",
            Cam4: r"D:\GitHub Repos\UCN-AI\UCN Reference Images\Camera Up Images\Cam4.png",
            Cam5: r"D:\GitHub Repos\UCN-AI\UCN Reference Images\Camera Up Images\Cam5.png",
            Cam6: r"D:\GitHub Repos\UCN-AI\UCN Reference Images\Camera Up Images\Cam6.png",
            Cam7: r"D:\GitHub Repos\UCN-AI\UCN Reference Images\Camera Up Images\Cam7.png",
            Cam8: r"D:\GitHub Repos\UCN-AI\UCN Reference Images\Camera Up Images\Cam8.png"
        }
        RedBlue_Button = {
            CamSystem: r"D:\GitHub Repos\UCN-AI\UCN Reference Images\Camera Up Images\CamSystem.png",
            DuctSystem: r"D:\GitHub Repos\UCN-AI\UCN Reference Images\Camera Up Images\DuctSystem.png",
            VentSystem: r"D:\GitHub Repos\UCN-AI\UCN Reference Images\Camera Up Images\VentSystem.png",
            ResetVentilation: r"D:\GitHub Repos\UCN-AI\UCN Reference Images\Camera Up Images\ResetVentilation.png"
        }

        #Presses the right key
        if key_Dictionary.keys() == key:
            if key != "S":
                return pyautogui.keyDown(key)
            else:
                pyautogui.keyDown(key)
                x, y = pyautogui.locateCenterOnScreen(camera_Dictionary[key])
                pyautogui.click(x, y)

        #Center mouse
        pyautogui.moveTo(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    #What to do for each animatronic
    def animatronic_Defense(self, animatronic): #<-- May add location and action as parameters

        #region FNAF

        #For Freddy
        #Location: Left side, Action: Shut the door, Tips: Hotter temperature causes him to move faster
        if animatronic == "Freddy":
            press_Key("A")

        #For Chica
        #Location: Kitchen, Action: Change the music box when she stops making noise
        elif animatronic == "Chica":
            press_Key("S")

        #For Bonnie
        #Location: Cove / Cam 5, Action: Figure on the desk means no camera on cove
        elif animatronic == "Bonnie":
            pass

        #For Foxy
        #Location: Office, Action: , Tips: Will scare next time the monitor is brought up if all 4 pieces are in the office
        elif animatronic == "Foxy":
            pass

        #Golden Freddy
        #Location: Office, Action: Move the Camera
        elif animatronic == "Golden Freddy":
            x, y = pyautogui.locateCenterOnScreen(r'D:\GitHub Repos\UCN-AI\UCN Reference Images\Mask (Red Button).png', confidence=1)
            pyautogui.moveTo(x, y)

        #For Phone Guy
        #Location: Office, Action: Click the mute button, Tips: Wants to mute due to audio
        elif pyautogui.locateOnScreen(r'D:\GitHub Repos\UCN-AI\UCN Reference Images\Phone Guy (Mute Button).png'):
            x, y = pyautogui.locateCenterOnScreen(r'D:\GitHub Repos\UCN-AI\UCN Reference Images\Phone Guy (Mute Button).png')
            pyautogui.click(x, y)

        #endregion

        #region FNAF 2

        #For BB
        #Location: Side Vent, Action: Shut the vent, Tips: If in then he will disable the flashlight
        if animatronic == "BB":
            press_Key("F")

        #For JJ
        #Location: Side Vent, Action: Shut the vent, Tips: If in then she will disable the doors
        if animatronic == "JJ":
            press_Key("F")

        #For Marionette
        #Location: Office, Action: Wind the music box, Tips: If escape then the ventalation drains faster
        if animatronic == "Marionette":
            press_Key("5")

        #For Mangle
        #Location: Vent, Action: Vent Snare, Tips: Wont leave once she arrives
        if animatronic == "Mangle":
            pass

        #For Toy Freddy
        #Location: Parts and Services / Cam 8, Action: Click the cameras on Freddy's screen, Tips: Don't let Mr. Hugs into Freddy's office
        if animatronic == "Toy Freddy":
            pass

        #For Toy Chica
        #Location: Office, Action: Flip the Mask on and look directly at, Tips: Enters on the left and is faster than Toy Bonnie
        if animatronic == "Toy Chica":
            x , y = pyautogui.locateCenterOnScreen(r'D:\GitHub Repos\UCN-AI\UCN Reference Images\Mask (Red Button).png')
            pyautogui.moveTo(x, y)
        
        #For Toy Bonnie
        #Location: Office, Action: Flip the mask on and look directly at, Tips: Enters through the right trapdoor
        if animatronic == "Toy Bonnie":
            x , y = pyautogui.locateCenterOnScreen(r'D:\GitHub Repos\UCN-AI\UCN Reference Images\Mask (Red Button).png')
            pyautogui.moveTo(x, y)

        #For Whithered Chica
        #Location: Vent, Action: Vent Snare and Door, Tips: She can get stuck in the vent door preventing Ennard, Molten Freddy and Springtrap from entering
        if animatronic == "Whithered Chica":
            pass

        #For Whithered Bonnie
        #Location: Office, Action: Flip the mask on after, Tips: Has audio cues and attacks when fliping down the camera
        if animatronic == "Whithered Bonnie":
            x , y = pyautogui.locateCenterOnScreen(r'D:\GitHub Repos\UCN-AI\UCN Reference Images\Mask (Red Button).png')
            pyautogui.moveTo(x, y)

        #endregion
        
        #region FNAF 3

        #For Phantom Freddy
        #Location: Office, Action: Shine flashlight on him, Tips:
        elif animatronic == "Phantom Freddy":
            press_Key("Z")

        #For Phantom Mangle
        #Location: Monitor, Action: Close the monitor, Tips: Will make noise in the office
        elif animatronic == "Phantom Mangle":
            pass

        #For Phantom BB
        #Location: Monitor, Action: CLose or change camera, Tips:
        elif animatronic == "Phantom BB":
            pass

        #For Springtrap
        #Location: Front Vent, Action: Close Front Vent, Tips:
        elif animatronic == "Springtrap":
            press_Key("W")

        #endregion

        #region FNAF 4

        #For Nightmare Freddy
        #Location: Office, Action: Shine flashlight on him, Tips:
        if animatronic == "Nightmare Freddy":
            press_Key("Z")

        #For Nightmare Chica
        #Location: Slowly approaches, Action: Use the heater, Tips:
        if animatronic == "Nightmare Chica":
            press_Key("3")

        #For Nightmare Bonnie
        #Location: Right side / Cam 2, Action: Keep right door closed, Tips: Can go the route of buying the plush
        if animatronic == "Nightmare Bonnie":
            press_Key("D")

        #For Nightmare Mangle
        #Location: Right Side / Cam 2, Action: Keep right door closed, Tips: Can go the route of buying the plush
        if animatronic == "Nightmare Mangle":
            press_Key("D")

        #For Nightmare Marionne
        #Location: Office, Action: Avoid mousing over, Tips:
        if animatronic == "Nightmare Marionne":
            pass

        #For Nightmare BB
        #Location: Office, Action: Shine flashlight on him, Tips:
        if animatronic == "Nightmare BB":
            press_Key("Z")

        #For Nightmare Fredbear
        #Location: Left side / Cam 2, Action: Close the left door, Tips:
        if animatronic == "Nightmare Fredbear":
            press_Key("A")

        #For Nightmare
        #Location: Right Side / Cam 1, Action: Close the right door, Tips:
        if animatronic == "Nightmare":
            press_Key("D")

        #For Jack-O-Chica
        #Location: Left and Right Side / Cam 1 and 2, Action: Close the left and right door, Tips:
        if animatronic == "Jack-O-Chica":
            press_Key("A")
            press_Key("D")

        #For Plushtrap
        #Location: Office / Monitor, Action: Click on him, Tips:
        if animatronic == "Plushtrap":
            pass

        #endregion

        #region FNAF World

        #For Old Man Consequences
        #Location: Office, Action: Catch the fish with "c" key
        elif animatronic == "Old Man Consequences":
            if pyautogui.locateOnScreen(r'D:\GitHub Repos\UCN-AI\UCN Reference Images\Old Man Consequences (Catching Fish).png', confidence=0.9):
                press_Key("C")

        #For Dee Dee
        #Location: Office, Action: None, Tips: Adds a new animatronic
        elif animatronic == "Dee Dee":
            pass

        #endregion

        #region FNAF: Sister Location

        #For Funtime Foxy
        #Location: Cove, Action: Don't Change to Cam 5, Tips: 
        if animatronic == "Funtime Foxy":
            pass

        #For Ballora
        #Location: Left or Right Door / Cam 1 or 2, Action: Close either the left or right door, Tips: It depends on where the audio cue is located 
        if animatronic == "Ballora":
            pass

        #For Minireena
        #Location: Screen, Action: Nothing, Tips: Just there to cover obscure vision 
        if animatronic == "Minireena":
            pass

        #For Baby
        #Location: Right Side / Cam 2, Action: Keep right door closed, Tips: Can go the route of buying the plush
        if animatronic == "Baby":
            press_Key("D")

        #For Bonnet
        #Location: Office, Action: Click her nose, Tips: 
        if animatronic == "Bonnet":
            pass

        #For Lolbit
        #Location: N/A, Action: Type LOL, Tips: When the audio cue occurs 
        if animatronic == "Lolbit":
            pass

        #For Ennard
        #Location: Front Vent, Action: Close front vent, Tips: Only can be heard from the audio cue 
        if animatronic == "Ennard":
            pass

        #endregion

        #region FNAF: Pizzeria Simulator

        #For Happy Frog
        #Location: Vent System, Action: Audion lure, Tips: Heat does nothing for her
        if animatronic == "Happy Frog":
            pass

        #For Mr. Hippo
        #Location: Vent System, Action: Audio lure and the heater, Tips: Faster than Happy Frog
        if animatronic == "Mr Hippo":
            pass

        #For Pigpatch
        #Location: Vent System, Action: Audio lure and the heater, Tips: Faster than Mr. Hippo
        if animatronic == "Pigpatch":
            pass

        #For Nedd Bear
        #Location: Vent System, Action: Audio lure (only works 50% of the time) and the heater, Tips: Faster than Pigpatch
        if animatronic == "Nedd Bear":
            pass

        #For Orville Elephant
        #Location: Vent System, Action: Audio lure (only works 10% of the time) and the heater, Tips: Faster than Nedd Bear
        if animatronic == "Orville Elephant":
            pass

        #For Rockstar Freddy
        #Location: Office, Action: Turn on the heater or pay Faz-Coins, Tips: Heater can be turned on for a few seconds
        if animatronic == "Rockstar Freddy":
            press_Key("3")

        #For Rockstar Chica
        #Location: Left or Right Doors / Cam 1 or 2, Action: Double click the wet floor sign in front of the correct door, Tips:
        if animatronic == "Rockstar Chica":
            pass

        #For Rockstar Bonnie
        #Location: Office, Action: Click on the parrot for a bounus (don't have to click on it though), Tips:
        if animatronic == "Rockstar Bonnie":
            pass

        #For Helpy
        #Location: Office, Action: Click to get rid of, Tips:
        if animatronic == "Helpy":
            pass

        #For El Chip/
        #Location: Screen, Action: Press enter, Tips:
        if animatronic == "El Chip":
            press_Key("Enter")

        #For Trash and the Gang
        #Location: Screen, Action: Nothing, Tips: Just there to annoy
        if animatronic == "Trash and the Gang":
            pass

        #For Lefty
        #Location: Office, Action: Wind the global music box, Tips: Annoyed by heat and noise
        if animatronic == "Lefty":
            press_Key("5")

        #For Molten Freddy
        #Location: Vents, Action: Close the vent, Tips: He is fast and can be tracked in the monitor
        if animatronic == "Molten Freddy":
            pass

        #For Funtime Chica
        #Location: Screen, Action: Nothing, Tips: Just there to annoy
        if animatronic == "Funtime Chica":
            pass

        #For Shadow Bonnie
        #Location: Office, Action: Nothing, Tips: Causes darkness for 10 seconds
        if animatronic == "Shadow Bonnie":
            pass

        #For Music Man
        #Location: Nothing, Action: Keep the noise down, Tips:
        if animatronic == "Music Man":
            pass

        #For Scrap Baby
        #Location: Office, Action: Shock her when she moves, Tips:
        if animatronic == "Scrap Baby":
            pass

        #For Fredbear
        #Location: Office, Action: Click his hat, Tips:
        if animatronic == "Fredbear":
            pass

        #For William Afton
        #Location: Right Door, Action: Close right door, Tips: Comes once a night and the lights flicker if he is there
        if animatronic == "William Afton":
            press_Key("D")

        #endregion

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
