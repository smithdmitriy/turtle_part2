import turtle as tr

tr.shape('turtle')
tr.color('blue', 'black')
tr.pensize(4)
tr.speed(5)


def pr_number(ax: list, ay: list, shift: int):
    size = 30
    tr.pu()
    tr.goto((ax[1] + shift) * size, ay[1] * size)
    tr.pd()
    for i in range(2, len(ax)):
        tr.goto((ax[i] + shift) * size, ay[i] * size)
    tr.pu()
    tr.goto((ax[0] + shift) * size, ay[0] * size)

input = open('task_3', 'r')
ax = []
ay = []
for i in range(10):

    stx = input.readline()
    stx = stx[7:len(stx) - 2]
    stx = stx.replace(', ', '')
    tplx = []
    for i in range(len(stx)):
        tplx.append(int(stx[i]))

    sty = input.readline()
    sty = sty[7:len(sty)- 2]
    sty = sty.replace(', ', '')
    tply = []
    for i in range(len(sty)):
        tply.append(int(sty[i]))

    ax.append(tuple(tplx))
    ay.append(tuple(tply))

strx = '01234567890'
x = int(strx)
k = 0
for i in range(len(strx)):
    j = x // 10 ** (len(strx) - i - 1)
    x = x % 10 ** (len(strx) - i - 1)
    pr_number(ax[j], ay[j], 2 * i - 10)
