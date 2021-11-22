import turtle as tr

tr.shape('turtle')
tr.color('blue', 'black')
tr.pensize(4)
tr.speed(10)


def pr_number(ax: list, ay: list, shift: int):
    size = 30
    tr.pu()
    tr.goto((ax[1] + shift) * size, ay[1] * size)
    tr.pd()
    for i in range(2, len(ax)):
        tr.goto((ax[i] + shift) * size, ay[i] * size)
    tr.pu()
    tr.goto((ax[0] + shift) * size, ay[0] * size)


a0x = (0, 0, 0, 1, 1, 0)
a0y = (0, 0, 2, 2, 0, 0)
a1x = (0, 0, 1, 1)
a1y = (0, 1, 2, 0)
a2x = (0, 0, 1, 1, 0, 1)
a2y = (0, 2, 2, 1, 0, 0)
a3x = (0, 0, 1, 0, 1, 0)
a3y = (0, 0, 1, 1, 2, 2)
a4x = (0, 0, 0, 1, 1, 1)
a4y = (0, 2, 1, 1, 2, 0)
a5x = (0, 0, 1, 1, 0, 0, 1)
a5y = (0, 0, 0, 1, 1, 2, 2)
a6x = (0, 0, 1, 1, 0, 0, 1)
a6y = (0, 1, 1, 0, 0, 1, 2)
a7x = (0, 0, 0, 1, 0)
a7y = (0, 0, 1, 2, 2)
a8x = (0, 0, 0, 1, 1, 0, 0, 1)
a8y = (0, 0, 2, 2, 0, 0, 1, 1)
a9x = (0, 0, 1, 0, 0, 1, 1)
a9y = (0, 0, 1, 1, 2, 2, 1)

ax = [a0x, a1x, a2x, a3x, a4x, a5x, a6x, a7x, a8x, a9x]
ay = [a0y, a1y, a2y, a3y, a4y, a5y, a6y, a7y, a8y, a9y]

strx = '0123456789'
x = int(strx)
k = 0
for i in range(len(strx)):
    j = x // 10 ** (len(strx) - i - 1)
    print('i=', i, 'j=', j)
    x = x % 10 ** (len(strx) - i - 1)
    print(x)
    pr_number(ax[j], ay[j], 2 * i - 10)
