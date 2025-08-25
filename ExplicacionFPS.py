import pygame as pg

pg.init()

# Pantalla
screen = pg.display.set_mode((500, 300))
pg.display.set_caption("Ejemplo FPS")

# Colores
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Bola
x = 0
y = 150
speed = 5   # velocidad en píxeles por frame

# Reloj de pygame
clock = pg.time.Clock()

# FPS (prueba cambiando este valor: 30, 60, 120...)
FPS = 120

running = True
while running:
    # Eventos (cerrar ventana)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    # Lógica: mover la bola
    x += speed
    if x > 500:   # si se sale de pantalla, vuelve
        x = 0

    # Dibujar
    screen.fill(WHITE)
    pg.draw.circle(screen, RED, (x, y), 20)

    # Actualizar pantalla
    pg.display.flip()

    # Controlar FPS
    clock.tick(FPS)

pg.quit()
