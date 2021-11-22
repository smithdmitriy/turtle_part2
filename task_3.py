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

input = open('task_3', 'r')

ax = []
ay = []
for i in range(18):
    stx = input.readline()
    sty = input.readline()
    ax.append(stx[7:len(stx)-2])
    ay.append(sty[7:len(sty)-2])
print(ax)
#ax = [a0x, a1x, a2x, a3x, a4x, a5x, a6x, a7x, a8x, a9x]
#ay = [a0y, a1y, a2y, a3y, a4y, a5y, a6y, a7y, a8y, a9y]

strx = '0123456789'
x = int(strx)
k = 0
for i in range(len(strx)):
    j = x // 10 ** (len(strx) - i - 1)
    print('i=', i, 'j=', j)
    x = x % 10 ** (len(strx) - i - 1)
    print(x)
    pr_number(ax[j], ay[j], 2 * i - 10)
