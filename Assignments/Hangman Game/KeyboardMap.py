"""
    Author:   Byron Dowling
    Class:    5443 2D Python Gaming

    Stupid thing I had to make so the python module keyboardlayout would
    work the way it is advertised

"""

import pygame
from EnumKeys import Key
from typing import Tuple, Union, Optional, Dict

## This is all somewhat hardcoded to my monitor's dimensions of 1750 x 800

Keyboard_Map = {
    "A": {"xMin": 110, "xMax": 157, "yMin": 622, "yMax": 668, "Clicked": False},
    "B": {"xMin": 380, "xMax": 430, "yMin": 680, "yMax": 730, "Clicked": False},
    "C": {"xMin": 260, "xMax": 310, "yMin": 680, "yMax": 730, "Clicked": False},
    "D": {"xMin": 230, "xMax": 280, "yMin": 622, "yMax": 668, "Clicked": False},
    "E": {"xMin": 210, "xMax": 260, "yMin": 560, "yMax": 610, "Clicked": False},
    "F": {"xMin": 290, "xMax": 340, "yMin": 622, "yMax": 668, "Clicked": False},
    "G": {"xMin": 350, "xMax": 400, "yMin": 622, "yMax": 668, "Clicked": False},
    "H": {"xMin": 410, "xMax": 460, "yMin": 622, "yMax": 668, "Clicked": False},
    "I": {"xMin": 510, "xMax": 560, "yMin": 560, "yMax": 610, "Clicked": False},
    "J": {"xMin": 470, "xMax": 520, "yMin": 622, "yMax": 668, "Clicked": False},
    "K": {"xMin": 530, "xMax": 580, "yMin": 622, "yMax": 668, "Clicked": False},
    "L": {"xMin": 590, "xMax": 640, "yMin": 622, "yMax": 668, "Clicked": False},
    "M": {"xMin": 500, "xMax": 550, "yMin": 680, "yMax": 730, "Clicked": False},
    "N": {"xMin": 440, "xMax": 490, "yMin": 680, "yMax": 730, "Clicked": False},
    "O": {"xMin": 570, "xMax": 620, "yMin": 560, "yMax": 610, "Clicked": False},
    "P": {"xMin": 630, "xMax": 680, "yMin": 560, "yMax": 610, "Clicked": False},
    "Q": {"xMin": 90, "xMax": 140, "yMin": 560, "yMax": 610, "Clicked": False},
    "R": {"xMin": 270, "xMax": 320, "yMin": 560, "yMax": 610, "Clicked": False},
    "S": {"xMin": 170, "xMax": 220, "yMin": 622, "yMax": 668, "Clicked": False},
    "T": {"xMin": 330, "xMax": 380, "yMin": 560, "yMax": 610, "Clicked": False},
    "U": {"xMin": 450, "xMax": 500, "yMin": 560, "yMax": 610, "Clicked": False},
    "V": {"xMin": 320, "xMax": 370, "yMin": 680, "yMax": 730, "Clicked": False},
    "W": {"xMin": 150, "xMax": 200, "yMin": 560, "yMax": 610, "Clicked": False},
    "X": {"xMin": 200, "xMax": 250, "yMin": 680, "yMax": 730, "Clicked": False},
    "Y": {"xMin": 390, "xMax": 440, "yMin": 560, "yMax": 610, "Clicked": False},
    "Z": {"xMin": 140, "xMax": 190, "yMin": 680, "yMax": 730, "Clicked": False}
}

## Work in Progress
pygameKeyMatrix = {
    "A": {"key": Key.A},
    "B": {"key": Key.B},
    "C": {"key": Key.C},
    "D": {"key": Key.D},
    "E": {"key": Key.E},
    "F": {"key": Key.F},
    "G": {"key": Key.G},
    "H": {"key": Key.H},
    "I": {"key": Key.I},
    "J": {"key": Key.J},
    "K": {"key": Key.K},
    "L": {"key": Key.L},
    "M": {"key": Key.M},
    "N": {"key": Key.N},
    "O": {"key": Key.O},
    "P": {"key": Key.P},
    "Q": {"key": Key.Q},
    "R": {"key": Key.R},
    "S": {"key": Key.S},
    "T": {"key": Key.T},
    "U": {"key": Key.U},
    "V": {"key": Key.V},
    "W": {"key": Key.W},
    "X": {"key": Key.X},
    "Y": {"key": Key.Y},
    "Z": {"key": Key.Z}
}

## Dido: Work in Progress
def fetchKey(letter):
     for key, value in pygameKeyMatrix.items():
        if key == letter:
            print(f'Returning {type({value["key"]})} : {value["key"]}')
            # return key
            return value["key"]


def ButtonClicked(CoordPair):
    for key, value in Keyboard_Map.items():
        if CoordPair[0] >= value["xMin"] and CoordPair[0] <= value["xMax"]:
            if CoordPair[1] >= value["yMin"] and CoordPair[1] <= value["yMax"]:
                if value["Clicked"] == False:
                    value["Clicked"] = True
                    return key


if __name__ == '__main__':

    result = ButtonClicked(133,644)
    print(f'The letter clicked is: {result}')

    result = ButtonClicked(201,639)
    print(f'The letter clicked is: {result}')

    result = ButtonClicked(253,640)
    print(f'The letter clicked is: {result}')

    result = ButtonClicked(313,646)
    print(f'The letter clicked is: {result}')
