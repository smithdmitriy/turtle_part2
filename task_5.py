from random import *
import turtle as tr

number_of_turtles = 5
delta = 50
steps_of_time_number = 10000
tr.tracer(2, 60)
tr.pu()
tr.speed(0)
tr.goto(-250, -250)
tr.pd()
tr.goto(-250, 250)
tr.goto(250, 250)
tr.goto(250, -250)
arx = [0 for i in range(10)]
ary = [0 for i in range(10)]
pool = [tr.Turtle(shape='circle') for i in range(number_of_turtles)]
j = 0
for unit in pool:

    unit.number = j
    unit.turtlesize(1.5)
    unit.pu()
    unit.vx = random()
    print(unit.vx)
    unit.ax = 0
    unit.vy = random()
    print(unit.vy)
    unit.ay = 0
    unit.speed(50)
    unit.x = randint(-200, 200)

    unit.y = randint(-200, 200)
    arx[unit.number] = unit.x
    ary[unit.number] = unit.y
    unit.goto(unit.x, unit.y)
    j += 1

for i in range(steps_of_time_number):
    for unit in pool:
        for t in range(number_of_turtles):
            if t != unit.number and abs(unit.x - arx[t]) < delta and abs(unit.y - ary[t]) < delta:

                unit.ax = (1 / (unit.x - arx[t])**2)
                print(unit.number, unit.ax)
                unit.ay = (1 / (unit.y - ary[t]))
                print(unit.number, unit.ay, t)

            if t != unit.number and abs(unit.x - arx[t]) < delta and abs(unit.y - ary[t]) < delta:
                unit.ax = (1 / (unit.x - arx[t]))
                print(unit.number, unit.ax)
                unit.ay = (1 / (unit.y - ary[t]))
                print(unit.number, unit.ay, t)

        unit.x += unit.vx + unit.ax
        unit.y += unit.vy + unit.ay
        unit.ax = 0
        unit.ay = 0
        unit.goto(unit.x, unit.y)
        arx[unit.number] = unit.x
        ary[unit.number] = unit.y

        if abs(unit.x) > 250:
            unit.vx *= -1
        if abs(unit.y) > 250:
            unit.vy *= -1
