# Helpers.py - Conway's Game of Life #
# Author: Pratiksha Jain #

# ---------------------#

# Imports #
import random
import numpy as np

# ---------------------#

# For updating the array
def UpdateArray(current_status, INT):
    updated_status = np.zeros((INT,INT), dtype=int)
    for i in range(0,INT):
        for j in range(0,INT):
            
            alive_neigh = GetAliveNeigh(i,j,current_status,INT)
            updated_status[i][j] = GetStatus(alive_neigh,current_status[i][j])

    return updated_status


def GetStatus(alive_neigh, status):
    alive = 0
    if status == 1:
        if alive_neigh in (2,3):
            alive = 1
        else:
            alive = 0
    elif alive_neigh == 3:
        alive = 1
    
    return alive


def GetAliveNeigh(x,y,current_status,INT):
    '''
    alive_neigh = 0
    
    for i in (x-1,x+1):
        if i < INT and i != x:
            if current_status[i][y] == 1:
                alive_neigh += 1
        else:
            i_new = i%INT
            if current_status[i_new][y] == 1:
                alive_neigh += 1

    for j in (y-1,y+1):
        if j < INT and j != y:
            if current_status[x][j] == 1:
                alive_neigh += 1
        else:
            j_new = j%INT
            if current_status[j_new][y] == 1:
                alive_neigh += 1

    
    '''

    alive_neigh = 0

    for i in range(x-1,x+2):
        for j in range(y-1,y+2):
            if i in range(0, INT) and j in range(0,INT):
                if i != x and j != y and current_status[i][j] == 1:
                    alive_neigh += 1
    
    return alive_neigh
