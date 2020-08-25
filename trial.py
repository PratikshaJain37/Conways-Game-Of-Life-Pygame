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