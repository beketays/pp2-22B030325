import pygame 
import math 

pygame.init()

monitor = pygame.display.set_mode((1000,800))
check = True
is_blue = True 
x = 50
y = 50

while check:

    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            check = False
        if i.type == pygame.KEYDOWN and i.key == pygame.K_SPACE:
            is_blue = not is_blue 
        elif i.type == pygame.KEYDOWN and i.key == pygame.K_q:
            monitor = pygame.display.set_mode((1000,800))
        elif i.type == pygame.KEYDOWN and i.key == pygame.K_w:
            monitor = pygame.display.set_mode((400,300))
    button = pygame.key.get_pressed()
    if 1000 >= x >= 0 and 800 >= y >= 0:   
        if button [pygame.K_UP]: y -= 20
        if button [pygame.K_DOWN]: y += 20
        if button [pygame.K_LEFT]: x -= 20
        if button [pygame.K_RIGHT]: x += 20

    if x > 1000 or  x < 0:
        if x > 0:
            x = abs(x - 1000)
        if x < 0:
            x = abs(x + 1000)
    if y > 800 or y < 0:
        if y > 0:
            y = abs(y - 800)
        if y < 0:
            y = abs(y + 800)

    if is_blue: color = (255, 255, 255)
    else: color = (255, 100, 0)
    monitor.fill(color)
    pygame.draw.circle(monitor,(255, 0 , 0),(x,y),25 )
    pygame.display.update()