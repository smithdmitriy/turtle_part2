from random import random
from random import randint
import turtle as tr
import numpy as np

tr.shape('turtle')
tr.color('blue', 'black')
tr.pensize(4)
tr.speed(1)


def prnt(ax: list, ay: list, shift:int):
    size = 80
    tr.goto((ax[0]+shift) * size, ay[0])
    tr.pd
    for i in range(len(ax)):
        tr.goto((ax[i]+shift) * size, ay[i] * size)
    tr.pu()
    tr.goto((ax[0]+shift)*size, ay[0])

a1x = [0, 1, 1]
a1y = [1, 2, 0]
a0x = [0, 0, 1, 1, 0]
a0y = [0, 2, 2, 0, 0]

prnt(a1x, a1y,0)
prnt(a0x, a0y,2)


