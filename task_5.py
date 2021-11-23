from random import randint
import turtle as tr


number_of_turtles = 10
steps_of_time_number = 100

tr.screensize(canvwidth=200, canvheight=200, bg='red')
pool = [tr.Turtle(shape='circle') for i in range(number_of_turtles)]
tr.setworldcoordinates(-250, -250, 250, 250)
for unit in pool:
    unit.turtlesize(0.5)
    unit.pu()
    unit.speed(50)
    unit.goto(randint(-200, 200), randint(-200, 200))
    unit.right(randint(0, 360))


for i in range(steps_of_time_number):
    for unit in pool:
        unit.forward(1)