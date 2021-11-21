from random import random
from random import randint
import turtle as tr

tr.shape('turtle')
tr.speed(10)
tr.color('red', 'black')
tr.pensize(2)

for i in range(100):
    tr.forward(random()*50)
    if random() > 0.5:
        tr.right(randint(0, 180))
    else:
        tr.left(randint(0, 180))
