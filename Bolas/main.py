import pygame as pg
import random as r

pg.init()

screen_x_size = 800
screen_y_size = 600

screen = pg.display.set_mode((screen_x_size, screen_y_size))

pg.display.set_caption("Bouncing ball")

# ball
ballPath = 'Spaceship/img_downsized/ball.png'
ballPath_ = 'ball.png'
ballImg = pg.image.load(ballPath)

steps_x = 0.2
steps_y = 0.2

ball_x = r.randint(0, screen_x_size)
ball_y = r.randint(0, screen_y_size)

def ball_pos(x, y):
    screen.blit(ballImg, (x, y))

isActiva = True

while isActiva:
    screen.fill((255, 255, 255))
    for event in pg.event.get():
        if event.type == pg.QUIT:
            isActiva = False
    if ball_x > screen_x_size - ballImg.get_width() or ball_x < 0:
        steps_x *= -1
    if ball_y > screen_y_size - ballImg.get_height() or ball_y < 0:
        steps_y *= -1

    ball_x += steps_x
    ball_y += steps_y
    ball_pos(ball_x, ball_y)
    
    pg.display.flip()
