import pygame
import time
import random

pygame.init()
width = 800
height = 800
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (128,0,0)
green = (0, 255, 0)
blue = (50, 153, 213)
DarkMagenta = (139, 0, 139)

pygame.init()

window = pygame.display.set_mode((width, height))
pygame.display.set_caption('Snake')

clock = pygame.time.Clock()

snake_block = 40
snake_speed = 5

font_style = pygame.font.SysFont(None, 40)
score_font = pygame.font.SysFont(None, 35)
def message(text, color, x, y):
    font = pygame.font.SysFont(None, 40)
    rendered_text = font.render(text, True, color)
    window.blit(rendered_text, (x, y))

def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(window, DarkMagenta, [x[0], x[1], snake_block, snake_block])

def pause(isPause,snakesp):
    if(isPause == False):
        message("пауза",green,width/2 - 100, height/2)
        snakesp = 0
    else:


def game_loop():
    game_over = False
    game_close = False
    isPause = False


    x1 = width / 2
    y1 = height / 2

    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1

    foodx = round(random.randrange(0, width - snake_block) / snake_block) * snake_block
    foody = round(random.randrange(0, height - snake_block) / snake_block) * snake_block
    score = 1

    while not game_over:

        if game_close:
            import end
            end.game_end()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pause(isPause,snake_speed)
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    x1_change = 0
                    y1_change = -snake_block
                elif event.key == pygame.K_DOWN:
                    x1_change = 0
                    y1_change = snake_block



        if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        window.fill(black)
        pygame.draw.rect(window, red, [foodx, foody, snake_block, snake_block])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        our_snake(snake_block, snake_List)

        score_text = score_font.render("Счёт: " + str(score), True, white)
        window.blit(score_text, [10, 10])
        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, width - snake_block) / snake_block) * snake_block
            foody = round(random.randrange(0, height - snake_block) / snake_block) * snake_block
            Length_of_snake += 1
            score += 1
        clock.tick(snake_speed)

    pygame.quit()
    quit()
