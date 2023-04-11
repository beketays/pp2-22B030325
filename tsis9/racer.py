import random
import pygame
import time

pygame.init()

SCORE = 0
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

WIDTH, HEIGHT = 400, 700
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))

#choosing path and setting up images
path = r"/Users/symbat/Documents/pp2-22B030325/tsis9/racer//"   #'C:\Users\Сырым\Documents\pp2-22B030546\tsis9\racer2.0\\'
background_image = pygame.image.load(path + 'AnimatedStreet.png')
enemy_image = pygame.image.load(path + 'Enemy.png')
player_image = pygame.image.load(path + 'Player.png')
coin_image_L1 = pygame.image.load(path + 'CoinL1.png')
coin_image_L2 = pygame.image.load(path + 'CoinL2.png')
coin_image_L3 = pygame.image.load(path + 'CoinL3.png')

background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))

#setting up fonts
font = pygame.font.SysFont("times new roman", 30)
font_small = pygame.font.SysFont("times new roman", 20)
game_over = font.render("Game Over", True, BLACK)

clock = pygame.time.Clock()


#defining enemy
class Enemy():
    def __init__(self):
        self.speed = 10
        self.image = enemy_image
        self.rect = self.image.get_rect()

        #choosing random point in x-axis to spawn enemy
        random_width = random.randint(self.rect.width, WIDTH - self.rect.width)
        self.rect.center = (random_width, 0)


    def update(self):
        global SCORE
        self.rect.y += self.speed // 1

        #cheking if enemy is outside of screen
        if self.rect.y > HEIGHT:
            SCORE += 1
            #choosing random point in x-axis to re-spawn enemy
            random_width = random.randint(self.rect.width, WIDTH - self.rect.width)
            self.rect.center = (random_width, 0)


    def draw(self):
        SCREEN.blit(self.image, self.rect)


#defining Player
class Player():
    def __init__(self):
        self.speed = 5
        self.image = player_image
        self.rect = self.image.get_rect()
        #creating player in the middle
        self.rect.center = (WIDTH // 2, HEIGHT - self.rect.height // 2 - 20)

    def update(self):
        pressed = pygame.key.get_pressed()
        #checking if player is still on screen before moving
        if pressed[pygame.K_LEFT] and self.rect.x - self.speed >= 0:
            self.rect.x -= self.speed
        elif pressed[pygame.K_RIGHT] and self.rect.x + self.speed + self.rect.width <= WIDTH:
            self.rect.x += self.speed
    
    def draw(self):
        SCREEN.blit(self.image, self.rect)



class Background():    #adding sliding background
    def __init__(self, start_y):
        self.image = background_image
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 2, HEIGHT - self.rect.height // 2 + start_y)

    def draw(self):
        SCREEN.blit(self.image, self.rect)

    def update(self, speed):
        #if image is outside of screen moving to -HEIGHT by y-axis
        if self.rect.y >= HEIGHT + 10:
            self.rect.y = -HEIGHT - 10
        self.rect.y += speed

class Coin():  #defining coins
    def __init__(self, x, y, num):   #getting initial coordinates
        self.x = x
        self.y = y
        image_dict = {
            1 : coin_image_L1,
            2 : coin_image_L2,
            3 : coin_image_L3,
        }

        
        self.image = image_dict[num]
        self.weight = num
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)


    def update(self, speed):
        self.rect.y += speed

    
    def draw(self):
        SCREEN.blit(self.image, self.rect)


def add_coins(coins):
    for i in range(4):   #choosing random point in x-axis
        random_width = random.randint(40, WIDTH - 40)
        num = random.randint(1, 3)
        coins.append(Coin(random_width, - (i) * HEIGHT * 0.15, num))
    return coins


def main():
    COLLECTED = 0
    CoeficientN = 10
    enemy = Enemy()
    player = Player()
    background_1 = Background(0)
    background_2 = Background(-HEIGHT)  #background_2 will follow background_1, that's why -HEIGHT 
    coins = []
    running = True

    while running:
        SCREEN.fill(WHITE)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        if len(coins) <= 1:    #checking if there is enough coins and adding if it's not
            add_coins(coins)

        #updating states of all entities exept coins
        background_1.update(enemy.speed // 3)
        background_2.update(enemy.speed // 3)
        player.update()
        enemy.update()
        #coins are drawn and updated below
        #drawing all entities exept coins
        background_1.draw()
        background_2.draw()
        player.draw()
        enemy.draw()

        score = font_small.render("Your score: " + str(SCORE), True, BLACK)   #showing score and number of coins
        coins_text = font_small.render("Coins collected: " + str(COLLECTED), True, BLACK)
        SCREEN.blit(score, (0, 0))
        SCREEN.blit(coins_text, (WIDTH // 2, 0))

        if player.rect.colliderect(enemy):  #checking for collision between player and enemy
            SCREEN.blit(game_over, (30, 250))
            pygame.display.flip() #without this display won't update and won't show game_over
            time.sleep(2)
            running = False 

        i = 0
        while i < len(coins):
            #checking for collision between player and coin
            if player.rect.colliderect(coins[i]):
                COLLECTED += coins[i].weight
                enemy.speed += COLLECTED // CoeficientN * 0.25 # Coeficient that used to increase speed (default = 5)
                coins.pop(i)
                i -= 1
            #returning coin to its start position if it is outside of screen
            if coins[i].rect.y >= HEIGHT + 20:
                coins[i].rect.y = -20
            i += 1

        #updating states of coins in list "coins", and drawing them
        for coin in coins:
            coin.update(enemy.speed // 3)
            coin.draw()

        pygame.display.flip()
        clock.tick(60)


if __name__ == '__main__':
    main()