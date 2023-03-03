import pygame
sc = pygame.display.set_mode((800, 500))

def print_text(message, x, y, font_color=(0, 0, 0), font_type='tupo-vyaz_bold.ttf', font_size=30):
    font_type = pygame.font.Font(font_type, font_size)
    text = font_type.render(message, True, font_color)
    sc.blit(text, (x, y))


def show_menu():
    global show
    mune = pygame.image.load('images/fon.png')
    level1 = Button(300, 70)

    show = True

    while show:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        sc.blit(mune, (0, 0))

        print_text('Добро пожаловать на сервер безумные зомби', 200, 100)
        level1.draw(250, 150, 'ИГРАТЬ', start_game1, 50)
        pygame.display.update()

def start_game1():
    # эта функция будет запускать игру после фона
    global show
    show = False


class Button:
    def __init__(self, widht, height):
        self.widht = widht
        self.height = height
        self.inactive = (13, 162, 58)
        self.active = (23, 204, 58)

    def draw(self, x, y, message, action=None, font_size=30):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if x < mouse[0] < x + self.widht and y < mouse[1] < y + self.height:
            pygame.draw.rect(sc, self.active, (x, y, self.widht, self.height))

            if click[0] == 1:
                pygame.time.delay(100)
                if action is not None:
                    action()

        else:
            pygame.draw.rect(sc, self.inactive, (x, y, self.widht, self.height))

        print_text(message=message, x=x+10, y=y+10, font_size=font_size)