from New_Perlin import Perlin
import random
import pygame
import sys

pygame.init()
pygame.font.init()

WIDTH, HEIGHT = 800, 680
BLOCK_SIZE = 40
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT+20))

clock = pygame.time.Clock()
font = pygame.font.SysFont(pygame.font.get_default_font(), 27)

RED   = (255, 0, 0)
BLACK = (0, 0, 0)
BLUE  = (0, 0, 255)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)
GREY  = (127, 127, 127)




class Point(): # defines point (cells) on screen
    def __init__(self, x, y):
        self.x = x
        self.y = y




class Snake(): # defines body and head of snake on points
    def __init__(self):
        # initiating head
        self.body = [
            Point(
                x=WIDTH // BLOCK_SIZE // 2,
                y=HEIGHT // BLOCK_SIZE // 2,
            ),
        ]

    def draw(self):  # draws body and head
        head = self.body[0]
        
        # draws head
        pygame.draw.rect(
            SCREEN,
            RED,
            pygame.Rect(
                head.x * BLOCK_SIZE,
                head.y * BLOCK_SIZE,
                BLOCK_SIZE,
                BLOCK_SIZE,
            )
        )

        # draws body
        for body in self.body[1:]:
            pygame.draw.rect(
                SCREEN,
                BLUE,
                pygame.Rect(
                    body.x * BLOCK_SIZE,
                    body.y * BLOCK_SIZE,
                    BLOCK_SIZE,
                    BLOCK_SIZE,
                )
            )

    def move(self, dx, dy): # moves body after head
        for idx in range(len(self.body) - 1, 0, -1):
            self.body[idx].x = self.body[idx - 1].x
            self.body[idx].y = self.body[idx - 1].y

        self.body[0].x += dx
        self.body[0].y += dy

        # finishes the game when snake bites itself
        for idx in range(len(self.body) - 1, 0, -1):
            if self.body[idx].x == self.body[0].x and self.body[idx].y == self.body[0].y:
                game_over()

    def check_bite(self, food): # checks if food was eaten
        if food.location.x != self.body[0].x:
            return False
        if food.location.y != self.body[0].y:
            return False
        return True
    
    def check_collision(self, obstacles): # checks for collision with obstacles and borders
        # keeps snake in playing area
        if self.body[0].x >= WIDTH // BLOCK_SIZE:
            return True
        elif self.body[0].x < 0:
            return True
        elif self.body[0].y < 0:
            return True
        elif self.body[0].y >= HEIGHT // BLOCK_SIZE:
            return True
        
        # checks if snake's head collided with obstacle
        for block in obstacles.blocks:
            if block.x == self.body[0].x and block.y == self.body[0].y:
                return True
        return False




