import pygame
import math
import random


def new_coord_x(coord: float, speed: float, angle: float):
    coord += speed * math.cos(angle)
    return coord


def new_coord_y(coord: float, speed: float, angle: float):
    coord += speed * math.sin(angle)
    return coord


def ball_distance(x1: float, y1: float, x2: float, y2: float):
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5


pygame.init()
width = 500  # Ширина поля
height = 500  # Высота поля
balls_window = pygame.display.set_mode((width, height))
pygame.display.set_caption('Balls')
PI = math.pi

number_balls = 2  # Количество шаров
radius_ball = []
mass_ball = []
x_coord_ball = []
y_coord_ball = []
speed_ball = []
speed_angle = []
color_ball = []

for i in range(number_balls + 1):  # Генерация листов с характеристиками шаров
    radius_ball.append(random.randint(15, 50))  # Радиус шара
    mass_ball.append(radius_ball[i]**3)  # Масса шара
    x_coord_ball.append(random.randint(1, width - radius_ball[i]))  # X-координата
    y_coord_ball.append(random.randint(1, height - radius_ball[i]))  # Y-координата
    speed_ball.append(random.random())  # Скорость шара
    speed_angle.append(random.random() * 2 * PI)  # Угол скорости относительно оси 0X, -Пи до Пи
    color_ball.append([  # Цвет шара
        random.randint(0, 255),  # Красный
        random.randint(0, 255),  # Зеленый
        random.randint(0, 255)  # Синий
    ])

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    balls_window.fill((0, 0, 0))

    # Движение шаров
    for i in range(1, number_balls + 1):
        x_coord_ball[i] = new_coord_x(x_coord_ball[i], speed_ball[i], speed_angle[i])
        y_coord_ball[i] = new_coord_y(y_coord_ball[i], speed_ball[i], speed_angle[i])

        # обработка столкновений со стенками

    # Столкновение со стенами
    for i in range(1, number_balls + 1):
        # Левая стена
        if x_coord_ball[i] - radius_ball[i] < 0 and math.cos(speed_angle[i]) < 0:
            speed_angle[i] = (PI - speed_angle[i])
        # Правая стена
        if x_coord_ball[i] + radius_ball[i] > width and math.cos(speed_angle[i]) > 0:
            speed_angle[i] = (PI - speed_angle[i])
        # Верхняя стена
        if y_coord_ball[i] - radius_ball[i] < 0 and math.sin(speed_angle[i]) < 0:
            speed_angle[i] = (-speed_angle[i])
        # Нижняя стена
        if y_coord_ball[i] + radius_ball[i] > height and math.sin(speed_angle[i]) > 0:
            speed_angle[i] = (-speed_angle[i])

        speed_angle[i] %= (2 * PI)
        if speed_angle[i] > PI:
            speed_angle[i] -= 2 * PI

    # Обработка столкновения шаров между собой
    for i in range(1, number_balls + 1):
        for j in range(i + 1, number_balls + 1):  # j - другие шары
            distance = ball_distance(
                x_coord_ball[i],
                y_coord_ball[i],
                x_coord_ball[j],
                y_coord_ball[j])
            new_distance = ball_distance(
                new_coord_x(x_coord_ball[i], speed_ball[i], speed_angle[i]),
                new_coord_y(y_coord_ball[i], speed_ball[i], speed_angle[i]),
                new_coord_x(x_coord_ball[j], speed_ball[j], speed_angle[j]),
                new_coord_y(y_coord_ball[j], speed_ball[j], speed_angle[j]))

            if (radius_ball[i] + radius_ball[j]) >= distance > new_distance:
                # Угол поворота луча между центрами шаров на центр второго шара
                bb = (math.atan((y_coord_ball[j] - y_coord_ball[i]) / (x_coord_ball[j] - x_coord_ball[i]))) % PI
                if not - PI / 2 < bb < PI / 2:
                    bb -= PI
                print(bb * 180 / PI)
                # Угол луча между центрами шаров до направления движения
                w1 = speed_angle[i] - bb
                w2 = speed_angle[j] - bb

                vwt1 = speed_ball[i] * math.sin(w1)

                vwt2 = speed_ball[j] * math.sin(w2)

                vw1 = (2 * mass_ball[j] * speed_ball[j] * math.cos(w2) +
                       (mass_ball[i] - mass_ball[j]) * speed_ball[i] * math.cos(w1)) / (mass_ball[i] + mass_ball[j])

                vw2 = (2 * mass_ball[i] * speed_ball[i] * math.cos(w1) +
                       (mass_ball[j] - mass_ball[i]) * speed_ball[j] * math.cos(w2)) / (mass_ball[j] + mass_ball[i])

                w1 = math.atan(vwt1 / vw1)
                if vw1 < 0:
                    w1 += PI
                w2 = math.atan(vwt2 / vw2)
                if vw2 < 0:
                    w2 += PI

                speed_ball[i] = (vw1 ** 2 + vwt1 ** 2) ** 0.5
                speed_ball[j] = (vw2 ** 2 + vwt2 ** 2) ** 0.5

                speed_angle[i] = bb + w1
                speed_angle[j] = bb + w2

        pygame.draw.circle(balls_window, color_ball[i], (x_coord_ball[i], y_coord_ball[i]), radius_ball[i])

    # обработка магнитного взаимодействия шаров
    for i in range(1, number_balls + 1):
        for j in range(i + 1, number_balls + 1):
            distance = ball_distance(
                x_coord_ball[i],
                y_coord_ball[i],
                x_coord_ball[j],
                y_coord_ball[j])
            if distance <= 4 * (radius_ball[i]+radius_ball[j]):
                f_mag = mass_ball[i] * mass_ball[j] / distance**2 * 0.000000001
                bb = (math.atan((y_coord_ball[j] - y_coord_ball[i]) / (x_coord_ball[j] - x_coord_ball[i]))) % PI
                if not - PI / 2 < bb < PI / 2:
                    bb -= PI
                # Угол луча между центрами шаров до направления движения
                w1 = speed_angle[i] - bb
                w2 = speed_angle[j] - bb

                vwt1 = speed_ball[i] * math.sin(w1)

                vwt2 = speed_ball[j] * math.sin(w2)

                vw1 = f_mag + math.cos(w2)

                vw2 = f_mag + math.cos(w1)

                w1 = math.atan(vwt1 / vw1)
                if vw1 < 0:
                    w1 += PI
                w2 = math.atan(vwt2 / vw2)
                if vw2 < 0:
                    w2 += PI

                #speed_ball[i] = (vw1 ** 2 + vwt1 ** 2) ** 0.5
                #speed_ball[j] = (vw2 ** 2 + vwt2 ** 2) ** 0.5

                speed_ball[i] -= f_mag
                speed_ball[j] -= f_mag

                #speed_angle[i] = bb + w1*f_mag
                #speed_angle[j] = bb + w2*f_mag

                print(f'{f_mag=} {vwt1 =} {vw1=} {speed_ball[i] =} {speed_angle[i] = }')


    pygame.time.delay(1)

    pygame.display.update()
