import pygame
import random

pygame.init()
pygame.font.init()

WHITE = (255, 255, 255)
BG_COLOR = (32, 24, 41)
ROCKET_X, ROCKET_Y = 10, 60

width, height = 900, 600
screen = pygame.display.set_mode((width, height+20))
clock = pygame.time.Clock()
font = pygame.font.SysFont(pygame.font.get_default_font(), 27)

# path = r"/Users/symbat/Documents/pp2-22B030325/l8"  
# случайный выбор направления движения манипулятора, управляемого процессором, вверх или вниз
selected_cpu_dy = -1 * random.randint(0, 1)


ROCKET_IMAGE = pygame.image.load(r"/Users/symbat/Documents/pp2-22B030325/l8/Player.jpg")
BALL_IMAGE = pygame.image.load(r"/Users/symbat/Documents/pp2-22B030325/l8/Ball.jpg")
BALL_IMAGE = pygame.transform.scale(BALL_IMAGE, (30, 30))



class Ball(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.x = width // 2
        self.y = height // 2
        self.image = BALL_IMAGE
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)
        self.speed = 5
   

    def move(self, dx, dy):
        screen.blit(self.image, self.rect)
        self.rect.y += dy*self.speed
        self.rect.x += dx*self.speed  


    def set_default(self):  
        self.rect.center = (self.x, self.y)



class Rocket(pygame.sprite.Sprite):
    score = 0

    def __init__(self, x):
        super().__init__()
        self.x = x
        self.speed = 5
        self.image = ROCKET_IMAGE
        self.rect = self.image.get_rect()
        self.rect.center = (x, height // 2 - self.rect.height // 2)


    def move(self, dy):
        screen.blit(self.image, self.rect)
        if self.rect.y <= self.speed:
            dy = 1
        if self.rect.y + self.rect.height + self.speed >= height:
            dy = -1
        self.rect.y += dy*self.speed




def draw_interface(cpu_score, player_score):
        cpu_font = font.render('Cpu: ' + str(cpu_score), True, (255, 255, 255))
        player_font = font.render('Player: ' + str(player_score), True, (255, 255, 255))

        screen.blit(cpu_font, (0, height+1))
        screen.blit(player_font, (width // 2, height+1))

        pygame.draw.line(screen, WHITE, (0, height), (width, height))




def gpt_9(ball_x, ball_y, ball_dx, own_y, selected_random):
    if ball_dx == 1:
        return 1
    
    if width / 3 < ball_x <= width / 2.4:
        if selected_random == 0: 
            return -1
        return selected_random

    if ball_x >= width // 3:
        return -1
    elif ball_y < own_y:
        return -1
    elif ball_y > own_y:
        return 1
    
    return 1




def reselect():
    global selected_cpu_dy
    selected_cpu_dy = -1 * random.randint(0, 1)




def main():
    paused_state = False
    running = True

    ball_dx = ball_dy = 1
    dy = 0

    player = Rocket(width - ROCKET_X)
    cpu = Rocket(ROCKET_X)
    ball = Ball()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    paused_state = not paused_state
                elif event.key == pygame.K_DOWN:
                    dy = 1
                elif event.key == pygame.K_UP:
                    dy = -1


        if paused_state == True:
            continue
        
        if ball.rect.y <= ball.speed:
            ball_dy = 1
        if ball.rect.y + ball.rect.height + ball.speed >= height:
            ball_dy = -1

        if ball.rect.x <= ball.speed:
            ball.set_default()
            player.score += 1
            ball_dx = 1
        if ball.rect.x + ball.rect.width + ball.speed > width:
            ball.set_default()
            cpu.score += 1
            ball_dx = -1

        if ball.rect.colliderect(player.rect) or ball.rect.colliderect(cpu.rect):
            reselect()
            ball_dx *= -1
        
        cpu_dy = gpt_9(ball.rect.x, ball.rect.y, ball_dx, cpu.rect.y, selected_cpu_dy)

        screen.fill(BG_COLOR)
        draw_interface(cpu.score, player.score)

        player.move(dy)
        cpu.move(cpu_dy)
        ball.move(ball_dx, ball_dy)
        
        pygame.display.flip()
        clock.tick(60)






if __name__ == '__main__':
    main()