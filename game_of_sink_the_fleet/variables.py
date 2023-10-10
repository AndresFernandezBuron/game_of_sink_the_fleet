#!/usr/bin/env
#-*- coding: utf-8 -*-

"""
Andrés Fernández Burón
2023/10/04

Console game of 'Sink the fleet' with Python 3


File with program variables which change during the game is running.
"""

# DEPENDENCIES
import numpy as np

# SUBMODULES
from .config import BOARD_SIZE
from .consts import WATER

# GAME VARS

# ROUND VARS

global current_is_player
current_is_player = False   # <-- If False, Player starts the game

global round_counter
round_counter = 0

# PLAYER VARS

'''
global player_name
player_name = 'Andrés'





# GAME BOARDS
board_shape = (BOARD_SIZE, BOARD_SIZE)




global computer_board
computer_board = np.full( shape=board_shape, fill_value=WATER )

global player_board, hidden_board
player_board = np.full( shape=board_shape, fill_value=WATER )
hidden_board = np.full( shape=board_shape, fill_value=WATER )
'''

