import pygame as pg
import random as r
import math

pg.init()

screen_x_size = 800
screen_y_size = 600

screen = pg.display.set_mode((screen_x_size, screen_y_size))

pg.display.set_caption("Bouncing ball")

# ball
ballPath = 'Spaceship/img_downsized/ball.png'
ballPath_ = 'ball.png'
ballImg = pg.image.load(ballPath)

# -- Bola 1 --
ball_x = r.randint(0, screen_x_size)
ball_y = r.randint(0, screen_y_size)

steps_x = 0.2
steps_y = 0.2

# -- Bola 2 --
ball_x_2 = r.randint(0, screen_x_size)
ball_y_2 = r.randint(0, screen_y_size)

steps_x2 = -0.2
steps_y2 = 0.2

def ball_pos(x, y):
    screen.blit(ballImg, (x, y))

def colision(x1, y1, x2, y2, radio):
    """Devuelve True si las dos pelotas chocan."""
    distancia = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
    return distancia <= 2 * radio

isActiva = True

while isActiva:
    screen.fill((255, 255, 255))
    for event in pg.event.get():
        if event.type == pg.QUIT:
            isActiva = False
    if ball_x_2 > screen_x_size - ballImg.get_width() or ball_x_2 < 0:
        steps_x2 *= -1
    if ball_y_2 > screen_y_size - ballImg.get_height() or ball_y_2 < 0:
        steps_y2 *= -1

    if ball_x > screen_x_size - ballImg.get_width() or ball_x < 0:
        steps_x *= -1
    if ball_y > screen_y_size - ballImg.get_height() or ball_y < 0:
        steps_y *= -1

    # Detectar choque entre las dos bolas
    if colision(ball_x, ball_y, ball_x_2, ball_y_2, ballImg.get_width() // 2):
        steps_x *= -1
        steps_y *= -1
        steps_x2 *= -1
        steps_y2 *= -1


    ball_x += steps_x
    ball_y += steps_y

    ball_x_2 += steps_x2
    ball_y_2 += steps_y2

    ball_pos(ball_x, ball_y)
    ball_pos(ball_x_2, ball_y_2)

    pg.display.flip()
