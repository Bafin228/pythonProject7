import pygame
import random

sc = pygame.display.set_mode((800, 500))
pygame.display.set_caption('Вкусно и точка')
clock = pygame.time.Clock()
stoli = ['stoli\glavni stol.png', 'stoli\table govna3.png']
numbers = ['1.gif', '2.png', '3.png', '4.png', '5.png']
x = 200
y = 100
fat = 10
FPS = 30
pos = (x, y, fat, fat)
game = True
color = (0, 255, 0)
pygame.init()
pygame.mixer.music.load('zombie.mp3')


def print_text(message, x, y, font_color=(0, 0, 0), font_type='font.ttf', font_size=30):
    font_type = pygame.font.Font(font_type, font_size)
    text = font_type.render(message, True, font_color)
    sc.blit(text, (x, y))


def show_menu():
    mune = pygame.image.load('fon.png')
    level1 = Button(300, 70)
    level2 = Button(300, 70)

    show = True

    while show:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        sc.blit(mune, (0, 0))

        print_text('Добро пожаловать на сервер безумные зомби', 200, 100)
        level1.draw(250, 150, '1 lvl', None, 50)
        level2.draw(250, 350, '2 lvl', None, 50)
        pygame.display.update()


def start_game():
    # эта функция будет запускать игру после фона
    pass


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





class Player(pygame.sprite.Sprite):
    def __init__(self, img='begun.png'):
        super().__init__()
        self.image = pygame.image.load(img).convert_alpha()
        self.rect = self.image.get_rect()
        self.alive = True
        self.b = pygame.sprite.Group()
        self.stol = None
        self.change_x = 0
        self.change_y = 0
        self.zakaz = None


    def update(self):
        # проверим врезается ли в стены или в ченибудь игрок
        self.rect.x += self.change_x
        self.rect.y += self.change_y
        stol_false = pygame.sprite.spritecollide(self, self.stol, False)
        for i in stol_false:
            if self.change_x > 0:
                self.rect.right = i.rect.left
            else:
                self.rect.left = i.rect.right
        for i in stol_false:
            if self.change_y > 0:
                self.rect.bottom = i.rect.top
            else:
                self.rect.top = i.rect.bottom
        # проверим соприкосновение с заказом
        zakaz = pygame.sprite.spritecollide(self, self.zakaz, False)
        if pygame.sprite.spritecollide(self, self.b, False):
            self.alive = False



class Gstol(pygame.sprite.Sprite):
    def __init__(self, x, y, img='glavni stol.png'):
        super().__init__()
        self.image = pygame.image.load(img).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class DefaultStol(pygame.sprite.Sprite):
    def __init__(self, x, y, img='table govna3.png'):
        super().__init__()
        self.image = pygame.image.load(img).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
class Babka(pygame.sprite.Sprite):
    def __init__(self, x, y, img='babka.png'):
        super().__init__()
        self.image = pygame.image.load(img).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.start = x
        self.stop = x + random.randint(180, 240)
        self.direction = 1

    def update(self):
        if self.rect.x >= self.x:
            self.rect.x = self.stop
            self.direction = -1

        if self.rect.x <= self.start:
            self.rect.x = self.start
            self.direction = 1
        self.rect.x += self.direction * 2



class Terpila(pygame.sprite.Sprite):
    def __init__(self, x, y, img='terpila'):
        super().__init__()
        self.image = pygame.image.load(img).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.start = x
        self.stop = x + 300


class Televisor(pygame.sprite.Sprite):
    def __init__(self, x, y, img='telik.png', ):
        super().__init__()
        self.image = pygame.image.load(img).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Zakaz(pygame.sprite.Sprite):
    def __init__(self, x, y, img='eda'):
        super().__init__()
        self.image = pygame.image.load(img).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def random(self):
        # бабка может задуматься о жизни в любой момент и остановится
        pass


all_sprite = pygame.sprite.Group()
stol_list = pygame.sprite.Group()


stol_coords = [
    [400, 200],
    [300, 100],
    [200, 150]
]

for coord in stol_coords:
    stol = DefaultStol(coord[0], coord[1])
    stol_list.add(stol)
    all_sprite.add(stol)

Gstol_list = pygame.sprite.Group()
gstol = Gstol(600, 150)
Gstol_list.add(gstol)
all_sprite.add(gstol)
player = Player(100, 100)


font = pygame.font.SysFont('Arial', 100, True)
text = font.render('GAME OVER', True, WHITE)





while game:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_d]:
        x += 10
    if keys[pygame.K_w]:
        y -= 10
    if keys[pygame.K_s]:
        y += 10
    if keys[pygame.K_a]:
        x -= 10
    sc.fill((0, 0, 0))
    pygame.display.flip()

pygame.quit()