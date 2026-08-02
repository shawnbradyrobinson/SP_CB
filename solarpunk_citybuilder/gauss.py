# -*- coding: utf-8 -*-
"""
Created on Fri Jul 17 17:30:36 2026

@author: dylan
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Jul 17 10:51:15 2026

@author: dylan
"""

import LandscapeCA as LCA
import numpy as np
import matplotlib.pyplot as plt

# plt.imshow(grid)

# ij_land  = []
# for i in range(np.max(grid)+1):
#     ij_land.append(np.where(grid == i))
    
'''
0: water
1: soil
2: tree
3: rock
4: sand
5: concrete 
'''
rng = np.random.default_rng()

def gaussian2d(ax,ay,x0,y0,i,j,sx,sy,n):
    x = np.arange(n)
    y = np.arange(n)
    g = np.zeros((n,n))
    g[i,j] = ax * np.exp(-(x[i]-x0)**2/(2*sx**2)) * ay *np.exp(-(y[j]-y0)**2/(2*sy**2))
    return g

def apply_gaussian_togrid(hills, terrain, height_mult, grid, sign = 1, n = 100):
    landscape = np.zeros((n,n))
    t_grid = np.where(grid == terrain)
    ts = np.shape(t_grid[0])[0]
    x0 = rng.choice(t_grid[0])
    y0 = rng.choice(t_grid[1])
    for h in range(hills): 
        ax = rng.random() * height_mult
        ay = rng.random() * height_mult
        sx = rng.random()*5 + rng.random()*5 + rng.random()*5 + rng.random()*5
        sy = rng.random()*5 + rng.random()*5 + rng.random()*5 + rng.random()*5
        r = rng.integers(0, ts)
        i = t_grid[0][r]
        j = t_grid[1][r]
        landscape += gaussian2d(ax,ay,x0,y0,i,j,sx,sy,n) * sign
    return landscape

def landscape_smoothening(ws, landscape, n=100):
    smooth_scape = np.copy(landscape)
    steps = int(n/ws)
    for i in range(steps): 
        a = [i*ws, (i+1)*ws]
        
        for j in range(steps):
            b = [j*ws, (j+1)*ws]
            avg = np.average(landscape[a[0]:a[1], b[0]:b[1]])
            smooth_scape[a[0]:a[1], b[0]:b[1]] = avg

    mt_spc = n - steps*ws
    smooth_scape[steps*ws:] = smooth_scape[steps*ws-mt_spc:steps*ws]
    smooth_scape[steps*ws:] += (rng.random(size=100)-1) * np.average(smooth_scape[steps*ws:])
    
    return smooth_scape
    

def generation(n_terrain = 3, water_gen = ['number rng', 'size rng'], land_gen = ['terrain rng', 'size rng'], n=100, heights = np.array([]), plotting = False, verbose = False):
    water_dict = {
        'number rng': rng.integers(1,100),
        'number small': rng.integers(1, 10),
        'number medium': rng.integers(10, 30),
        'number larger': rng.integers(30, 65),
        'number largest': rng.integers(65,100),
        
        'size rng': rng.integers(1, 30),
        'size small': rng.integers(1, 5),
        'size medium': rng.integers(5, 10),
        'size larger': rng.integers(10, 20),
        'size largest': rng.integers(20, 30)
        }
    
    land_dict = {
        'terrain rng': rng.choice(np.arange(1,11), size=10, replace=False),
        'terrain standard': np.arange(1,11),
        
        'size rng': rng.integers(1, 30),
        'size small': rng.integers(1, 4),
        'size medium': rng.integers(4, 9),
        'size larger': rng.integers(9, 14),
        'size largest': rng.integers(14, 20)
        }
    
    water_prevalance = water_dict[water_gen[0]]
    water_growth= water_dict[water_gen[1]]
    terrain_types = land_dict[land_gen[0]][:n_terrain]
    land_growth = land_dict[land_gen[1]]
    
    if verbose:
        print('water prevalance', water_prevalance)
        print('water growth', water_growth) 
        print('terrain types', terrain_types)
        print('land growth', land_growth) 
    
    grid = LCA.make_landscape(water = water_prevalance, its_water=water_growth, n_terrain_1=n_terrain, its_land=land_growth, plotting=plotting)
    for i in range(1, n_terrain):
        grid[grid==i] = terrain_types[i-1]
    
    terrain_types = np.unique(grid)
    
    n_terrain = np.shape(terrain_types)[0]
    plt.figure()
    plt.imshow(grid)
    plt.figure()
    landscape = np.zeros(np.shape(grid))
    signs = np.ones(n_terrain)
    if np.unique(grid)[0] == 0:
        signs[0] = -1
    
    if np.shape(heights)[0] == 0:
        heights = np.ones(n_terrain)
        if np.unique(grid)[0] == 0:
            heights[0] = 3

    for i in range(n_terrain):
        terrain = terrain_types[i]
        for j in range(100):
            landscape += apply_gaussian_togrid(100, terrain, heights[i], grid, sign=signs[i])
            if not j%100 and plotting:
                plt.figure()
                plt.imshow(landscape)
                plt.show()
    
    smooth_scape = np.copy(landscape)
    for i in range(2,10):
        smooth_scape += landscape_smoothening(i, smooth_scape) / (i-1)
        if plotting:
            plt.figure()
            plt.imshow(smooth_scape)
            plt.show()

    if plotting:
            
        landscape[grid == 0] -= 1
        landscape[landscape < -3] = -4
        landscape[landscape < -2] += 1
        smooth_scape[grid == 0] -= 1
        smooth_scape[smooth_scape < -3] = -4
        smooth_scape[smooth_scape < -2] += 1
        
        
        fig = plt.figure(figsize=(8, 3))
        ax1 = fig.add_subplot(121)
        ax1.imshow(landscape)
        ax2 = fig.add_subplot(122)
        ax2.imshow(smooth_scape)
        
        fig = plt.figure(figsize=(10, 10))
        ax1 = fig.add_subplot(121, projection='3d')
        x,y = np.meshgrid(np.arange(n),np.arange(n))
        ax1.scatter3D(x, y, smooth_scape, c=smooth_scape)
        ax2 = fig.add_subplot(122, projection='3d')
        x,y = np.meshgrid(np.arange(n),np.arange(n))
        ax2.scatter3D(x, y, smooth_scape, c=grid)
        
        int_scape = np.copy(smooth_scape)
        int_scape = int_scape.astype(int)
        fig = plt.figure(figsize=(10, 10))
        ax1 = fig.add_subplot(121, projection='3d')
        x,y = np.meshgrid(np.arange(n),np.arange(n))
        ax1.scatter3D(x, y, int_scape, c=int_scape)
        ax2 = fig.add_subplot(122, projection='3d')
        x,y = np.meshgrid(np.arange(n),np.arange(n))
        ax2.scatter3D(x, y, int_scape, c=grid)
    
    return grid, landscape, smooth_scape, int_scape

grid, landscape, smooth_scape, int_scape = generation(n_terrain=5, water_gen = ['number rng', 'size rng'], land_gen = ['terrain rng', 'size small'], plotting=True, verbose=True)