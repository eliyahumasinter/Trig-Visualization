import math
import pygame

WIDTH = 600
HEIGHT = 600
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
RADIUS = 250
running = True
centerx = WIDTH / 2
centery = HEIGHT / 2
angle = 0
x = 0
y = 0
FPS = 30
clock = pygame.time.Clock()
pi = math.pi
value1 = (math.sqrt(2) / 2) * RADIUS
while running:
  clock.tick(FPS)
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    else:
      pass
  screen.fill((120, 120, 120))

  x = int(math.cos(angle) * RADIUS) + centerx
  y = int(math.sin(angle) * RADIUS) + centery

  angle += 0.05
  pygame.draw.line(screen, BLACK, (centerx, y), (x, centery), 3)  # Hypotenus
  pygame.draw.circle(screen, BLACK, (centerx, centery),
                     RADIUS, width=3)  # Outline circle
  pygame.draw.circle(screen, RED, (x, y), 10)  # Moving circle
  pygame.draw.line(screen, BLACK, (centerx, centery - RADIUS),
                   (centerx, centery + RADIUS), 3)  # line 1
  pygame.draw.line(screen, BLACK, (centerx - RADIUS, centery),
                   (centerx + RADIUS, centery), 3)  # line 2
  pygame.draw.circle(screen, YELLOW, (centerx, y),
                     10)  # Yellow moving circle 1
  pygame.draw.circle(screen, YELLOW, (x, centery),
                     10)  # Yellow moving circle 2

  pygame.display.flip()

pygame.quit()

#(50+(RADIUS-value1))+((x/RADIUS)*value1)-(50)
