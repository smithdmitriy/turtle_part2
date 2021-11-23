from random import randint
import turtle as tr

tr.tracer(40, 24)
number_of_turtles = 160
steps_of_time_number = 10000
tr.pu()
tr.speed(0)
tr.goto(-250, -250)
tr.pd()
tr.goto(-250, 250)
tr.goto(250, 250)
tr.goto(250, -250)
tr.goto(-250, -250)

pool = [tr.Turtle(shape='circle') for i in range(number_of_turtles)]
for unit in pool:
    unit.turtlesize(0.5)
    unit.pu()
    unit.vx = randint(-4, 4)
    print(unit.vx)
    unit.vy = randint(-4, 4)
    print(unit.vy)
    unit.speed(50)
    unit.x = randint(-200, 200)
    unit.y = randint(-200, 200)
    unit.goto(unit.x, unit.y)


for i in range(steps_of_time_number):
    for unit in pool:
        unit.x += unit.vx
        unit.y += unit.vy
        unit.goto(unit.x, unit.y)
        if abs(unit.x) > 250:
            print(unit.pos())
            unit.vx *= -1
        if abs(unit.y) > 250:
            unit.vy *= -1
            print(unit.pos())
