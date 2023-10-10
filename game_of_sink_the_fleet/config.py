#!/usr/bin/env
#-*- coding: utf-8 -*-

"""
Andrés Fernández Burón
2023/10/04

Console game of 'Sink the fleet' with Python 3

File with Constants to configure the game.
"""

# Flags for debuggin
DEBUG = True
DEBUG = False

DEEP_DEBUG = True
DEEP_DEBUG = False

# The side of the game board
# EJ: 10 --> 10*10 --> (10,10)
BOARD_SIZE = 10

# Number of ships = SHIPS_SIZES_COUNT!
# EJ: 4! --> 10
SHIPS_SIZES_COUNT = 4 

# Make the game less interactive
INTERACTIVE = True
#INTERACTIVE = False

# Computer's shot per round = COMPUTER_SHOTS_PER_ROUND * DIFFICULTY
# EJ: 5 * 1 --> 5
COMPUTER_SHOTS_PER_ROUND = 1
DIFFICULTY = 1 #10

# Time sleep when the Computer plays versus himself
TIME_LAPSE = 1
TIME_LAPSE = .5
TIME_LAPSE = .2
#TIME_LAPSE = 0
