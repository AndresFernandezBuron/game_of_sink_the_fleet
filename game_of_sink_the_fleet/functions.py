#!/usr/bin/env
#-*- coding: utf-8 -*-

"""
Andrés Fernández Burón
2023/10/04

Console game of 'Sink the fleet' with Python 3

Functions for the game.
"""

# DEPENDENCIES


from .config import BOARD_SIZE

from .utils import get_random_value


############################################
#### DEBUG FUNCTIONS #######################
############################################

def get_debug_location( index ):
    location_list = [        # <-- Coordenadas en tupla
        [ (2,0) ],
        [ (4,2) ], 
        [ (5,4) ],
        [ (9,8) ],
        [ (1,7), (1,8) ],
        [ (2,4), (2,5) ],
        [ (7,1), (8,1) ],
        [ (4,8), (5,8), (6,8) ],
        [ (8,4), (8,5), (8,6) ],
        [ (0,1), (0,2), (0,3), (0,4) ],
    ]
    location = location_list[ index ]
    return location


############################################
#### RANDOM FUNCTIONS ######################
############################################

def get_random_coord():
    ''' Return a random Tuple with random coordniates (x,y) '''
    coord_x = get_random_value( 0, BOARD_SIZE-1 )
    coord_y = get_random_value( 0, BOARD_SIZE-1 )
    coordinates = (coord_x, coord_y)
    return coordinates  # <-- tuple

