#!/usr/bin/env
#-*- coding: utf-8 -*-

"""
Andrés Fernández Burón
2023/10/04

Console game of 'Sink the fleet' with Python 3


File with Board and GameBoard classes for the game.
"""

# DEPENDENCIES
import numpy as np


# SUBMODULES
from .config import *
from .consts import *


############################################
#### GAME BOARDS ###########################
############################################

class Board:
    ''' Board class definition '''

    def __init__( self ):
        ''' Board class constructor '''
        board_shape = (BOARD_SIZE, BOARD_SIZE)
        self.content = np.full( shape=board_shape, fill_value=WATER )

    # METHODS:

    def get_as_str_list( self ):
        ''' Get a str list with a game board '''
        game_board_list = []
        line = ''.join([ f' {i}' for i in range(BOARD_SIZE) ])
        game_board_list.append( f' {line}' )
        row_index = 0
        for row in self.content:
            line = f'{row_index}'
            for col in row:
                line = f'{line}{col}'
            line = f'{line}'
            game_board_list.append( line )
            row_index += 1
        return game_board_list
    



class GameBoard( Board ):
    ''' GameBoard class definition '''

    def __init__( self ):
        ''' GameBoard class constructor '''
        super().__init__()

    # METHODS:
    
    def put_ship( self, location ):
        ''' Set a ship on the game board '''
        for coord in location:
            coord_x, coord_y = coord
            self.content[coord_x][coord_y] = SHIP
    
    def is_sunked_ship( self, location ):
        ''' Check if is a sunked ship '''
        for coord in location:
            coord_x, coord_y = coord 
            state = self.content[ coord_x ][ coord_y ]
            if state == SUNKEN:
                return True
            elif state == SHIP:
                return False
        return True

