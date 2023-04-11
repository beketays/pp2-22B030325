
import pygame
import math

pygame.init()
clock = pygame.time.Clock()
WIDTH, HEIGHT = 800, 700
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
BLACK = pygame.Color(0, 0, 0)
WHITE = pygame.Color(255, 255, 255)
GREEN = pygame.Color(0, 255, 0)
RED = pygame.Color(255, 0, 0)
BLUE = pygame.Color(0, 0, 255)
buttons_bar = pygame.Surface((200, 700))
font = pygame.font.SysFont("Times New Roman", 15)
button_position = {
    'line': [4, 4, 44, 44],
    'rect': [52, 4, 44, 44],
    'triangle_R': [4, 50, 44, 44],
    'triagle_E': [52, 50, 44, 44],
    'rhombus': [4, 96, 44, 44]
}

def submaterials():

    pygame.draw.rect(buttons_bar, BLACK, (2, 2, 96, 206), 1) 
    pygame.draw.aaline(buttons_bar, BLACK, (8, 8), (40, 40), 1)
    pygame.draw.rect(buttons_bar, BLACK, (58, 10, 32, 32), 1)
    pygame.draw.polygon(buttons_bar, BLACK, (27, 70), 15, 1)
    pygame.draw.polygon(buttons_bar, BLACK, (56, 58, 36, 28))
    pygame.draw.polygon(buttons_bar, BLACK, (4, 96, 44, 44))
    c = font.render('Press:', True, 'black')
    buttons_bar.blit(c, (5, 100))
    r = font.render('1 - Red', True, 'black')
    buttons_bar.blit(r, (5, 120))
    g = font.render('2 - Green', True, 'black')
    buttons_bar.blit(g, (5, 140))
    b = font.render('3 - Blue', True, 'black')
    buttons_bar.blit(b, (5, 160))
    y = font.render('4 - White', True, 'black')
    buttons_bar.blit(y, (5, 180))
    SCREEN.blit(buttons_bar, (700, 0))



class GameObject:
    def draw(self):
        return

    def update(self, current_pos):
        return
    
    
class Button(pygame.sprite.Sprite):
    def __init__(self, points, width=1, color='gray'):
        super().__init__()
        
        self.points = points
        self.width = width
        self.color = color
        self.rect = pygame.draw.polygon(SCREEN, self.color, self.ponts, self.width)
        
    def draw(self):
        pygame.draw.polygon(SCREEN, self.color, self.points, self.width)
    

class Pen(GameObject):
    def __init__(self, start_pos, thickness=5, color=WHITE):  # Pen(1, 2, 3, a=4) =>
        self.thickness = thickness
        self.color = color
        self.points = []

    def draw(self):
        for idx, point in enumerate(self.points[:-1]):  # range(len(self.points))
            pygame.draw.line(
                SCREEN,
                self.color,
                start_pos=(point.x, point.y),  # self.points[idx]
                end_pos=self.points[idx + 1],
                width=5
            )

    def update(self, current_pos):
        self.points.append(current_pos)  # (x, y) Point((x, y)) => Point(x, y)
    
    
class Rectangle(GameObject):
    def __init__(self, start_pos, thickness=5, color=WHITE): # Rectangle(start_pos=1); Pen(start_pos=1)
        self.thickness = thickness
        self.color = color
        self.start_pos = start_pos
        self.end_pos = start_pos
        
    def draw(self):
        start_pos_x = min(self.start_pos[0], self.end_pos[0])  # min(self.start_pos[0], self.end_pos[0])
        start_pos_y = min(self.start_pos[1], self.end_pos[1])


        end_pos_x = max(self.start_pos[0], self.end_pos[0])
        end_pos_y = max(self.start_pos[1], self.end_pos[1])

        pygame.draw.rect(
            SCREEN,
            self.color,
            (
                start_pos_x, start_pos_y,
                end_pos_x - start_pos_x,
                end_pos_y - start_pos_y,
            ),
            width=self.thickness,
        )

    def update(self, current_pos):
        self.end_pos.x, self.end_pos.y = current_pos  
        
        
class RightTriangle(GameObject):
    def __init__(self, start_pos, thickness=5, color=WHITE):
        self.thickness = thickness
        self.color = color
        self.start_pos = start_pos
        self.end_pos = start_pos

    def draw(self):
        start_pos_x, start_pos_y = self.start_pos
        end_pos_x, end_pos_y = self.end_pos

        side_len = end_pos_x - start_pos_x                     # calculating length of side
        h = math.pow(side_len**2 * 0.75, 0.5) # calculating height

        if side_len < 0: h *= -1              # to draw inverted triangle
        
        # calculating vertices
        vertex_1 = (start_pos_x, start_pos_y)
        vertex_2 = (end_pos_x, start_pos_y)
        vertex_3 = (start_pos_x + side_len/2, start_pos_y - h)
        vertices = [vertex_1, vertex_2, vertex_3]

        # Drawing right triangle
        pygame.draw.polygon(SCREEN, self.color, vertices, width=self.thickness)

    def handle(self, current_pos):
        self.end_pos = current_pos


