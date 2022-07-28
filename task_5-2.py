import pygame
import math
import random


pygame.init()
wigth = 1000
height = 600
balls_window = pygame.display.set_mode((wigth, height))
pygame.display.set_caption('Balls')


number_balls = 10
radius_ball = []
mass_ball = []
x_coord_ball = []
y_coord_ball = []
direction_ball = []
speed_ball = []
speed_angle = []
color_ball = []

for i in range(number_balls + 1):
    radius_ball.append(random.randint(10, 25))
    mass_ball.append(random.randint(5, 50))
    x_coord_ball.append(random.randint(1, wigth - radius_ball[i]))
    y_coord_ball.append(random.randint(1, height - radius_ball[i]))
    speed_ball.append(random.randint(1, 3))
    speed_angle.append(random.random() * math.pi * random.choice([-1, 1]))
    color_ball.append([random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)])

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    balls_window.fill((0, 0, 0))
    for i in range(1, number_balls + 1):
        x_coord_ball[i] += (speed_ball[i] * round(math.cos(speed_angle[i])))
        print(f'X {x_coord_ball[i]}')
        y_coord_ball[i] += (speed_ball[i] * round(math.sin(speed_angle[i])))
        print(f'Y {y_coord_ball[i]}')
        print(f'{speed_angle}')

        # обработка столкновений со стенками

        # левая стена
        if x_coord_ball[i] - radius_ball[i] < 0 and abs(speed_angle[i]) > math.pi / 2:
            x_coord_ball[i] = radius_ball[i]
            speed_angle[i] = math.pi - speed_angle[i]

        # правая стена
        if x_coord_ball[i] + radius_ball[i] > wigth and abs(speed_angle[i]) < math.pi / 2:
            x_coord_ball[i] = wigth - radius_ball[i]
            speed_angle[i] = math.pi - speed_angle[i]

        # верхняя стена
        if y_coord_ball[i] + radius_ball[i] > 0 and speed_angle[i] > -math.pi and speed_angle[i] < 0:
            y_coord_ball[i] = height - radius_ball[i]
            speed_angle[i] = -speed_angle[i]

        #
        # if y_coord_ball[i] + radius_ball[i] > height or y_coord_ball[i] + radius_ball[i] < 0:
        #     print('boom')
        #     y_coord_ball[i] = height - radius_ball[i]

        pygame.draw.circle(balls_window, color_ball[i], (x_coord_ball[i], y_coord_ball[i]), radius_ball[i])

    pygame.time.delay(10)

    pygame.display.update()


