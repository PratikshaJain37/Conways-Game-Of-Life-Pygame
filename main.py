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

# ---------------------#

# Initialize number of rows/columns
INT = 100
INT_SQ = INT*INT

# Initialize size of arrays
SIZE = 5

# Initialize Pygame
pygame.init()

# Initialize screen and status
width = 80+INT*SIZE
height = 160+INT*SIZE
screen = pygame.display.set_mode((width,height))
running = True

# Defining Colours 

black = (0,0,0)
darkgrey = (50,50,50)
lightgrey = (170,170,170)
white = (255,255,255)

COLORS = [(random.randint(1,256),random.randint(0,256),random.randint(0,256)) for i in range(5)]
COLOR_DEAD = black

# Defining default font
starmap = "00-starmap.TTF"

# Initialize Status Array and make it randomly filled with 0's and 1's
current_status_array = np.zeros((INT,INT), dtype=int)
RandomizeArray(INT, current_status_array)

# ---------------------#

# For Title Text to be displayed

title_text, title_rect = DisplayText(" Conway's Game of Life ", 32,white,(40+INT*SIZE/2, 40) ,color_bg=darkgrey, antialias=True)

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
    boxes.append(Box(x,y,current_status_array[x][y]))

# ---------------------#

# Loop for Start Screen

# Setting up the start button, it's rect and the label on it
start_button = (width/2-70, height/2-20)
start_button_rect = Rect(start_button[0],start_button[1],140,40)

intro_start_text, intro_start_rect = DisplayText('Start', 20, black,(width/2,height/2))


# For displaying title text
intro_title_text, intro_title_rect = DisplayText("Welcome to Conway's Game of Life", 32, white, (width/2,height/4) , color_bg=darkgrey)

# For displaying Created By text
intro_creator_text, intro_creator_rect = DisplayText("Made by Pratiksha Jain", 20, lightgrey, (width/2, height*3/4))

# For displaying Credits text
intro_credits_text, intro_credits_rect = DisplayText("Font Used: 00-Starmap by Daniel Zadorozny", 20, lightgrey, (width/2,height*3/4+25))


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
    screen.blit(intro_title_text,intro_title_rect)
    screen.blit(intro_creator_text, intro_creator_rect)
    screen.blit(intro_credits_text, intro_credits_rect)
    screen.blit(intro_start_text, intro_start_rect)

    
    # Refresh screen
    pygame.display.update()

    # Setting the screen to black - default
    screen.fill(black)
    
# ---------------------#

# Main python loop for game

while running:
    
    # Main python quit function
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # For updating array and boxes status
    current_status_array = UpdateArray(current_status_array, INT)
    for box in boxes:
        box.update()

    # Display Title
    screen.blit(title_text, title_rect)

    # Refresh screen
    pygame.display.update()

    # A more optimal version of the clock.tick() function, determines fps of display basically
    time.sleep(0.1)

# ---------------------#
