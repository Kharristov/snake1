import pygame as pg
pg.init()
from pygame.color import THECOLORS
def game_end():
    sizes = [800,800]

    window = pg.display.set_mode(sizes)
    my_font = pg.font.SysFont('arial', 40)
    surface = pg.Surface(sizes)
    pg.display.set_caption("Конец")

    x = 350
    y = [300, 600]
    wight = 350
    hight = 80
    endlist = ['Начать заново',  'Выход']
    end_open = True

    j = 5
    while end_open:
        for i in range (2):
            pg.draw.rect(surface, THECOLORS['red'],[x,y[i], wight, hight], 0,30)
            text = my_font.render(endlist[i], True, THECOLORS['black'])
            surface.blit(text,[x+40, y[i]+20])

        text = my_font.render('конец',True, THECOLORS['white'])
        surface.blit(text,[150,10])
        window.blit(surface,[0,0])
        pg.display.update()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                quit()
            elif event.type == pg.MOUSEBUTTONDOWN:
                xm, ym = pg.mouse.get_pos()
                for j in range(2):
                    if((xm > x) and (xm < x + wight) and (ym > y[j]) and (ym < y[j] + hight)):
                        break
                if j == 0:

                    import snake
                    snake.game_loop()
                if j == 1:
                    quit()

game_end()