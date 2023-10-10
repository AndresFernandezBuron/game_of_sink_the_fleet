#!/usr/bin/env
#-*- coding: utf-8 -*-

"""
Andrés Fernández Burón
2023/10/04

Console game of 'Sink the fleet' with Python 3


File with Ship and Fleet classes for the game.
"""

# DEPENDENCIES

import numpy as np

# SUBMODULES
from .config import *
from .consts import *


############################################
#### GAME FLEET ############################
############################################

class Ship:
    ''' Ship class definition '''

    def __init__( self, large:int ):
        ''' Ship class constructor '''
        self.large = large

        empty_data = [ tuple([0,0]) for i in range( large ) ]
        self.location = np.array( empty_data ).astype( tuple )

    # METHODS:

    def ubicate( self, location ):
        ''' Update ship location in the class variable '''
        if type(location) == list:
            self.location = np.array( location )
        
        elif type(location) == np.array:
            self.location = location

class Fleet:
    ''' Fleet class definition '''

    def __init__( self ):
        ''' Fleet class constructor '''
        self.initialize()

    # METHODS:

    def initialize( self ):
        ''' Initialize the ship array '''
        ship_buffer = []
        for i in range( SHIPS_SIZES_COUNT ):
            large = SHIPS_SIZES_COUNT - i
            ship_count = i + 1

            for j in range( ship_count ):
                ship = Ship(large)
                ship_buffer.append( ship )

        self.ship_list = np.asarray( ship_buffer )
        self.count = len( self.ship_list )



    def get_ship_location( self, coordinates:tuple ):
        ''' Get a ship location of the fleet '''
        for i in range( self.ship_list.size ):
            for coord_arr in self.ship_list[i].location:

                mask = ( coord_arr == coordinates )

                if np.any( coord_arr[ mask ] ):
                    return self.ship_list[i].location

