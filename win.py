import pygame
import menu
sc = pygame.display.set_mode((800, 500))

def show_win():
    global show
    mune = pygame.image.load('images/papich.png')
    win = menu.Button(400, 200)
    show = True
    while show:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        sc.blit(mune, (0, 0))
        menu.print_text('ТЫ ВЫИГРАЛ', 200, 100)
        pygame.display.update()

def win1():
    # эта функция будет запускать игру после фона
    global show
    show = False
