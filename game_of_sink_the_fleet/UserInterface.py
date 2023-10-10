#!/usr/bin/env
#-*- coding: utf-8 -*-

"""
Andrés Fernández Burón
2023/10/04

Console game of 'Sink the fleet' with Python 3


File with UserInterface class for the game.
"""

# DEPENDENCIES

from time import time

# SUBMODULES
from .config import *
from .consts import *

from .utils import clear_screen, wait_for_user, seconds_to_time_str

from .GameBoard import *
from .Player import *



class UserInterface:
    ''' UserInterface class definition '''

    # STATIC VARS
    tab = '  '

    def __init__( self ):
        ''' UserInterface class constructor '''

    # METHODS:

    def show_banner( self, first_screen:bool=True ):
        ''' Show de game start banner '''
        clear_screen()
        print(f"{HEAD_LINE}\n{GAME_BANNER}\n{HEAD_LINE}")
        print( GAME_INFO )
        print( SEP_LINE )
        if first_screen:
            print( GAME_DESC )
            wait_for_user('empezar la partida')

    def show_header( self, mode:str, round_counter:int, start_time:float ):
        ''' Show the game screen header '''
        time_count = time() - start_time
        time_str = seconds_to_time_str(time_count)
        clear_screen()
        print(f"{HEAD_LINE}\n\tHUNDIR LA FLOTA - {mode}\n{HEAD_LINE}")
        print(f" LEVEL:  {DIFFICULTY}\tROUND:  {round_counter + 1}\tTIME: {time_str}")
        print()

    def show_player_header( self, player:Player ):
        ''' Show player round header '''
        print(f"{PLAY_LINE}\n {player.char} {player.name.upper()} \n{PLAY_LINE}")

    def join_boards( self, game_board:GameBoard, history_board:Board ):
        ''' Join user boards horizontaly '''
        
        main_board = game_board.get_as_str_list()
        hist_board = history_board.get_as_str_list()

        boards = []
        data = zip( main_board, hist_board )
        for line_1, line_2 in data:
            boards.append(f"{self.tab}{line_1}{self.tab*2}{line_2}")
        return boards

    def show_boards( self, player:Player ):
        ''' Show user boards '''

        boards = self.join_boards( player.board, player.history )
        user_info = player.score.get_info()
        user_info.insert( 0, '')

        for i in range( len(boards) ):
            print(f"{boards[i]}{self.tab*2}{user_info[i] if i<len(user_info) else ''}")

    def show_final_screen(self, mode:str, round:int, start_time:float, winner:Player, loser:Player):
        ''' Show Winner info at the end of the game '''
        self.show_header(mode, round, start_time)
        self.show_player_header( winner )
        self.show_boards( winner )
        print()
        self.show_player_header( loser )
        self.show_boards( loser )

        print(f'\n THE WINNER IS {winner.name} {WINNER} !!')
        print(f' {loser.name} HAS LOSE {LOSER} !!\n')
