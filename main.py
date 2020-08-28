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

# Initialize screen and status
width = 80+INT*SIZE
height = 160+INT*SIZE+50
screen = pygame.display.set_mode((width,height))
running = True
SLEEPTIME = 0.1

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

# For play, pause, stop, faster, slower buttons to be displayed

play = pygame.image.load("images/play.jpg").convert()
play = pygame.transform.scale(play, (40,40))

play_light = pygame.image.load("images/play_light.jpg").convert()
play_light = pygame.transform.scale(play_light, (40,40))


stop = pygame.image.load("images/stop.jpg").convert()
stop = pygame.transform.scale(stop, (40,40))

stop_light = pygame.image.load("images/stop_light.jpg").convert()
stop_light = pygame.transform.scale(stop_light, (40,40))


pause = pygame.image.load("images/pause.jpg").convert()
pause = pygame.transform.scale(pause, (40,40))

pause_light = pygame.image.load("images/pause_light.jpg").convert()
pause_light = pygame.transform.scale(pause_light, (40,40))


faster = pygame.image.load("images/faster.jpg").convert()
faster = pygame.transform.scale(faster, (40,40))

faster_light = pygame.image.load("images/faster_light.jpg").convert()
faster_light = pygame.transform.scale(faster_light, (40,40))


slower = pygame.image.load("images/slower.jpg").convert()
slower = pygame.transform.scale(slower, (40,40))

slower_light = pygame.image.load("images/slower_light.jpg").convert()
slower_light = pygame.transform.scale(slower_light, (40,40))

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

    # For getting location of mouse
    mouse = pygame.mouse.get_pos() 

    # Main python event function
    for event in pygame.event.get():

        # Main quit function
        if event.type == pygame.QUIT:
            running = False

        # For the buttons
        if event.type == MOUSEBUTTONDOWN:
            
            # Play button
            if width/2-20 <= mouse[0] <= width/2+20 and 130+SIZE*INT <= mouse[1] <= 130+SIZE*INT+40:
                running = True
            
            # Pause button
            if width/2+30 <= mouse[0] <= width/2+70 and 130+SIZE*INT <= mouse[1] <= 130+SIZE*INT+40:
                running = True
            
            # Stop button
            if width/2+80 <= mouse[0] <= width/2+120 and 130+SIZE*INT <= mouse[1] <= 130+SIZE*INT+40:
                running = False
            
            # Faster button
            if width/2-70 <= mouse[0] <= width/2-30 and 130+SIZE*INT <= mouse[1] <= 130+SIZE*INT+40:
                running = True
            
            # Slower button
            if width/2-120 <= mouse[0] <= width/2-80 and 130+SIZE*INT <= mouse[1] <= 130+SIZE*INT+40:
                running = True

    # For hover colour change - colour changes to light grey
    if width/2-20 <= mouse[0] <= width/2+20 and 130+SIZE*INT <= mouse[1] <= 130+SIZE*INT+40:
        screen.blit(play_light, (width/2-20, 130+SIZE*INT))      
    else: 
        screen.blit(play, (width/2-20, 130+SIZE*INT)) 
    
    if width/2+30 <= mouse[0] <= width/2+70 and 130+SIZE*INT <= mouse[1] <= 130+SIZE*INT+40:
        screen.blit(pause_light, (width/2+30, 130+SIZE*INT))      
    else: 
        screen.blit(pause, (width/2+30, 130+SIZE*INT)) 

    if width/2+80 <= mouse[0] <= width/2+120 and 130+SIZE*INT <= mouse[1] <= 130+SIZE*INT+40:
        screen.blit(stop_light, (width/2+80, 130+SIZE*INT))      
    else: 
        screen.blit(stop, (width/2+80, 130+SIZE*INT)) 
    
    if width/2-70 <= mouse[0] <= width/2-30 and 130+SIZE*INT <= mouse[1] <= 130+SIZE*INT+40:
        screen.blit(faster_light, (width/2-70, 130+SIZE*INT))      
    else: 
        screen.blit(faster, (width/2-70, 130+SIZE*INT)) 
    
    if width/2-120 <= mouse[0] <= width/2-80 and 130+SIZE*INT <= mouse[1] <= 130+SIZE*INT+40:
        screen.blit(slower_light, (width/2-120, 130+SIZE*INT))      
    else: 
        screen.blit(slower, (width/2-120, 130+SIZE*INT)) 


    # For updating array and boxes status
    current_status_array = UpdateArray(current_status_array, INT)
    for box in boxes:
        box.update()

    # Display Title
    screen.blit(title_text, title_rect)

    # Refresh screen
    pygame.display.update()

    # A more optimal version of the clock.tick() function, determines fps of display basically
    time.sleep(SLEEPTIME)



# ---------------------#
