import pygame

pygame.init()

WIDTH, HEIGTH = 500, 500
pygame.display.set_caption("RED BALL")
screen = pygame.display.set_mode((WIDTH, HEIGTH))

ball_radius = 25
ball_color = (255, 0, 0)  #red
x = WIDTH // 2
y = HEIGTH // 2

def draw_ball(x, y):
    pygame.draw.circle(screen, color=ball_color, center=(x, y), radius=ball_radius)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
            
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                y -= 20
            elif event.key == pygame.K_DOWN:
                y += 20
            elif event.key == pygame.K_LEFT:
                x -= 20
            elif event.key == pygame.K_RIGHT:
                x += 20
    
    if x < ball_radius:
        x = ball_radius
    elif x > WIDTH - ball_radius:
        x = WIDTH - ball_radius
    if y < ball_radius:
        y = ball_radius
    elif y > HEIGTH - ball_radius:
        y = HEIGTH - ball_radius
    
    screen.fill((255, 255, 255))
    draw_ball(x, y)
    pygame.display.update()