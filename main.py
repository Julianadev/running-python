import pygame
from random import randint

pygame.init()

# speed cars / bg
x = 600
y = 600
y1 = -50
y2 = -20
y3 = -30
y4 = -40
y5 = -220
v = 10
v1 = -30
v2 = -15
v3 = -20
v4 = -20
v5 = -20

# background
background = pygame.image.load("estrada-bg.jpg")
background2 = pygame.image.load("estrada-bg-2.jpg")
background3 = pygame.image.load("estrada-bg-2.jpg")

# bg-cars
cars = pygame.image.load("carro-1.png")
cars2 = pygame.image.load("carro-2.png")
cars3 = pygame.image.load("carro-3.png")
cars4 = pygame.image.load("police.png")
cars5 = pygame.image.load("carro-5.png")

# display
window = pygame.display.set_mode((800, 680))
pygame.display.set_caption("racer")

# close/open display
open_window = True
while open_window:
    pygame.time.delay(50)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            open_window = False

    # commands
    commands = pygame.key.get_pressed()
    if commands[pygame.K_UP]:
        y -= v
    if commands[pygame.K_DOWN]:
        y += v
    if commands[pygame.K_RIGHT] and x <= 690:
        x += v
    if commands[pygame.K_LEFT] and x >= 0:
        x -= v
    y1 -= v1
    y2 -= v2
    y3 -= v3
    y4 -= v4
    y5 -= v5
    if y1 >= 700:
        y1 = -50
    if y2 >= 750:
        y2 = randint(-150, -20)
    if y3 >= 760:
        y3 = randint(-200, -30)
    if y4 >= 770:
        y4 = randint(-250, -30)
    if y5 >= 780:
        y5 = randint(-300, -200)

    # background position
    window.blit(background, (0, 0))
    window.blit(background2, (306, y1))
    window.blit(background3, (403, y1))
    window.blit(cars5, (450, y5))
    window.blit(cars4, (100, y4))
    window.blit(cars3, (630, y3))
    window.blit(cars2, (230, y2))
    window.blit(cars, (x, y))
    pygame.display.update()


pygame.quit()
