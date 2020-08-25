# Helpers.py - Conway's Game of Life #
# Author: Pratiksha Jain #

# ---------------------#

# Imports #
import random
import numpy as np

# ---------------------#

# For updating the array
def UpdateArray(current_status, INT):

    #Generating new updated array (empty)
    updated_status = np.zeros((INT,INT), dtype=int)

    # Iterating over all in current_status
    for i in range(0,INT):
        for j in range(0,INT):
            
            # Finding number of alive neighbors
            alive_neigh = GetAliveNeigh(i,j,current_status,INT)
            
            # Updating status of box
            updated_status[i][j] = GetStatus(alive_neigh,current_status[i][j])

    return updated_status

# ----------#

# For calculating status of individual box - based on Conway's Rules - https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life

def GetStatus(alive_neigh, status):
    
    # Setting a default 
    alive = 0
    
    # The aforementioned conditions for staying alive
    if status == 1:
        if alive_neigh in (2,3):
            alive = 1
        else:
            alive = 0
    elif alive_neigh == 3:
        alive = 1
    
    return alive

# ----------#

# For calculating number of alive neighbors
def GetAliveNeigh(x,y,current_status,INT):
    
    alive_neigh = 0

    # Iterating through neighbors - the borders are considered dead
    for i in range(x-1,x+2):
        for j in range(y-1,y+2):
            if i in range(0, INT) and j in range(0,INT):
                if not (i == x and j == y):
                    if current_status[i][j] == 1:
                        alive_neigh += 1
    
    return alive_neigh

# ---------------------#