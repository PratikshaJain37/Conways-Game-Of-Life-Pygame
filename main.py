# Main.py - Conway's Game of Life #
# Author: Pratiksha Jain #

# ---------------------#

# Imports #
import pygame
from pygame.locals import *
from helpers import *
import random
import numpy as np
import time
import os

# ---------------------#

# Initialize number of rows/columns
INT = 100
INT_SQ = INT*INT

# Initialize size of arrays
SIZE = 5

# Initialize Pygame
pygame.init()

# Initialize screen
width = 80+INT*SIZE
height = 160+INT*SIZE+50
screen = pygame.display.set_mode((width,height))

# Defining Colours 
black = (0,0,0)
darkgrey = (50,50,50)
lightgrey = (170,170,170)
white = (255,255,255)

COLORS = [(random.randint(1,256),random.randint(0,256),random.randint(0,256)) for i in range(5)]
COLOR_DEAD = black

# ---------------------#

# Initialize Status Array and make it randomly filled with 0's and 1's
current_status_array = np.zeros((INT,INT), dtype=int)
RandomizeArray(INT, current_status_array)

# ---------------------#

# Defining Box Class
class Box():
    
    # Status can be dead (0) or alive(1); 
    def __init__(self, x, y, alive):
        self.x = x
        self.y = y
        self.alive = alive
        self.surf = pygame.Surface((SIZE,SIZE))
        self.rect = (40 + SIZE*self.y, 100 + SIZE*self.x)
    
    # Function to fill surface with color
    def assign_color(self):
        if self.alive == 0:
            self.surf.fill(COLOR_DEAD)
        else:
            self.surf.fill(random.choice(COLORS))
        screen.blit(self.surf,self.rect)

    # Function to update surface; as per current_status_array
    def update(self):
        self.alive = current_status_array[self.x][self.y]
        self.assign_color()
     

# ----------#

# Creating 'INT_SQ' instances of box class, and appending them to a list for accessibility

boxes = []

for i in range(INT_SQ):

    # x,y will be filled sequentially 
    x = i//INT
    y = i%INT

    # Alive status depening on current array
    boxes.append(Box(x, y, current_status_array[x][y]))

# ---------------------#

# Loop for Start Screen

def StartScreen():

    # Defining Global Variables
    global height, width, screen
    global black, white, lightgrey, darkgrey

    Blit_List = []

    # Setting up the start button, its rect and the label on it
    start_button = (width/2-70, height/2-20)
    start_button_rect = Rect(start_button[0],start_button[1],140,40)
    Blit_List.append(DisplayText('Start', 20, black,(width/2,height/2)))
    
    # For displaying title text
    Blit_List.append(DisplayText("Welcome to Conway's Game of Life", 32, white, (width/2,height/4) , color_bg=darkgrey))

    # For displaying Created By text
    Blit_List.append(DisplayText("Made by Pratiksha Jain", 20, lightgrey, (width/2, height*3/4)))

    # For displaying Credits text
    Blit_List.append(DisplayText("Font Used: 00-Starmap by Daniel Zadorozny", 20, lightgrey, (width/2,height*3/4+25)))

    # Initializing status for loop
    intro = True

    while intro:

        # For getting location of mouse
        mouse = pygame.mouse.get_pos() 

        # For hover colour change - colour changes to light grey
        if start_button[0] <= mouse[0] <= start_button[0]+140 and start_button[1] <= mouse[1] <= start_button[1]+40: 
            pygame.draw.rect(screen, lightgrey, start_button_rect)      
        else: 
            pygame.draw.rect(screen, darkgrey, start_button_rect) 

        # Loop for events
        for event in pygame.event.get():
            
            # If start button is pressed, the intro is turned off
            if event.type == MOUSEBUTTONDOWN:
                if start_button[0] <= mouse[0] <= start_button[0]+140 and start_button[1] <= mouse[1] <= start_button[1]+40:
                    intro = False
            
            # Main quit function
            if event.type == QUIT:
                exit()

        # Blitting the text on to the screen surface
        BlitObjects(Blit_List, screen)

        # Refresh screen
        pygame.display.update()

        # Setting the screen to black - default
        screen.fill(black)


