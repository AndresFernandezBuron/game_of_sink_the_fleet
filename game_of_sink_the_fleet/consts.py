#!/usr/bin/env
#-*- coding: utf-8 -*-

"""
Andrés Fernández Burón
2023/10/04

Console game of 'Sink the fleet' with Python 3

File with game Constants.
"""

from .config import BOARD_SIZE, SHIPS_SIZES_COUNT, DIFFICULTY, COMPUTER_SHOTS_PER_ROUND

PATTERN_1 = '='
PATTERN_2 = '_'
PATTERN_3 = '-'
HEAD_LINE = PATTERN_1 * BOARD_SIZE * 7
SEP_LINE = PATTERN_2 * BOARD_SIZE * 7
PLAY_LINE = PATTERN_3 * BOARD_SIZE * 7

PLAYER = u'👤' #'p1'
COMPUTER = u'🤖' #'c1'

WATER = u'🟦' #'~'
SHIP = u'⚓' #'#'

HIT =  u'🔥' #'o'
SUNKEN = u'💀' #'*'

FAIL = u'❌' #'x'
TOUCHED = u'💥' #'t'

WINNER = u'😎' #'W'
LOSER = u'😓' #'L'


GAME_BANNER = """     _   _                 _ _        _          __ _       _        
    | | | |_   _ _ __   __| (_)_ __  | | __ _   / _| | ___ | |_ __ _ 
    | |_| | | | | '_ \ / _` | | '__| | |/ _` | | |_| |/ _ \| __/ _` |
    |  _  | |_| | | | | (_| | | |    | | (_| | |  _| | (_) | || (_| |
    |_| |_|\__,_|_| |_|\__,_|_|_|    |_|\__,_| |_| |_|\___/ \__\__,_|
"""

GAME_INFO = """
 Andrés Fernández Burón
 2023/10/04

 Console game of 'Sink the fleet' with Python 3
 Player VS Computer
"""

ship_list = '\n\t'.join([f'{SHIPS_SIZES_COUNT-i} barcos de {i+1} de eslora' for i in range(SHIPS_SIZES_COUNT)])

GAME_DESC = f"""
 El juego sigue la mecánica de turnos y el objetivo es hundir los barcos del oponente.

 La Máquina empieza la partida y tiene 1*N tiradas por turno.
 Dónde N es el nivel de dificultad (1-N).
 La dificultad actual es {DIFFICULTY}, por lo que la máquina dispara {COMPUTER_SHOTS_PER_ROUND*DIFFICULTY} veces por turno.

 Hay dos jugadores y cada uno tiene un tablero de {BOARD_SIZE}*{BOARD_SIZE} en el que coloca sus barcos.

        {ship_list}

 Además, si el oponente acierta en algún barco, se visualiza en dicho tablero.

 Por otra parte, el jugador tiene un segundo tablero que le sirve para visualizar los  aciertos y fallos que ha tiene durante la partida.

 Gana el que hunde todos los barcos del otro jugador.
"""
