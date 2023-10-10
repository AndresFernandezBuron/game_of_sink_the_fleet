# game_of_sink_the_fleet
---------------------------

>
> Andrés Fernández Burón
> 2023/10/04
> 
> Game of 'Sink the fleet' with Python 3
> with player vs computer, and computer vs computer modes.
>

---------------------------

<pre>
 _   _                 _ _      
| | | |_   _ _ __   __| (_)_ __ 
| |_| | | | | '_ \ / _` | | '__|
|  _  | |_| | | | | (_| | | |   
|_| |_|\__,_|_| |_|\__,_|_|_|   
                                
 _          __ _       _        
| | __ _   / _| | ___ | |_ __ _ 
| |/ _` | | |_| |/ _ \| __/ _` |
| | (_| | |  _| | (_) | || (_| |
|_|\__,_| |_| |_|\___/ \__\__,_|
                
</pre>

---------------------------

Juego de HUndir la flota para consola

El juego sigue la mecánica de turnos y el objetivo es hundir los barcos del oponente.

La Máquina empieza la partida y tiene 1*N tiradas por turno.
Dónde N es el nivel de dificultad (1-N).
La dificultad actual es 1, por lo que la máquina dispara 1 veces por turno.

Hay dos jugadores y cada uno tiene un tablero de 10*10 en el que coloca sus barcos.

    4 barcos de 1 de eslora
	3 barcos de 2 de eslora
	2 barcos de 3 de eslora
	1 barcos de 4 de eslora

Además, si el oponente acierta en algún barco, se visualiza en dicho tablero.

Por otra parte, el jugador tiene un segundo tablero que le sirve para visualizar los  aciertos y fallos que ha tiene durante la partida.

Gana el que hunde todos los barcos del otro jugador.

-------------------------------
