from random import *
import turtle as tr

number_of_turtles = 3
delta = 50
steps_of_time_number = 10000 * 100
ball_size = 3
r_ball = ball_size * 10
dt = 0.1

tr.tracer(20, 60)
arx = [0 for i in range(number_of_turtles)]
ary = [0 for i in range(number_of_turtles)]
arvx = [0 for i in range(number_of_turtles)]
arvy = [0 for i in range(number_of_turtles)]
pool = [tr.Turtle(shape='circle') for i in range(number_of_turtles)]
j = 0
for unit in pool:
    unit.number = j
    unit.turtlesize(ball_size)
    unit.pu()
    unit.vx = random()
    unit.ax = 0
    unit.vy = random()
    unit.ay = 0
    unit.speed(50)
    unit.x = randint(-200, 200)
    unit.y = randint(-200, 200)
    arx[unit.number] = unit.x
    ary[unit.number] = unit.y
    arvx[unit.number] = unit.vx
    arvy[unit.number] = unit.vy
    unit.goto(unit.x, unit.y)
    j += 1

for i in range(steps_of_time_number):
    for unit in pool:
        unit.x += unit.vx * dt + unit.ax * dt ** 2 / 2
        unit.y += unit.vy * dt + unit.ay * dt ** 2 / 2
        unit.ax = 0
        unit.ay = 0
        unit.goto(unit.x, unit.y)
        arx[unit.number] = unit.x
        ary[unit.number] = unit.y
        arvx[unit.number] = unit.vx
        arvy[unit.number] = unit.vy

        for t in range(number_of_turtles):
            if t != unit.number and ((unit.x - arx[t])**2 + (unit.y - ary[t])**2)**0.5 <= r_ball * 2:
                unit.vx, arvx[t] = arvx[t], unit.vx
                unit.vy, arvy[t] = arvy[t], unit.vy



        if abs(unit.x) > 250 - r_ball:
            unit.vx *= -1
        if abs(unit.y) > 250 - r_ball:
            unit.vy *= -1
