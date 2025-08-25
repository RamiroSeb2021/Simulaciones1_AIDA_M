import pygame as pg
import random as r
import math 

# ===================== Configuración básica =====================
pg.init()

W, H = 800, 600
screen = pg.display.set_mode((W, H))
pg.display.set_caption("Bouncing Balls - AutoSpawn")

# Cargar imagen 

BALL_IMG = None
BALL_PATH = "Spaceship/img_downsized/ball.png"

try:
    BALL_IMG = pg.image.load(BALL_PATH).convert_alpha()
except Exception as e:
    print(f"Ocurrió un error: {e}")
    BALL_IMG = None

BACKGROUND = (255, 255, 255)
FPS = 120

# Cada cuanto aparece una bola 
SPAWN_MS = 125 # 1000MS = 1 segundo
SPAWN_EVENT = pg.USEREVENT + 1 # Agregar un nuevo evento
pg.time.set_timer(SPAWN_EVENT, SPAWN_MS)


class Bola:
    def __init__(self, x = None, y = None):
        # Posición inicial aleatoria 
        if BALL_IMG:
            self.w = BALL_IMG.get_width()
            self.h = BALL_IMG.get_height()
            self.r = self.w // 2
        else:
            self.r = r.randint(12, 14)
            self.w = self.r * 2

        self.x = x if x is not None else r.uniform(self.r, W - self.r)
        self.y = y if y is not None else r.uniform(self.r, H - self.r)

        # Velocidad inicial aleatoria 
        speed = r.uniform(0.9, 1.9)
        angle = r.uniform(0, 2 * math.pi)
        self.vx = speed * math.cos(angle)
        self.vy = speed * math.sin(angle)

        self.color = (r.randint(50, 200), r.randint(50, 200), r.randint(50, 200))

    def updatePos(self, dt = 1.0):
         self.x += self.vx * dt
         self.y += self.vy * dt

         # Rebote con paredes
         if self.x > W - self.r:
             self.x = W - self.r
             self.vx *= -1
         elif self.x < self.r:
             self.x = self.r
             self.vx *= -1
        
         if self.y > H - self.r:
             self.y =  H - self.r
             self.vy *= -1
         elif self.y < self.r:
             self.y = self.r
             self.vy *= -1

    def draw(self, surface):
        if BALL_IMG:
            # Centrar la imagen en (x, y)
            surface.blit(BALL_IMG, (self.x - self.w//2, self.y - self.h//2))
        else:
            pg.draw.circle(surface, self.color, (int(self.x), int(self.y), int(self.r)))

# ========== Choque simple entre bolas ==========
def collide_and_bounce(b1:Bola, b2:Bola):
    """
    Resuelve choque simple: si se superponen, separa y refleja velocidades
    sobre la normal (aprox. choque elástico igual-masa).
    """
    dx = b2.x - b1.x 
    dy = b2.y - b1.y
    dist = math.hypot(dx, dy)
    min_dist = b1.r + b2.r

    if dist == 0:
         # Evitar dividir entre cero
         dx, dy = r.uniform(-1, 1), r.uniform(-1, 1)
         dist = math.hypot(dx, dy)
     
    if dist < min_dist:
        # Normal y tangente 
        nx, ny = dx/dist, dy/dist

        # Separación mínima para que no queden pegados
        overlap = (min_dist - dist) / 2
        b1.x -= nx * overlap
        b1.y -= ny * overlap
        b2.x += nx * overlap
        b2.y += ny * overlap

        # Proyección de velocidades en la normal (choque elástico con masas iguales)
        v1n = b1.vx * nx + b1.vy * ny
        v2n = b2.vx * nx + b2.vy * ny

        # Intercambio de componentes normales
        b1.vx += (v2n - v1n) * nx
        b1.vy += (v2n - v1n) * ny
        b2.vx += (v1n - v2n) * nx
        b2.vy += (v1n - v2n) * ny


# ===================== Bucle principal =====================
clock = pg.time.Clock()
balls = []

# Creación de una primera bola para iniciar
balls.append(Bola())

running = True

while running:
    dt_ms = clock.tick(FPS)  # limita FPS y devuelve ms transcurridos
    # Escala temporal opcional (1.0 está bien; si quieres variación, usa dt_ms)
    dt = 1.0

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        elif event.type == SPAWN_EVENT:
            # Generar una nueva bola automaticamente
            balls.append(Bola())
    
    # Movimiento
    for b in balls:
        b.updatePos()

    # Choques par-a-par (O(N**2) - bien para decenas de bolas)
    for i in range(len(balls)):
        for j in range(i + 1, len(balls)):
            collide_and_bounce(balls[i], balls[j])

    # Render 
    screen.fill(BACKGROUND)
    for b in balls:
        b.draw(screen)
    
    # 🔹 Actualizar título con el número de bolas
    pg.display.set_caption(f"Bouncing balls - Total: {len(balls)}")

    pg.display.flip()

pg.quit()