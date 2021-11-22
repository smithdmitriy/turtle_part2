import turtle as tr

tr.shape('turtle')
tr.color('blue', 'black')
tr.pensize(1)
tr.speed(10)

x = -300
y = 0
tr.pu()
tr.goto(-300,0)
tr.pd()
Vx = 3
Vy = 8
dt = 0.5
ay = 0.2

while Vx>0:
    tr.goto(x, y)
    x += Vx * dt
    y += Vy * dt - ay * dt ** 2 / 2
    Vy += -ay * dt
    print(y, Vy)
    if y < 0:
        Vy = -Vy/1.4
        y = 0
    if abs(Vy) < 0.01:
        Vx = 0.5*Vx-0.1



