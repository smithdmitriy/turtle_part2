from random import random
from random import randint
import turtle as tr
import numpy as np

tr.shape('turtle')
tr.color('blue', 'black')
tr.pensize(4)
tr.speed(1)

def prnt(ax:list, ay:list):
    for i in range(len(ax)):
        tr.goto(ax[i]*40, ay[i]*40)
    tr.penup()
    tr.goto(0,0)

a0x = [0, 1, 1, 0]
a0y = [2, 2, 0, 0]

prnt(a0x, a0y)