class Food(): # defines foods
    def __init__(self, x, y):
        self.location = Point(x, y)

    def draw(self): # draws food rectangles
        pygame.draw.rect(
            SCREEN,
            GREEN,
            pygame.Rect(
                self.location.x * BLOCK_SIZE,
                self.location.y * BLOCK_SIZE,
                BLOCK_SIZE,
                BLOCK_SIZE,
            )
        )
    
    def generate_new(self, snake_body, obstacles):
        self.location.x = random.randint(0, WIDTH // BLOCK_SIZE - 1)
        self.location.y = random.randint(0, HEIGHT // BLOCK_SIZE - 1)

        # checks if food fell on snake's body, if true: generates again and checks from the beginning 
        for idx in range(len(snake_body) - 1, 0, -1):
            if self.location.x == snake_body[idx].x and self.location.y == snake_body[idx].y:
                self.location.x = random.randint(0, WIDTH // BLOCK_SIZE - 1)
                self.location.y = random.randint(0, HEIGHT // BLOCK_SIZE - 1)
                idx = len(snake_body) - 1

        for i in range(len(obstacles)):
            if self.location.x == obstacles[i].x and self.location.y == obstacles[i].y:
                self.location.x = random.randint(0, WIDTH // BLOCK_SIZE - 1)
                self.location.y = random.randint(0, HEIGHT // BLOCK_SIZE - 1)
                i = 0




class Obstacle(Perlin): # defines obstacles
    def __init__(self):
        super().__init__()
        self.blocks = self._generate(filter=0.32)        


    def _generate(self, filter=0.32): # generating noise
        xpix, ypix = WIDTH // BLOCK_SIZE, HEIGHT // BLOCK_SIZE
        parameters = [
            {"octaves" : 24, "persistence" : 0.9, "amplitude" : 1,},
            {"octaves" : 18, "persistence" : 0.7, "amplitude" : 1,},
            {"octaves" : 12, "persistence" : 0.5, "amplitude" : 1,},
            {"octaves" : 10, "persistence" : 0.4, "amplitude" : 3,},
            {"octaves" :  6, "persistence" : 0.3, "amplitude" : 4,},
        ]

        noise_values = self.multiParameterNoise(ypix, xpix, parameters) # it is a method in Perlin class
        # filtering results
        for i in range(xpix):
            for j in range(ypix):
                if noise_values[i][j] < filter: 
                    noise_values[i][j] = 0

        return  self._project_to_points(noise_values)


    def _project_to_points(self, list): # projecting noise into "Points" on screen
        xpix, ypix = WIDTH//BLOCK_SIZE, HEIGHT//BLOCK_SIZE
        
        list[5][5] = 0 # it's a initial position of food
        list[ypix//2][xpix//2] = 0

        projected_list = []
        for i in range(xpix):
            for j in range(ypix):
                if list[i][j] != 0: projected_list.append(Point(i, j))
        
        return projected_list


    def draw(self):
        for block in self.blocks:
            pygame.draw.rect(
                SCREEN,
                GREY,
                pygame.Rect(
                    block.x * BLOCK_SIZE,
                    block.y * BLOCK_SIZE,
                    BLOCK_SIZE,
                    BLOCK_SIZE,
                )
            )




def draw_grid():
    # draw cells
    for x in range(0, WIDTH, BLOCK_SIZE):
        pygame.draw.line(SCREEN, WHITE, start_pos=(x, 0), end_pos=(x, HEIGHT), width=1)
    for y in range(0, HEIGHT, BLOCK_SIZE):
        pygame.draw.line(SCREEN, WHITE, start_pos=(0, y), end_pos=(WIDTH, y), width=1)

    # draw borders
    pygame.draw.line(SCREEN, RED, start_pos=(0, HEIGHT-1), end_pos=(WIDTH-1, HEIGHT-1), width=1)  #bottom border
    pygame.draw.line(SCREEN, RED, start_pos=(0, 0), end_pos=(0, HEIGHT), width=1)   #left border
    pygame.draw.line(SCREEN, RED, start_pos=(WIDTH-1, 0), end_pos=(WIDTH-1, HEIGHT-1), width=1)   #right border
    pygame.draw.line(SCREEN, RED, start_pos=(0, 0), end_pos=(WIDTH, 0), width=1)    #top border




def game_over():
    print("game over")
    sys.exit()




def main():

    running = True
    snake = Snake()
    food = Food(5, 5)
    obstacles = Obstacle()
    dx, dy = 0, 0
    score = 0
    level = 0

    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # иногда бывает что змейка сама себе шею ломает
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and dy != 1:
                    dx, dy = 0, -1
                elif event.key == pygame.K_DOWN and dy != -1:
                    dx, dy = 0, 1
                elif event.key == pygame.K_RIGHT and dx != -1:
                    dx, dy = 1, 0
                elif event.key == pygame.K_LEFT and dx != 1:
                    dx, dy = -1, 0
                elif event.key == pygame.K_q:
                    running = False

        snake.move(dx, dy)

        # appending snake's body
        if snake.check_bite(food):
            score += 1
            level = score // 3
            food.generate_new(snake.body, obstacles.blocks)
            snake.body.append(Point(snake.body[-1].x, snake.body[-1].y))

        if snake.check_collision(obstacles):
            game_over()

        score_font = font.render('Score: ' + str(score), True, (255, 255, 255))
        level_font = font.render('Level: ' + str(level), True, (255, 255, 255))

        SCREEN.fill(BLACK)
        SCREEN.blit(score_font, (0, HEIGHT))
        SCREEN.blit(level_font, (WIDTH // 2, HEIGHT))

        snake.draw()
        food.draw()
        obstacles.draw()
        draw_grid()

        pygame.display.flip()
        clock.tick(2 * level + 5)


if __name__ == '__main__':
    main()