#!/usr/bin/env
#-*- coding: utf-8 -*-

"""
Andrés Fernández Burón
2023/10/04

Console game of 'Sink the fleet' with Python 3


File with Score, Player. Computer and Human classes for the game.
"""

# DEPENDENCIES

# SUBMODULES
from .config import *
from .consts import *

from .utils import ask_value

from .functions import get_debug_location

from .GameBoard import GameBoard
from .Fleet import *


class Score:
    ''' Score class definition '''

    def __init__( self, ship_counter ):
        ''' Score class constructor '''
        self.info = {
            'ships': ship_counter, 
            'shots': 0, 
            'hits':  0, 
            'fails': 0
        }

    # METHODS:

    def get_info( self, space:int=5 ):
        ''' Return array os str with user game info '''
        hits = fails = 0
        if self.info['shots'] > 0:
            hits = (self.info['hits']*100)/self.info['shots']
            fails = (self.info['fails']*100)/self.info['shots']

        score_info = [
            f"BARCOS:   {str(self.info['ships']).ljust(space,' ')}",
            f"DISPAROS: {str(self.info['shots']).ljust(space,' ')}",
            f"ACIERTOS: {str(self.info['hits']).ljust(space,' ')} ({round(hits,1)} %)",
            f"FALLOS:   {str(self.info['fails']).ljust(space,' ')} ({round(fails,1)} %)",
        ]
        return score_info



############################################
#### GAME PLAYERS ##########################
############################################


class Player:
    ''' Player class definition '''

    def __init__( self, player_type:str ):
        ''' User class constructor '''
        ##self.type = player_type
        self.board = GameBoard()
        self.history = GameBoard()
        self.fleet = Fleet()
        self.score = Score( self.fleet.ship_list.size )

    # METHODS:

    def randomize_ships( self ):
        ''' Randomize the ship locations '''
        for i in range( self.fleet.ship_list.size ):

            location = []
            if DEBUG:
                location = get_debug_location( i )
            else:
                location = get_debug_location( i )
                pass #location = get_rand_location()

            self.fleet.ship_list[i].ubicate( location )

            self.board.put_ship( location )
            

    def count_alive_ships( self ):
        ''' Count alive ships in the fleet '''
        counter = 0
        # Each ship
        for i in range( self.fleet.ship_list.size ):
            # Each coorinate
            is_sunked = True
            for coord in self.fleet.ship_list[i].location:
                coord_x, coord_y = coord
                if self.board.content[coord_x][coord_y] == SUNKEN:
                    is_sunked = True
                    break
                elif self.board.content[coord_x][coord_y] == SHIP:
                    is_sunked = False
                    break
            if not is_sunked:
                counter += 1
        self.score.info['ships'] = counter
        return counter

class Computer( Player ):
    ''' Computer class definition '''

    # STATIC VAR
    cont = 0

    def __init__( self ):
        ''' Computer class constructor '''
        super().__init__('COMPUTER')
        
        self.char = COMPUTER

        self.name = f'COMPUTER {Computer.cont + 1}'
        Computer.cont += 1

        self.randomize_ships()

class Human( Player ):
    ''' Human class definition '''

    def __init__( self ):
        ''' Human class constructor '''
        super().__init__('PLAYER')

        self.char = PLAYER

        self.name = ask_value('Introduce tu nombre')

        if INTERACTIVE:
            self.randomize_ships()
            pass

        else:
            self.randomize_ships()
