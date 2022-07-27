import pygame
import math
import random


pygame.init()
wigth = 700
height = 500
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

for i in range(number_balls):
    radius_ball.append(random.randint(10, 25))
    mass_ball.append(random.randint(5, 50))
    x_coord_ball.append(random.randint(1, height - radius_ball[i]))
    y_coord_ball.append(random.randint(1, wigth - radius_ball[i]))
    speed_ball.append(random.randint(1, 3))
    speed_angle.append(random.randint(0, 10))
    color_ball.append([random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)])

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    balls_window.fill((0, 0, 0))
    for i in range(1, number_balls):
        x_coord_ball[i] += (speed_ball[i] * math.cos(speed_angle[i]))
        y_coord_ball[i] += (speed_ball[i] * math.sin(speed_angle[i]))
        if abs(x_coord_ball[i]) >= height:
            x_coord_ball[i] = int(height)


        pygame.draw.circle(balls_window, color_ball[i], (x_coord_ball[i], y_coord_ball[i]), radius_ball[i])

    pygame.time.delay(10)

    pygame.display.update()


