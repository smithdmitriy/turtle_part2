import turtle as tr

tr.shape('turtle')
tr.color('blue', 'black')
tr.pensize(2)
tr.speed(10)

x = -300
y = 0

tr.goto(300, 0)
tr.goto(-300, 0)
Vx = 3
Vy = 8
dt = 0.5
ay = 0.2
ax = 0.005

while Vx > 0.1:
    tr.goto(x, y)
    x += Vx * dt
    y += Vy * dt - ay * dt ** 2 / 2
    Vy += -ay * dt
    Vx += -ax * dt
    print(round(Vx, 2))
    if y < 0:
        Vy = -Vy / 1.4
        y = 0
        Vx = 0.8 * Vx
