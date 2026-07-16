# -*- coding: utf-8 -*-
"""
Created on Sat Jul 11 09:02:47 2026

@author: dylan
"""

import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng()

t = 0
ts = 40
shifts = np.array([[-1,0], [-1,-1], [-1,1], [0,-1], [0,1], [1,1], [1,0], [1,-1]])

def init_grid(n, n_terrain):
    '''
    n : integer, square grid length
    n_terrain : integer, number of types of terrain
    
    grid : n x n output of initialized with terrain in equal values
    '''
    grid = rng.integers(n_terrain, size = (n,n))
    return grid    


def update_cell_id_fast(grid, n_terrain, energy):
    '''
    grid :  n x n terrain values
    n_terrain : number of types of terrain 
    energy: difficulty to flip a terrain value
    '''
    ### initialize ###
    n = np.shape(grid)[0]
    newgrid = np.copy(grid)
    
    ### set a random order of terrain types to comb through ###
    ### samples without replacement, e.g. 4 terrain types: order = [2,1,3,4] ### 
    order = rng.choice(np.arange(n_terrain), size=n_terrain, replace=False)

    ### comb through grid, update terrain types based on surrounding pixels ###
    for i in range(n_terrain):
        ind = order[i]
        a0 = np.where(newgrid == ind)
        for j in range(np.shape(a0)[1]): 
            ### 'a' is coordinates for given pixel ###
            a = a0[0][j], a0[1][j]

            ### sub is the pixels surrounding pixel at 'a' (L2 neighbors) ###
            sub = grid[(shifts[:,0] + a[0])%n, (shifts[:,1] + a[1])%n]
            
            ### Cellular automata update rule: if the number of L2 neighbors ###
            ### does not contain at least 'energy' amount of the same type    ### 
            ### as pixel at 'a', then randomly change pixel at 'a' to the value ###
            ### of one of its neighbors ###
            if len(sub[sub==ind]) < energy:
                newgrid[a] = rng.choice(sub)
        grid = newgrid
    return grid


def fast_ca(grid, n_terrain, iterations):
    '''
    Parameters
    ----------
    grid : n x n array, initialized with the desired number / ratio of terrain types 
    n_terrain : integer, number of types of terrain
    iterations : number of growth steps
    
    Returns
    -------
    grid : n x n array, final state after iterations of cell growth
    '''
    ### the 'energy' value of the CA is set to 'j' and is ran 1 through 7 ###
    ### j == 1: eliminates 'loner' terrains, e.g. a value 4 surrounded by no other 4's
    ### j == 2-6: increases requirement for a terrain to remain.
    ###           increasingly favors larger more stable terrains. 
    ###           note that j = 5 or 6 will cause boundaries to flip and create jagged edges 
    ### repeat this process 'iterations' number of times
    for i in range(iterations):
        for j in range(1, 7):
            grid = update_cell_id_fast(grid, n_terrain, j)
            
    ### works to remove jagged edges ###
    grid = update_cell_id_fast(grid, n_terrain, 4)
    return grid


def make_landscape(n = 100, its_water = 15, its_land = 5, n_terrain_0 = 2, n_terrain_1 = 5, water = 13, plotting = False):
    '''
    n = 100       # square grid length 
    iterations    # more iterations = more growth
    n_terrain     # types of terrain
    water         # prevalance of water, higher value = more water, max value of n**2
    '''
    #### GENERATE WATER ####
    grid = init_grid(n, n_terrain_0)      # initialize a random grid w/ 2 states
    
    ### the below line increases the prevalance of land from the 50/50 initial split ###
    grid[rng.integers(0,n, size=(int(n**2 / water))), rng.integers(0,n, size=(int(n**2 / water)))] = 1
    
    grid_water = fast_ca(grid, n_terrain_0, its_water)
    if plotting:
        plt.imshow(grid_water)
        plt.show()
    
    
    #### GENERATE LAND ####
    grid = init_grid(n, n_terrain_1)  # initiate a random grid w/ n_terrain states
    grid_land = fast_ca(grid, n_terrain_1, its_land) 
    grid_land += 1      # add one to everything since water is chosen as state '0' 
                        # adding 1 makes there be no water in the land prior to masking
    grid_land[np.where(grid_water == 0)] = 0    # mask the land with the water/bedrock.
    if plotting:
        plt.imshow(grid_land)   # look at the beautiful landscape!
        plt.show()
        
    return grid_land

if __name__ == '__main__':
    make_landscape(plotting=True)

#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#####################################################################
####### OLD FUNCTIONS FROM DEV TIMES. THEY ARE KINDA INTERESTING ####
####### BUT PROBABLY JUST JUNK AT THIS POINT ########################
#####################################################################

# def update_cell_id(grid, cell_a, cell_b, temp, energy):
#     n = np.shape(grid)[0]
#     newgrid = np.copy(grid)
#     a0 = np.where(newgrid == cell_a)
#     for j in range(np.shape(a0)[1]): 
#         a = a0[0][j], a0[1][j]
#         sub = grid[(shifts[:,0] + a[0])%n, (shifts[:,1] + a[1])%n]
#         if len(sub[sub==cell_a]) < energy:
#             newgrid[a] = cell_b
#         if rng.random() < temp:
#             newgrid[a] = cell_b
#     return newgrid

# def update_cell_id_2(grid, n_terrain, temp, energy):
#     n = np.shape(grid)[0]
#     newgrid = np.copy(grid)
#     for i in range(n_terrain):
#         a0 = np.where(newgrid == i)
#         for j in range(np.shape(a0)[1]): 
#             a = a0[0][j], a0[1][j]
#             sub = grid[(shifts[:,0] + a[0])%n, (shifts[:,1] + a[1])%n]
#             for k in range(n_terrain):
#                 if len(sub[sub==k]) > energy:
#                     newgrid[a] = k
#                 else: 
#                     if rng.random() < temp:
#                         newgrid[a] = rng.integers(n_terrain)
#     return newgrid

# def run_ca(grid, n, n_terrain, ts, temp, energy, tolerance):    
#     #tolerance = n_terrain * energy * 5 * (1 + temp) 
#     plt.imshow(grid, cmap='jet')
#     plt.clim(0,n_terrain)
#     plt.show()
#     for i in range(ts):
#         for j in range(n_terrain):
#             for k in range(j+1, n_terrain):
#                 grid1 = update_cell_id_2(grid, n_terrain, temp, energy)
                
#                 if np.sum(abs(grid-grid1))/np.average(grid) < tolerance:
#                     return grid
                
#                 else:
#                     grid = grid1
#                     plt.imshow(grid, cmap='jet')
#                     plt.show()
#     return grid
