#!/usr/bin/env
#-*- coding: utf-8 -*-

"""
Andrés Fernández Burón
2023/10/04

Console game of 'Sink the fleet' with Python 3


File with Game, SinkTheFleet, GameCvC and GamePvE classes for the game.
"""

# DEPENDENCIES

import numpy as np

from time import sleep

# SUBMODULES
from .config import *
from .consts import *

from .functions import get_random_coord

from .utils import ask_coordinates

from .GameBoard import *
from .Player import *
from .UserInterface import *


class Game:
    ''' Game class definition '''

    def __init__( self ):
        ''' Game class constructor '''

        self.winner = False
        self.round = 0

        self.ui = UserInterface()
        if not DEBUG:
            self.ui.show_banner()

    # METHODS:

    def new_round( self ):
        ''' Update round variables '''
        self.round += 1

    def is_valid_shot( self, attacker_char:str, attacker_history:Board, coordinates:tuple ):
        ''' Check if is not a repeated shot '''
        coord_x, coord_y = coordinates
        history_value = attacker_history[coord_x][coord_y]
        if history_value==WATER:
            return True
        elif history_value==FAIL or history_value==TOUCHED or history_value==SUNKEN:
            
            if attacker_char == PLAYER:
                print(f' Disparado repetido en {coordinates}')
                
            return False
        return True

class SinkTheFleet( Game ):
    ''' SinkTheFleet class definition '''

    def __init__( self, mode:str ):
        ''' SinkTheFleet class constructor '''
        super().__init__()

        self.mode = mode

        self.start_time = time()

    # METHODS:

    def sunk_ship( self, attacker_history:Player, defender_board:Player, location ):
        ' '' Show a ship location as sunked in the board '' '
        for coord in location:
            coord_x, coord_y = coord
            attacker_history[coord_x][coord_y] = SUNKEN
            defender_board[coord_x][coord_y] = SUNKEN

    def update_sunked_ships( self, attacker, defender ):
        ''' Update all ship state if are sunk '''
        # Each ship
        for i in range( defender.fleet.ship_list.size ):
            # Each coorinate
            is_sunk = False
            hit_cont = 0
            for coord in defender.fleet.ship_list[i].location:
                coord_x, coord_y = coord
                shotted_value = defender.board.content[coord_x][coord_y]
                if shotted_value == SUNKEN:
                    is_sunk = True
                    break
                elif shotted_value != SHIP:
                    hit_cont += 1
                    if hit_cont == defender.fleet.ship_list[i].large:
                        is_sunk = True
            # Update ship state to sunk
            if is_sunk:
                self.sunk_ship(attacker.history.content, defender.board.content, defender.fleet.ship_list[i].location)

    def handle_player_round( self, attacker:Player, defender:Player, show:bool=True ):
        ''' Handle a player round '''

        self.ui.show_player_header( attacker )
        
        if show:
            self.ui.show_boards( attacker )
        else:
            info = attacker.score.get_info( space=1 )
            [ print(f' {i}', end='') for i in info ]
            print()

        # WHILE SHOOTER HITS 
        another_shot = True
        while another_shot:
            another_shot = self.shot( attacker, defender )

            if defender.count_alive_ships() == 0:
                self.winner = attacker
                break

    def shot( self, attacker:Player, defender:Player ):
        ''' Make 1-N shot 
        If the shot is hit or is a repeated shot, 
        player have another shot '''
        # WHILE SHOOTER REPEATS THE SHOT
        valid_shot = False
        while not valid_shot:
            coordinates = ()

            # PLAYER
            if isinstance(attacker, Human):
                if INTERACTIVE: coordinates = ask_coordinates()
                else: coordinates = get_random_coord()

            # COMPUTER
            elif isinstance(attacker, Computer):
                coordinates = get_random_coord()

            valid_shot = self.is_valid_shot( attacker.char, attacker.history.content, coordinates )

        return self.handle_shot( attacker, defender, coordinates )

    def handle_shot( self, attacker:Player, defender:Player, coordinates:tuple ):
        '''Handle a shot in a coordinates ''' 

        coord_x, coord_y = coordinates
        shotted_value = defender.board.content[coord_x][coord_y]

        # SHOOTER FAILS
        if shotted_value==WATER:
            print(f' Disparado fallado en {coordinates}')
            attacker.score.info['shots'] += 1
            attacker.score.info['fails'] += 1
            attacker.history.content[coord_x][coord_y] = FAIL

        # SHOOTER HITS
        elif shotted_value==SHIP:
            attacker.score.info['shots'] += 1
            attacker.score.info['hits'] += 1

            attacker.history.content[coord_x][coord_y] = TOUCHED
            defender.board.content[coord_x][coord_y] = HIT

            self.update_sunked_ships( attacker, defender )

            shooted_ship_loc = defender.fleet.get_ship_location( coordinates )
            
            # SUNKEN
            if defender.board.is_sunked_ship( shooted_ship_loc ):
                print(f' Hundido el barco de {defender.name} en {coordinates}')
                
                attacker.history.content[coord_x][coord_y] = SUNKEN
                defender.board.content[coord_x][coord_y] = SUNKEN

                self.sunk_ship( attacker.history.content, defender.board.content, shooted_ship_loc )

            # TOUCHED
            else:
                print(f' Tocado el barco de {defender.name} en {coordinates}')
            
            return True

        else:
            print(f"ERROR SHOT NOT HANDLED")
            print(f"COORD: {coordinates}")
            wait_for_user()


class GameCvC( SinkTheFleet ):
    ''' GameCvC class definition '''

    def __init__( self ):
        ''' GameCvC class constructor '''
        super().__init__('CvC')
        self.player_1 = Computer()
        self.player_2 = Computer()
        if DEEP_DEBUG:
            wait_for_user()
        self.start_time = time()


    def handle_round( self ):
        ''' Handle Computer vs Computer rounds '''
        self.ui.show_header( self.mode, self.round, self.start_time )

        self.handle_player_round( self.player_1, self.player_2 )
        if DEEP_DEBUG:
            wait_for_user()
        
        print()

        self.handle_player_round( self.player_2, self.player_1 )
        if DEEP_DEBUG:
            wait_for_user()
        else:
            sleep( TIME_LAPSE )
        self.new_round()
        

class GamePvE( SinkTheFleet ):
    ''' GamePvE class definition '''

    def __init__( self ):
        ''' GamePvE class constructor '''
        super().__init__('PvE')

        self.ui.show_banner(False)

        self.player_1 = Human()
        self.player_2 = Computer()

        self.start_time = time()

    def handle_round( self ):
        ''' Handle Player vs Computer rounds '''
        self.ui.show_header( self.mode, self.round, self.start_time )
        # PLAYER ROUND
        self.handle_player_round( self.player_1, self.player_2 )
        if DEEP_DEBUG:
            wait_for_user()
        elif isinstance( self.player_1, Computer ):
            sleep( TIME_LAPSE )
        print()
        # COMPUTER ROUND
        self.handle_player_round( self.player_2, self.player_1, show=False )
        if DEEP_DEBUG:
            wait_for_user()
        elif isinstance(self.player_1, Human) and isinstance(self.player_2, Computer):
            print()
            wait_for_user()
        elif isinstance( self.player_2, Computer ):
            sleep( TIME_LAPSE )

        self.new_round()

