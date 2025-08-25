import pygame as pg
import random as r
import math

pg.init()
screen = pg.display.set_mode((800, 600))

pg.display.set_caption("Space Shooter Game")

# === Upload images ===
icon_img = pg.image.load('Spaceship/img_downsized/icon.png')
ball_img = pg.image.load('Spaceship/img_downsized/ball.png')
bullet_img = pg.image.load('Spaceship/img_downsized/bullet_d.png')
enemy1_img = pg.image.load('Spaceship/img_downsized/enemy1_d.png')
enemy2_img = pg.image.load('Spaceship/img_downsized/enemy2_d.png')
player_img = pg.image.load('Spaceship/img_downsized/player_d.png')
space_bg_img = pg.image.load('Spaceship/img_downsized/space_d.png')
alien_blaster_img = pg.image.load('Spaceship/img_downsized/alienblaster_d.png')
explosion_img = pg.image.load('Spaceship/img_downsized/explosion.png')

pg.display.set_icon(icon_img)

# == Misil ==
bulletX = 370
bulletY = 480
bullet_changeY = 1
bullet_ratio = 0.1
check = False

# == Enemigos ==
enemy1X = r.randint(0, 736)
enemy1Y = 50
enemy1_changeX = 1
enemy1_changeY = 0
enemy1_ratio = 0.1

# == Nave Espacial ==
spaceShipX = 370
spaceShipY = 480
changeX = 0
changeY = 0
ratio = 0.1

def player():
    screen.blit(player_img, (spaceShipX, spaceShipY))

def enemy():
    screen.blit(enemy1_img, (enemy1X, enemy1Y))

def bullet():
    screen.blit(bullet_img, (bulletX, bulletY))

def explosion():
    screen.blit(explosion_img, (enemy1X + 10, enemy1Y))


def collision():
    distance = math.sqrt(math.pow(bulletX - enemy1X + 10, 2) + math.pow(bulletY - enemy1Y, 2))
    if distance < 55:
        return True


running = True
while running:
    screen.blit(space_bg_img, (0, 0))  # top corner

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

        if event.type == pg.KEYDOWN:
            if event.key == pg.K_LEFT:
                changeX = -1 * ratio
            if event.key == pg.K_RIGHT:
                changeX = +1 * ratio
            if event.key == pg.K_UP:
                changeY = -1 * ratio
            if event.key == pg.K_DOWN:
                changeY = +1 * ratio
            if event.key == pg.K_SPACE:
                if not check:
                    check = True
                    bulletX = spaceShipX + 22
                    bulletY = spaceShipY 

        if event.type == pg.KEYUP:
            changeX = 0
            changeY = 0

    spaceShipX += changeX
    spaceShipY += changeY

    if spaceShipX < 0:
        spaceShipX = 0
    if spaceShipX > 736:
        spaceShipX = 736
    if spaceShipY > 480:
        spaceShipY = 480
    if spaceShipY < 30:
        spaceShipY = 30

    if bulletY < 0:
        check = False
        

    # Enemigo
    enemy1X += enemy1_changeX * enemy1_ratio
    enemy1Y += enemy1_changeY

    if enemy1X < 0 or enemy1X > 726:
        enemy1_ratio *= -1
        enemy1Y += 20

    if enemy1Y > 480:
        enemy1Y = 480
    elif enemy1Y < 30:
        enemy1Y = 30

    collided = collision()  

    if check:
        bulletY -= bullet_changeY * bullet_ratio
        bullet()

    enemy()
    if collided:
        explosion()
        check = False
        enemy1X = r.randint(0, 736)
        enemy1Y = 50
        enemy()

    player()
    

    pg.display.update()
