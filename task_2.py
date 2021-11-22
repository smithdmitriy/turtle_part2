import turtle as tr

tr.shape('turtle')
tr.color('blue', 'black')
tr.pensize(4)
tr.speed(1)


def pr_number(ax: list, ay: list, shift: int):
    size = 40
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
a4x = (0, 0, 1, 0, 1, 1)
a4y = (0, 2, 1, 1, 2, 0)
a5x = (0, 0, 1, 1, 0, 0, 1)
a5y = (0, 0, 0, 1, 1, 2, 2)

ax = [a1x, a2x, a3x, a4x, a5x]
ay = [a1y, a2y, a3y, a4y, a5y]

strx = '124'
x = int(strx)
k = 0
for i in range(len(strx)-1, -1, -1):
    j = x // 10**(i)
    x %= 10**(i)
    print(j)
    x = int(strx)//10
    pr_number(ax[j], ay[j], 2*k)
    k += 1


'''
while i in len(x):
    prnt(a5x, a5y, 0)



a6x = [0,
a6y = [0,
a7x = [0,
a7y = [0,
a8x = [0,
a8y = [0,
a9x = [0,
a9y = [0,
'''

# prnt(a5x, a5y, 0)
#pr_number(a1x, a1y, 2)
# prnt(a3x, a3y, 4)
