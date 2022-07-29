import pygame
import math
import random


pygame.init()
wigth = 1000
height = 600
balls_window = pygame.display.set_mode((wigth, height))
pygame.display.set_caption('Balls')
PI = math.pi

number_balls = 10
radius_ball = []
mass_ball = []
x_coord_ball = []
y_coord_ball = []
speed_ball = []
speed_angle = []
color_ball = []

for i in range(number_balls + 1):
    radius_ball.append(random.randint(10, 50))
    mass_ball.append(random.randint(5, 50))
    x_coord_ball.append(random.randint(1, wigth - radius_ball[i]))
    y_coord_ball.append(random.randint(1, height - radius_ball[i]))
    speed_ball.append(random.randint(1, 3))
    speed_angle.append(random.random() * PI * random.choice([-1, 1]))
    color_ball.append([random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)])

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    balls_window.fill((0, 0, 0))
    for i in range(1, number_balls + 1):
        x_coord_ball[i] += (speed_ball[i] * math.cos(speed_angle[i]))
        y_coord_ball[i] += (speed_ball[i] * math.sin(speed_angle[i]))

        # обработка столкновений со стенками

        # левая стена
        if x_coord_ball[i] - radius_ball[i] < 0 and math.cos(speed_angle[i]) < 0:
            speed_angle[i] = (PI - speed_angle[i]) % (2 * (PI))

        # правая стена
        if x_coord_ball[i] + radius_ball[i] > wigth and math.cos(speed_angle[i]) > 0:
            speed_angle[i] = (PI - speed_angle[i]) % (2 * (PI))

        # верхняя стена
        if y_coord_ball[i] - radius_ball[i] < 0 and math.sin(speed_angle[i]) < 0:
            speed_angle[i] = (-speed_angle[i]) % (2 * (PI))

        # нижняя стена
        if y_coord_ball[i] + radius_ball[i] > height and math.sin(speed_angle[i]) > 0:
            speed_angle[i] = (-speed_angle[i]) % (2 * (PI))

        pygame.draw.circle(balls_window, color_ball[i], (x_coord_ball[i], y_coord_ball[i]), radius_ball[i])

    pygame.time.delay(3)

    pygame.display.update()


