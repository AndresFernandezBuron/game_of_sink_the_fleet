#!/usr/bin/env
#-*- coding: utf-8 -*-

"""
Andrés Fernández Burón
2023/10/04

Console game of 'Sink the fleet' with Python 3

File with util functions.
"""

# DEPENDENCIES

import random

from time import time

from os import system
from os import name as os_name

from .consts import SEP_LINE

# UTILE FUNCTIONS


############################################
#### RANDOM FUNCTIONS ######################
############################################

def get_random_value( min_val, max_val ):
    ''' Return a random integer '''
    #random.seed(0)
    #random.seed( time() )
    return random.randint( min_val, max_val )


############################################
#### OUTPUT FUNCTIONS ######################
############################################

def clear_screen():
    ''' Clear console '''
    if os_name == 'nt':
        system('cls')
    else:
        system('clear')

def seconds_to_time_str( seconds:float ):
    ''' Return a time in seconds as a formatted str '''
    seconds = int( seconds )
    minutes = 0
    while seconds > 60:
        minutes += 1
        seconds -=  60
    return f"{f'{minutes} minutos y ' if minutes>0 else ''}{seconds} segundos"


############################################
#### INPUT FUNCTIONS #######################
############################################

def wait_for_user( msg:str='continuar', msg_wrap:str='\n' ):
    ''' Prompt the user for a key enter to continue '''
    input(f'{SEP_LINE}{msg_wrap}\tPulsa ENTER para {msg}{msg_wrap}')


def ask_value( msg='Introduce un valor' ):
    ''' Prompt the user for a non-empty value '''
    value = ''
    while value == '':
        try:
            value = input(f'\n {msg}: ').strip()
        except Exception as e:
            print(f'\n\tExcepción al introducir el valor !!\n\n{e}\n')
    print()
    return value

def ask_coordinates( msg='Introduce las coordenadas X e Y separadas por coma' ):
    ''' Prompt the user for a  coordinates.
    Input:  X and Y coordinates, separated by comma.
    Return: String with X and Y coordinates, separated by comma.
    '''
    coordinates = ''
    while coordinates == '':
        coordinates = ask_value( msg )
        if ',' in coordinates:
            coordinates = coordinates.split(',')
            coordinates[0] = int(coordinates[0])
            coordinates[1] = int(coordinates[1])
            coordinates = tuple( coordinates )
        else:
            coordinates = ''
    return coordinates







