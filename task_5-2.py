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

number_balls = 1  # Количество шаров
radius_ball = []
mass_ball = []
x_coord_ball = []
y_coord_ball = []
speed_ball = []
speed_angle = []
color_ball = []

for i in range(number_balls + 1):  # Генерация листов с характеристиками шаров
    radius_ball.append(random.randint(50, 50))  # Радиус шара
    mass_ball.append(random.randint(5, 50))  # Масса шара
    x_coord_ball.append(random.randint(1, width - radius_ball[i]))  # X-координата
    y_coord_ball.append(random.randint(1, height - radius_ball[i]))  # Y-координата
    speed_ball.append(random.random())  # Скорость шара
#    speed_angle.append(random.random() * PI * random.choice([-1, 1]))  # Угол скорости относительно оси 0X, -Пи до Пи
    speed_angle.append(PI/4)
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
    for i in range(1, number_balls + 1):
        x_coord_ball[i] = new_coord_x(x_coord_ball[i], speed_ball[i], speed_angle[i])
        y_coord_ball[i] = new_coord_y(y_coord_ball[i], speed_ball[i], speed_angle[i])

        print(speed_angle[i] * 180 / PI)

        # обработка столкновений со стенками

        # Левая стена
        if x_coord_ball[i] - radius_ball[i] < 0 and math.cos(speed_angle[i]) < 0:
            speed_angle[i] = (PI - speed_angle[i]) % (2 * PI)

        # Правая стена
        if x_coord_ball[i] + radius_ball[i] > width and math.cos(speed_angle[i]) > 0:
            speed_angle[i] = (PI - speed_angle[i]) % (2 * PI)

        # Верхняя стена
        if y_coord_ball[i] - radius_ball[i] < 0 and math.sin(speed_angle[i]) < 0:
            speed_angle[i] = (-speed_angle[i]) % (2 * PI)

        # Нижняя стена
        if y_coord_ball[i] + radius_ball[i] > height and math.sin(speed_angle[i]) > 0:
            speed_angle[i] = (-speed_angle[i]) % (2 * PI)

        # Обработка столкновения шаров между собой

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
                bb = (math.atan((y_coord_ball[j] - y_coord_ball[i])/(x_coord_ball[j] - x_coord_ball[i])) + 2*PI) % 2 * PI

                speed_angle[i], speed_angle[j] = speed_angle[j], speed_angle[i]
                speed_ball[i], speed_ball[j] = speed_ball[j], speed_ball[i]
                pass

        pygame.draw.circle(balls_window, color_ball[i], (x_coord_ball[i], y_coord_ball[i]), radius_ball[i])

    pygame.time.delay(3)

    pygame.display.update()
