import pygame
from pygame.locals import *
import time
import random

SIZE = 20

BACKGROUND_COLOR = (110, 110, 5)
pineapple_image = pygame.image.load("pineapple.jpg")
apple_image = pygame.image.load("red-apple.jpg")
snake_image = pygame.image.load("block.jpg")
bg_image = pygame.image.load("background.jpg")

class Pineapple:
    def __init__(self, parent_screen):
        self.parent_screen = parent_screen
        self.image = pineapple_image.convert()
        self.x = 240
        self.y = 240

    def draw(self):
        self.parent_screen.blit(self.image, (self.x, self.y))
        # pygame.display.flip()

    def move(self):
        self.x = random.randint(1,31)*SIZE
        self.y = random.randint(1,23)*SIZE

class Apple:
    def __init__(self, parent_screen):
        self.parent_screen = parent_screen
        self.image = apple_image.convert()
        self.x = 120
        self.y = 120

    def draw(self):
        self.parent_screen.blit(self.image, (self.x, self.y))
        # pygame.display.flip()

    def move(self):
        self.x = random.randint(1,31)*SIZE
        self.y = random.randint(1,23)*SIZE


class Snake:
    def __init__(self, parent_screen):
        self.parent_screen = parent_screen
        self.image = snake_image.convert()
        self.direction = 'down'

        self.length = 1
        self.x = [20]
        self.y = [20]

    def move_left(self):
        self.direction = 'left'

    def move_right(self):
        self.direction = 'right'

    def move_up(self):
        self.direction = 'up'

    def move_down(self):
        self.direction = 'down'

    def walk(self):
        for i in range(self.length-1,0,-1):
            self.x[i] = self.x[i-1]
            self.y[i] = self.y[i-1]

        if self.direction == 'left':
            self.x[0] -= SIZE
        if self.direction == 'right':
            self.x[0] += SIZE
        if self.direction == 'up':
            self.y[0] -= SIZE
        if self.direction == 'down':
            self.y[0] += SIZE

        self.draw()

    def draw(self):
        for i in range(self.length):
            self.parent_screen.blit(self.image, (self.x[i], self.y[i]))

        # pygame.display.flip()

    def increase_length(self):
        self.length += 1
        self.x.append(-1)
        self.y.append(-1)

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("змея пожирает яблоки и не только")

        pygame.mixer.init()


        self.surface = pygame.display.set_mode((640, 480))
        self.snake = Snake(self.surface)
        self.snake.draw()
        self.pineapple = Pineapple(self.surface)
        self.pineapple.draw()
        self.apple = Apple(self.surface)
        self.apple.draw()
        self.point = 0
        #self.fruit_interval = 25
        #self.last_fruit_time = 0



    def reset(self):
        self.snake = Snake(self.surface)
        self.pineapple = Pineapple(self.surface)
        self.apple = Apple(self.surface)
        self.snake = Snake(self.surface)
        self.pineapple = Pineapple(self.surface)
        self.apple = Apple(self.surface)
        self.point = 0

    def is_collision(self, x1, y1, x2, y2):
        if x1 >= x2 and x1 < x2 + SIZE:
            if y1 >= y2 and y1 < y2 + SIZE:
                return True
        return False

    def render_background(self):
        bg = bg_image
        self.surface.blit(bg, (0,0))

    def play(self):
        self.render_background()
        self.snake.walk()
        self.apple.draw()
        self.pineapple.draw()
        self.display_score()
        

        pygame.display.flip()

        for i in range(self.snake.length):
            if self.is_collision(self.snake.x[i], self.snake.y[i], self.apple.x, self.apple.y):
                self.snake.increase_length()
                self.point += 1
                self.apple.move()

            if self.is_collision(self.snake.x[i], self.snake.y[i], self.pineapple.x, self.pineapple.y):
                self.snake.increase_length()
                self.point += 3
                self.pineapple.move()

        for i in range(3, self.snake.length):
            if self.is_collision(self.snake.x[0], self.snake.y[0], self.snake.x[i], self.snake.y[i]):
                raise "Collision Occurred"


        if not (0 <= self.snake.x[0] <= 640 and 0 <= self.snake.y[0] <= 480):
            raise "Hit the boundry error"

    def display_score(self):
        font = pygame.font.SysFont('arial',30)
        score = font.render(f"Score: {self.point}",True,(200,200,200))
        self.surface.blit(score,(240,10))

    def show_game_over(self):
        self.render_background()
        font = pygame.font.SysFont('arial', 30)
        line1 = font.render(f"Game is over!", True, (255, 255, 255))
        self.surface.blit(line1, (80, 100))
        line2 = font.render(f"You ate {(self.snake.length)-1} fruits", True, (220,20,60))
        self.surface.blit(line2, (80, 150))
        line5 = font.render(f"Your score is {self.point} ", True, (220,20,60))
        self.surface.blit(line5, (80, 200))
        line5 = font.render("To play again press Enter", True, (255, 255, 255))
        self.surface.blit(line5, (80, 250))
        line4 = font.render("To exit press Escape!", True, (255, 255, 255))
        self.surface.blit(line4, (80, 300))
        
        pygame.mixer.music.pause()
        pygame.display.flip()
    
    def run(self):
        running = True
        pause = False

        while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False

                    if event.key == K_RETURN:
                        pygame.mixer.music.unpause()
                        pause = False

                    if not pause:
                        if event.key == K_LEFT:
                            self.snake.move_left()

                        if event.key == K_RIGHT:
                            self.snake.move_right()

                        if event.key == K_UP:
                            self.snake.move_up()

                        if event.key == K_DOWN:
                            self.snake.move_down()

                elif event.type == QUIT:
                    running = False
            try:

                if not pause:
                    self.play()

            except Exception as e:
                self.show_game_over()
                pause = True
                self.reset()

            time.sleep(.1)

if __name__ == '__main__':
    game = Game()
    game.run()