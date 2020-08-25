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

# Initialize screen, status and clock
screen = pygame.display.set_mode((80+INT*SIZE,160+INT*SIZE))
running = True
clock = pygame.time.Clock()

# Defining Colors 
Colors = [(random.randint(1,256),random.randint(0,256),random.randint(0,256)) for i in range(5)]
COLOR_DEAD = (0,0,0)

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
font = pygame.font.Font('freesansbold.ttf', 32) 

text_title = font.render("Conway's Game of Life", True, (255,255,255), (0,0,0))
textRectTitle = text_title.get_rect()
textRectTitle.center = (40+INT*SIZE/2, 40)

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
            self.surf.fill(random.choice(Colors))
        screen.blit(self.surf,self.rect)

    # Function to update surface; as per current_status_array
    def update(self):
        self.alive = current_status_array[self.x][self.y]
        self.assign_color()
     

# ---------------------#

# Creating 'INT_SQ' instances of box class, and appending them to a list for accessibility

boxes = []

for i in range(INT_SQ):

    # x,y will be filled sequentially 
    x = i//INT
    y = i%INT

    # Alive status depening on current array
    boxes.append(Box(x,y,current_status_array[x][y]))

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
    screen.blit(text_title, textRectTitle)

    # Refresh screen
    pygame.display.update()

    # A more optimal version of the clock.tick() function, determines fps of display basically
    time.sleep(0.5)

# ---------------------#
