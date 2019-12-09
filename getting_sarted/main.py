#!/usr/bin/env pybricks-micropython

import random

from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase

motor_piedra = Motor(Port.A)
motor_papel = Motor(Port.B)
motor_tijera = Motor(Port.C)

motors = [motor_papel, motor_piedra, motor_tijera]

GRADOS = 90

def reset():
    for motor in motors:
        motor.track_target(0)
    
    wait(500)

def jugar_piedra():
    pass

def jugar_papel():
    for motor in motors:
        motor.track_target(GRADOS)

    wait(500)

def jugar_tijera():
    motor_tijera.track_target(GRADOS)
    motor_papel.track_target(GRADOS)

    wait(500)

jugadas = [jugar_papel, jugar_tijera, jugar_piedra]
jugadas_names = ["papel", "tijera", "piedra"]
jugadas_sonidos = ["papel.wav", "tijera.mp3", "piedra.mp3"]
pulsador = TouchSensor(Port.S1)

while True:
    if pulsador.pressed():
        n = random.randint(0, len(jugadas)-1)
        jugadas[n]()
        print(jugadas_names[n])
        reset()
        brick.sound.file(jugadas_sonidos[n])