class EquilateralTriangle(GameObject):
    def __init__(self, start_pos, thickness=5, color=WHITE):
        self.thickness = thickness
        self.color = color
        self.start_pos = start_pos
        self.end_pos = start_pos

    def draw(self):
        start_pos_x, start_pos_y = self.start_pos
        end_pos_x, end_pos_y = self.end_pos
        # calculating width(bottom side) of triangle
        w = (end_pos_x - start_pos_x) *2

        # calculating vertices
        vertex_1 = (start_pos_x, start_pos_y)
        vertex_2 = (end_pos_x, end_pos_y)
        vertex_3 = (end_pos_x-w, end_pos_y)
        vertices = [vertex_1, vertex_2, vertex_3]

        # Drawing equilateral triangle
        pygame.draw.polygon(SCREEN, self.color, vertices, width=self.thickness)

    def handle(self, current_pos):
        self.end_pos = current_pos

        
        
        
class Rhombus(GameObject):
    def __init__(self, start_pos, thickness=5, color=WHITE):
        self.thickness = thickness
        self.color = color
        self.start_pos = start_pos
        self.end_pos = start_pos
        
    def draw(self):
        start_pos_x, start_pos_y = self.start_pos
        end_pos_x, end_pos_y = self.end_pos
        
        # calculating length of side
        side_len = math.pow((start_pos_x - start_pos_x)**2 + (end_pos_y - start_pos_y)**2, 0.5)
        
        # calculating vertices
        vertex_1 = (start_pos_x, start_pos_y)
        vertex_2 = (end_pos_x, end_pos_y)
        vertex_3 = (end_pos_x + side_len, end_pos_y)
        vertex_4 = (start_pos_x + side_len, start_pos_y)
        vertices = [vertex_1, vertex_2, vertex_3, vertex_4]
        
        pygame.draw.polygon(SCREEN, self.color, vertices, width=self.thickness)
          
    def update(self, current_pos):
        self.end_pos = current_pos      
        



def main():
    running = True
    game_object = GameObject()
    active_obj = game_object
    current_shape = Pen  # current_shape()
    current_color = WHITE
    line_button = Button(4, 4, 44, 44, True)
    rec_button =  Button(52, 4, 44, 44, False)
    tri_r = Button(4, 50, 44, 44, False)
    tri_e = Button(52, 50, 44, 44, False)
    rhomb = Button(4, 96, 44, 44, False)
    buttons = [
        line_button, rec_button, tri_r, tri_e, rhomb
    ]
    objects = []

    while running:
        SCREEN.fill(BLACK)
        buttons_bar.fill('white')
        for obj in buttons:
            obj.draw()
        for obj in objects:
            obj.draw()
        submaterials()


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1 or event.key == pygame.K_KP_1:
                    current_color = RED
                elif event.key == pygame.K_2 or event.key == pygame.K_KP_2:
                    current_color = GREEN
                elif event.key == pygame.K_3 or event.key == pygame.K_KP_3:
                    current_color = BLUE
                elif event.key == pygame.K_4 or event.key == pygame.K_KP_4:
                    current_color = WHITE
                    
            if event.type == pygame.MOUSEBUTTONDOWN:
                if rec_button.rect.collidepoint((event.pos[0] - 700, event.pos[1])):
                    current_shape = Rectangle
                    for obj in buttons:
                        obj.button_pressed = False
                    rec_button.button_pressed = True

                    # current_shape = button.connected_shape
                elif line_button.rect.collidepoint((event.pos[0] - 700, event.pos[1])):
                    for obj in buttons:
                        obj.button_pressed = False
                    line_button.button_pressed = True
                    current_shape = Pen
                elif tri_r.rect.collidepoint((event.pos[0] - 700, event.pos[1])):
                    for obj in buttons:
                        obj.button_pressed = False
                    tri_r.button_pressed = True
                    current_shape = RightTriangle
                elif tri_e.rect.collidepoint((event.pos[0] - 700, event.pos[1])):
                    for obj in buttons:
                        obj.button_pressed = False
                    tri_e.button_pressed = True
                    current_shape = EquilateralTriangle
                elif rhomb.rect.collidepoint((event.pos[0] - 700, event.pos[1])):
                    for obj in buttons:
                        obj.button_pressed = False
                    rhomb.button_pressed = True
                    current_shape = Rhombus
                else:
                    active_obj = current_shape(start_pos=event.pos)
                    objects.append(active_obj)
                    active_obj.color = current_color

            if event.type == pygame.MOUSEMOTION:
                active_obj.update(current_pos=event.pos)


            if event.type == pygame.MOUSEBUTTONUP:
                active_obj = game_object
        clock.tick(30)
        pygame.display.flip()




if __name__ == '__main__':
    main()