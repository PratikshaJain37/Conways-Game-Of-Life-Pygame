# Helpers.py #

import random
import numpy as np

def UpdateArray(current_status, INT):
    updated_status = np.full((INT,INT),0)
    for i in range(0,INT):
        for j in range(0,INT):
            
            alive_neigh = GetAliveNeigh(i,j,current_status,INT)
            
            updated_status[i][j] = GetStatus(alive_neigh,current_status[i,j])

            print(alive_neigh, updated_status[i][j])

    
    return updated_status

def GetStatus(alive_neigh,current_status_box):
    alive = 0
    if current_status_box == 1:
        if alive_neigh in (2,3):
            alive = 1
    elif alive_neigh == 3:
        alive = 1
    
    return alive


def GetAliveNeigh(x,y,current_status_array,INT):
  
    alive_neigh = 0
    
    for i in range(x-1,x+2):
        if i < INT and i != x:
            if current_status_array[i][y] == 1:
                alive_neigh += 1
        else:
            i_new = i%INT
            if current_status_array[i_new][y] == 1:
                alive_neigh += 1

    for j in range(y-1,y+2):
        if j < INT and j != y:
            if current_status_array[x][j] == 1:
                alive_neigh += 1
        else:
            j_new = j%INT
            if current_status_array[j_new][y] == 1:
                alive_neigh += 1

    return alive_neigh

