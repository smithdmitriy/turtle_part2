from random import randint
import turtle as tr


number_of_turtles = 10
steps_of_time_number = 100

pool = [tr.Turtle(shape='circle') for i in range(number_of_turtles)]
for unit in pool:
    unit.turtlesize(1)
    unit.pu()
    unit.v = randint(1,12)
    unit.speed(50)
    unit.goto(randint(-200, 200), randint(-200, 200))
    unit.right(randint(0, 360))



for i in range(steps_of_time_number):
    for unit in pool:
        unit.forward(unit.v)