# ---------------------#

# Main python loop for game

def Main():

    # Defining Global Variables
    global height, width, screen
    global black, white, lightgrey, darkgrey

    # Defining variables that control the loops
    running = True
    SLEEPTIME = 0.1
    game = True

    # Creating list of items to be blitted in each Main loop
    Blit_List = []

    # For Title Text to be displayed
    Blit_List.append(DisplayText(" Conway's Game of Life ", 32,white,(40+INT*SIZE/2, 40) ,color_bg=darkgrey, antialias=True))


    # For play, pause, stop, faster, slower buttons to be displayed

    buttons = ["slower", "faster","play", "pause","stop"]
    button_dict = {}
    button_loc = width/2-120

    for num,button in enumerate(buttons):
        
        button_imgsurf = pygame.image.load("images/{}.jpg".format(button)).convert()
        button_imgsurf = pygame.transform.scale(button_imgsurf, (40,40))
        button_light_img = pygame.image.load("images/{}_light.jpg".format(button)).convert()
        button_light_img = pygame.transform.scale(button_light_img, (40,40))
        
        button_dict[button] = [button_imgsurf, button_light_img, button_loc+num*50]
    
    
    while running:

        # For getting location of mouse
        mouse = pygame.mouse.get_pos() 

        # Main python event function
        for event in pygame.event.get():

            # Main quit function
            if event.type == pygame.QUIT:
                running = False

            # For the buttons
            if event.type == MOUSEBUTTONDOWN:
                
                # Slower button
                if button_dict['slower'][2] <= mouse[0] <= button_dict['slower'][2]+40 and 130+SIZE*INT <= mouse[1] <= 130+SIZE*INT+40:
                    SLEEPTIME += 0.01
                
                # Faster button
                if button_dict['faster'][2] <= mouse[0] <= button_dict['faster'][2]+40 and 130+SIZE*INT <= mouse[1] <= 130+SIZE*INT+40:
                    SLEEPTIME -= 0.01

                # Play button
                if button_dict['play'][2] <= mouse[0] <= button_dict['play'][2]+40 and 130+SIZE*INT <= mouse[1] <= 130+SIZE*INT+40:
                    game = True
                
                # Pause button
                if button_dict['pause'][2] <= mouse[0] <= button_dict['pause'][2]+40 and 130+SIZE*INT <= mouse[1] <= 130+SIZE*INT+40:
                    game = False
                
                # Stop button
                if button_dict['stop'][2] <= mouse[0] <= button_dict['stop'][2]+40 and 130+SIZE*INT <= mouse[1] <= 130+SIZE*INT+40:
                    running = False

        # For hover colour change - colour changes to light grey
        
        for button in buttons:
        
            if button_dict[button][2] <= mouse[0] <= button_dict[button][2]+40 and 130+SIZE*INT <= mouse[1] <= 130+SIZE*INT+40:
                Blit_List.append((button_dict[button][1], (button_dict[button][2], 130+SIZE*INT)))      
            else: 
                Blit_List.append((button_dict[button][0], (button_dict[button][2], 130+SIZE*INT))) 
        
        # For updating array and boxes status
        if game == True:
            GameLoop(SLEEPTIME)

        # Blit objects
        BlitObjects(Blit_List, screen)
        Blit_List = Blit_List[:1]

        # Refresh screen
        pygame.display.update()


def GameLoop(SLEEPTIME):

    global current_status_array, INT, boxes
    
    # For updating array and boxes status
    current_status_array = UpdateArray(current_status_array, INT)
    for box in boxes:
        box.update()
    
    time.sleep(SLEEPTIME)

# ---------------------#

# Running the functions

StartScreen()
Main()

# ---------------------#
