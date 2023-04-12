import pygame

pygame.init()
pygame.font.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 255, 0)
GREEN = (0, 0, 255)

FPS = 240

WIDTH, HEIGHT = 600, 700

ROWS = COLS = 100

TOOLBAR_HEIGHT = HEIGHT - WIDTH

PIXEL_SIZE = WIDTH // COLS

BG_COLOR = WHITE

DRAW_GRID_LINES = True



class Button:
    def __init__(self, x, y, width, height, color, text=None, text_color=BLACK):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.text = text
        self.text_color = text_color

    def draw(self, win):
        pygame.draw.rect(
            win, self.color, (self.x, self.y, self.width, self.height))
        pygame.draw.rect(
            win, BLACK, (self.x, self.y, self.width, self.height), 2)
        if self.text:
            button_font = get_font(22)
            text_surface = button_font.render(self.text, 1, self.text_color)
            win.blit(text_surface, (self.x + self.width /
                                    2 - text_surface.get_width()/2, self.y + self.height/2 - text_surface.get_height()/2))

    def clicked(self, pos):
        x, y = pos

        if not (x >= self.x and x <= self.x + self.width):
            return False
        if not (y >= self.y and y <= self.y + self.height):
            return False

        return True
    
def get_font(size):
    return pygame.font.SysFont("comicsans", size)

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Drawing Program")


def init_grid(rows, cols, color):
    grid = []

    for i in range(rows):
        grid.append([])
        for _ in range(cols):
            grid[i].append(color)

    return grid


def draw_grid(win, grid):
    for i, row in enumerate(grid):
        for j, pixel in enumerate(row):
            pygame.draw.rect(win, pixel, (j * PIXEL_SIZE, i *
                                          PIXEL_SIZE, PIXEL_SIZE, PIXEL_SIZE))

    if DRAW_GRID_LINES:
        for i in range(ROWS + 1):
            pygame.draw.line(win, BLACK, (0, i * PIXEL_SIZE),
                             (WIDTH, i * PIXEL_SIZE))

        for i in range(COLS + 1):
            pygame.draw.line(win, BLACK, (i * PIXEL_SIZE, 0),
                             (i * PIXEL_SIZE, HEIGHT - TOOLBAR_HEIGHT))


def draw(win, grid, buttons):
    win.fill(BG_COLOR)
    draw_grid(win, grid)

    for button in buttons:
        button.draw(win)

    pygame.display.update()


def get_row_col_from_pos(pos):
    x, y = pos
    row = y // PIXEL_SIZE
    col = x // PIXEL_SIZE

    if row >= ROWS:
        raise IndexError

    return row, col


run = True
clock = pygame.time.Clock()
grid = init_grid(ROWS, COLS, BG_COLOR)
drawing_color = BLACK

button_y = HEIGHT - TOOLBAR_HEIGHT/2 - 25
buttons = [
    Button(10, button_y, 50, 50, BLACK),
    Button(70, button_y, 50, 50, RED),
    Button(130, button_y, 50, 50, GREEN),
    Button(190, button_y, 50, 50, BLUE),
    Button(250, button_y, 50, 50, WHITE, "Erase", BLACK),
    Button(310, button_y, 50, 50, WHITE, "Clear", BLACK)
]

while run:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if pygame.mouse.get_pressed()[0]:
            pos = pygame.mouse.get_pos()

            try:
                row, col = get_row_col_from_pos(pos)
                grid[row][col] = drawing_color
            except IndexError:
                for button in buttons:
                    if not button.clicked(pos):
                        continue

                    drawing_color = button.color
                    if button.text == "Clear":
                        grid = init_grid(ROWS, COLS, BG_COLOR)
                        drawing_color = BLACK

    draw(WIN, grid, buttons)

pygame.quit()








import pygame as pg
import random

pg.init()
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


screen = pg.display.set_mode((1200, 700))
pg.display.set_caption("PAINTING")
clock = pg.time.Clock()


blue = (0, 0, 100)
red = (150, 0, 0)
black = (20, 20, 20)
pink = (200, 0, 200)

redRect = pg.Rect(0, 0, 50, 50)
blueRect = pg.Rect(50, 0, 50, 50)
blackRect = pg.Rect(150, 0, 50, 50)
pinkRect = pg.Rect(100, 0, 50, 50)

rects = [[red, redRect], [blue, blueRect], [black, blackRect], [pink, pinkRect]]
        #self.colour = colour
colour = (100, 120, 140)
def colour_pick():
    posX, posY = pg.mouse.get_pos()
    clik = pg.mouse.get_pressed()
    global colour
    if clik[0]:
        if posX < 50 and posY < 50:
            colour = red
        elif posX < 100 and posX > 50 and posY < 50:
            colour = blue
        elif posX < 150 and posX > 100 and posY < 50:
            colour = pink
        elif posX < 200 and posX > 150 and posY < 50:
            colour = (0, 0, 0)

def draw(mode):
    posX, posY = pg.mouse.get_pos()
    clik = pg.mouse.get_pressed()
    if clik[0]:
        if mode == "line":
            pg.draw.circle(screen, colour, (posX, posY), 30)
        elif mode == "square":
            pg.draw.rect(screen, colour, pg.Rect(posX, posY, 80, 100),1)
        elif mode == "circle":
            pg.draw.circle(screen, colour, (posX, posY), 60,1)
        elif mode == "eraser":
             pg.draw.circle(screen, (0,0,0), (posX, posY), 40)
def clear_all():
        key = pg.key.get_pressed()
        if key[pg.K_LCTRL] and key[pg.K_c]:
            screen.fill((0, 0, 0))

figure = "line"

RUN = True
while RUN:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            RUN = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_c:
                figure = 'circle'
            elif event.key == pg.K_s:
                figure = 'square'
            elif event.key == pg.K_e:
                figure = 'eraser'
            elif event.key == pg.K_l:
                figure = 'line'

    for colrs in rects:
        pg.draw.rect(screen, colrs[0], colrs[1])

    clik = pg.mouse.get_pressed()
    posX, posY = pg.mouse.get_pos()
    draw(figure)

    colour_pick()

    clear_all()
    clock.tick(600)
    pg.display.update()