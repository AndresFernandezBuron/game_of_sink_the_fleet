#!/usr/bin/env
#-*- coding: utf-8 -*-


"""
Andrés Fernández Burón
2023/10/04

Console game of 'Sink the fleet' with Python 3

Main file of the game.
"""

from game_of_sink_the_fleet.SinkTheFleet import *


# THE GAME START

game = GameCvC()
#game = GamePvE()

# THE GAME LOOP
while game.winner == False:
    game.handle_round()



# PLAYER 1 WINS
if game.player_1 == game.winner:
    loser = game.player_2
# PLAYER 2 WINS
else:
    loser = game.player_1

game.ui.show_final_screen(game.mode, game.round, game.start_time, game.winner, loser )



from sys import exit
exit(0)

