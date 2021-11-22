import turtle as tr


def convert_str_to_turple(s: str) -> tuple:
    s = s[7:len(s) - 2]
    s = s.replace(', ', '')
    tpl = []
    for i in range(len(s)):
        tpl.append(int(s[i]))
    return tuple(tpl)


def pr_number(ax: list, ay: list, shift: int):
    size = 30
    tr.pu()
    tr.goto((ax[1] + shift) * size, ay[1] * size)
    tr.pd()
    for i in range(2, len(ax)):
        tr.goto((ax[i] + shift) * size, ay[i] * size)
    tr.pu()
    tr.goto((ax[0] + shift) * size, ay[0] * size)


tr.shape('turtle')
tr.color('blue', 'black')
tr.pensize(4)
tr.speed(5)

input = open('task_3', 'r')
ax = []
ay = []
for i in range(10):
    stx = input.readline()
    sty = input.readline()
    ax.append(convert_str_to_turple(stx))
    ay.append(convert_str_to_turple(sty))
strx = '01234567890'
x = int(strx)
for i in range(len(strx)):
    j = x // 10 ** (len(strx) - i - 1)
    x = x % 10 ** (len(strx) - i - 1)
    pr_number(ax[j], ay[j], 2 * i - 10)
