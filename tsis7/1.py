import pygame
import math 
import datetime

pygame.init()

width,height = 800, 800
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("Mickey Clock")
mickey = pygame.image.load('/Users/symbat/Documents/pp2-22B030325/tsis7/main-clock.png')
left_hand = pygame.image.load('/Users/symbat/Documents/pp2-22B030325/tsis7/left-hand.png')
right_hand = pygame.image.load('/Users/symbat/Documents/pp2-22B030325/tsis7/right-hand.png')

clock = pygame.transform.scale(mickey,(width,height))

x, y = width // 2, height // 2

status = True
while status:
    screen.blit(mickey,(0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            status = False
    
    time = datetime.datetime.now()
    min = time.minute - 13
    sec = time.second

    minute_angle = -math.radians((min / 60) * 360)
    minute_hand_rotated = pygame.transform.rotate(right_hand, math.degrees(minute_angle))
    minute_hand_rect = minute_hand_rotated.get_rect(center=(x, y))
    screen.blit(minute_hand_rotated, minute_hand_rect)

    second_angle = -math.radians((sec / 60) * 360)
    second_hand_rotated = pygame.transform.rotate(left_hand, math.degrees(second_angle))
    second_hand_rect = second_hand_rotated.get_rect(center=(x, y))
    screen.blit(second_hand_rotated, second_hand_rect)

    pygame.display.flip()

  