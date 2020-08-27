import pygame
from pygame.locals import *
from sys import exit
from random import *
import time

pygame.init()

screen = pygame.display.set_mode((640, 480))

class Rectangle:
    def __init__(self, pos, color, number):
        self.pos = pos
        self.color = color
        self.number = number
    def draw(self):
        pygame.draw.rect(screen, self.color, Rect(self.pos, (40,40)))
    def update(self, new_color):
        pygame.draw.rect(screen, new_color, Rect(self.pos, (40,40)))

rectangles = []     

for count in range(10):
    countx = count//5
    county = count%5
    
    random_pos = (30 + countx*45, 30 + county*45)
    
    if countx > 0:
        rectangles.append(Rectangle(random_pos, (0,120,255),count))
    else:
        rectangles.append(Rectangle(random_pos, (120,0,255),count))

width = screen.get_width() 
height = screen.get_height()
color_light = (170,170,170) 
color_dark = 

intro = True
while (intro == True):
    screen.fill((0,0,0))
    mouse = pygame.mouse.get_pos() 
    myfont=pygame.font.Font("00-starmap.TTF", 30)
    nlabel=myfont.render("Welcome to Conway's Game of Life", 1, (255, 0, 0))

    
    screen.fill((60,25,60))
    if width/2 <= mouse[0] <= width/2+140 and height/2 <= mouse[1] <= height/2+40: 
        pygame.draw.rect(screen,color_light,[width/2,height/2,140,40]) 
          
    else: 
        pygame.draw.rect(screen,color_dark,[width/2,height/2,140,40]) 
    
    
    
    for event in pygame.event.get():
        if event.type==MOUSEBUTTONDOWN:
            if width/2 <= mouse[0] <= width/2+140 and height/2 <= mouse[1] <= height/2+40:
                screen.fill((0,0,0))
                intro = False
        if event.type == QUIT:
            exit()
    screen.blit(nlabel,(200,200))
    pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
    screen.lock()
    for rectangle in rectangles:
        if rectangle.number > 4:
            rectangle.update((randint(0,255), randint(0,255), randint(0,255)))
        else:
            rectangle.update((0,200,255))
    screen.unlock()
    pygame.display.update()
    time.sleep(2)