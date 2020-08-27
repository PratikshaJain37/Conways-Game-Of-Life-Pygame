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

# Defining basic font
starmap = "00-starmap.TTF"

# Initialize Status Array 
current_status_array = np.zeros((INT,INT), dtype=int)

# ---------------------#

# Make random status array

for i in range(INT):
    for j in range(INT):
        if random.random() > 0.8:
            current_status_array[i][j] = 1

# ---------------------#

# For Title Text to be displayed

# Defining font style and size
font_title = pygame.font.Font(starmap, 32) 

# Defining position of rect
text_title = font_title.render(" Conway's Game of Life ", True, white, darkgrey)
textrect_title = text_title.get_rect()
textrect_title.center = (40+INT*SIZE/2, 40)

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

# Introduction start screen
# sort this out! add comments + see if text can be shifted to helpers.py
# The button works!


intro = True

while intro:
    
    screen.fill((0,0,0))
    mouse = pygame.mouse.get_pos() 
    intro_title = pygame.font.Font(starmap, 32)
    introlabel = intro_title.render("Welcome to Conway's Game of Life", True, white, darkgrey)
    introtextRect = introlabel.get_rect()
    introtextRect.center = (width/2,height/4)
    intro_text = pygame.font.Font(starmap, 25)
    intro_text1 = intro_text.render("Made by Pratiksha Jain",False, lightgrey)
    intro_text2 = intro_text.render("Font Used: 00-Starmap by Daniel Zadorozny",False, lightgrey)
    start_label = intro_text.render("Start", False, black)
    
    if width/2-70 <= mouse[0] <= width/2+70 and height/2-20 <= mouse[1] <= height/2+20: 
        pygame.draw.rect(screen,(170,170,170),[width/2-70,height/2-20,140,40])      
    else: 
        pygame.draw.rect(screen,(100,100,100),[width/2-70,height/2-20,140,40]) 
    
    for event in pygame.event.get():
        
        if event.type==MOUSEBUTTONDOWN:
            
            if width/2 <= mouse[0] <= width/2+140 and height/2 <= mouse[1] <= height/2+40:
                screen.fill((0,0,0))
                intro = False
        
        if event.type == QUIT:
            exit()
    
    screen.blit(start_label,[width/2-35,height/2-10,140,40])
    screen.blit(intro_text1, [15, height*3/4])
    screen.blit(intro_text2, [15, height*3/4+25])
    screen.blit(introlabel,introtextRect)
    pygame.display.flip()
    screen.fill((0,0,0))




# ---------------------#

# Main python loop

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
    screen.blit(text_title, textrect_title)

    # Refresh screen
    pygame.display.update()

    # A more optimal version of the clock.tick() function, determines fps of display basically
    time.sleep(0.1)

# ---------------------#
