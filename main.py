import pygame
import random

sc = pygame.display.set_mode((800, 500))
pygame.display.set_caption('Вкусно и точка')
numbers = ['1.gif', '2.png', '3.png', '4.png', '5.png']
x = 200
y = 100
FPS = 30
game = True
color = (0, 255, 0)
pygame.init()
pygame.mixer.music.load('zombie.mp3')


def print_text(message, x, y, font_color=(0, 0, 0), font_type='font.ttf', font_size=30):
    font_type = pygame.font.Font(font_type, font_size)
    text = font_type.render(message, True, font_color)
    sc.blit(text, (x, y))


def show_menu():
    global show
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
        level1.draw(250, 150, 'ИГРАТЬ', start_game1, 50)
        pygame.display.update()

def start_game1():
    # эта функция будет запускать игру после фона
    global show
    print_text('start lvl1', 200, 100)
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





class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, img='monkey.png'):
        super().__init__()
        self.image = pygame.image.load(img).convert_alpha()
        self.rect = self.image.get_rect()
        self.alive = True
        self.b = pygame.sprite.Group()
        self.stol = None
        self.gstol = None
        self.change_x = 0
        self.change_y = 0
        self.zakaz = None
        self.rect.x = x
        self.rect.y = y
        self.do_take = False


    def update(self):
        # проверим врезается ли в стены или в ченибудь игрок
        if self.do_take:
            zakaz.take -= 1
            print(zakaz.take)
        self.rect.x += self.change_x
        self.rect.y += self.change_y
        stol_false = pygame.sprite.spritecollide(self, self.stol, False)
        if stol_false:
            self.rect.x -= self.change_x
            self.rect.y -= self.change_y
            return
        stol_false = pygame.sprite.spritecollide(self, gstol_list, False)
        if stol_false:
            # я и бабка возле стола
            if pygame.sprite.spritecollide(babka, gstol_list, False):
                self.alive = False
            self.rect.x -= self.change_x
            self.rect.y -= self.change_y
            if zakaz.visible == 0:
                if zakaz.take > 0:
                    self.do_take = True
            return

    def proverka_zakaza(self):
        pass




class Gstol(pygame.sprite.Sprite):
    def __init__(self, x, y, img='glavni stol.png'):
        super().__init__()
        self.image = pygame.image.load(img).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.x = x

class DefaultStol(pygame.sprite.Sprite):
    def __init__(self, x, y, img='stol.png'):
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
        self.stop = x + random.randint(70, 100)
        self.directionx = 1
        self.directiony = 1
        self.sleep = 0
        self.starty = y
        self.stopy = y + random.randint(200, 300)
        self.w = 0

    def update(self):
        if self.sleep > 0:
            self.sleep -= 1
        else:
            if self.rect.x >= self.stop:
                self.rect.x = self.stop
                self.directionx = -1

            if self.rect.x <= self.start:
                self.rect.x = self.start
                self.directionx = 1
            self.rect.x += self.directionx * 2
            # 10 - Как часто, 100 - это сколько стоять
        if random.randint(0, 1000) < 10:
            self.sleep = 100



class Terpila(pygame.sprite.Sprite):
    def __init__(self, x, y, img='terpila.png'):
        super().__init__()
        self.image = pygame.image.load(img).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x * -1
        self.rect.y = y * -1
        self.visible = False
        self.visible_cnt = 0

    def show(self):
        self.visible_cnt = random.randint(60, 180)

    def update(self):
        if self.visible_cnt > 0:
            self.visible_cnt -= 1
            if self.visible_cnt <= 0:
                self.visible_cnt = 0
                self.visible = True
                self.rect.x = self.rect.x * -1
                self.rect.y = self.rect.y * -1
        if self.visible == True:
            if self.rect.y < 100:
                self.rect.y += 1
            elif self.rect.y > 100:
                self.rect.y -= 1
            elif self.rect.x < 400:
                self.rect.x += 1
            elif self.rect.x > 400:
                self.rect.x -= 1
            else:
                self.visible = False
                self.rect.x = 350 * -1
                self.rect.y = 350 * -1
                zakaz.hide()







class Televisor(pygame.sprite.Sprite):
    def __init__(self, x, y, img='telik.png', ):
        super().__init__()
        self.image = pygame.image.load(img).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Zakaz(pygame.sprite.Sprite):
    def __init__(self, x, y, img='eda.png'):
        super().__init__()
        self.image = pygame.image.load(img).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x * -1
        self.rect.y = y * -1
        self.visible = random.randint(100, 500)
        self.take = 150

    def update(self):
        if self.visible > 0:
            self.visible -= 1
            if self.visible <= 0:
                self.rect.x = self.rect.x * -1
                self.rect.y = self.rect.y * -1
                terpila.show()

    def hide(self):
        self.rect.x = self.rect.x * -1
        self.rect.y = self.rect.y * -1
        self.visible = random.randint(100, 500)





all_sprite = pygame.sprite.Group()
stol_list = pygame.sprite.Group()


stol_coords = [
    [400, 300],
    [350, 100],
    [150, 100]
]

for coord in stol_coords:
    stol = DefaultStol(coord[0], coord[1])
    stol_list.add(stol)
    all_sprite.add(stol)

Gstol_list = pygame.sprite.Group()
gstol = Gstol(450, 150)
zakaz = Zakaz(500, 150)
all_sprite.add(zakaz)
all_sprite.add(gstol)
player = Player(50, 150)
# proverka stolov
player.stol = stol_list
all_sprite.add(player)
gstol_list = pygame.sprite.Group()
gstol_list.add(gstol)

#babka
babka = Babka(600, 150)
all_sprite.add(babka)
terpila = Terpila(350, 350)
all_sprite.add(terpila)
font = pygame.font.SysFont('Arial', 100, True)
text1 = font.render('GAME OVER', True, (0, 0, 0))
text2 = font.render('Заказ украден', True, (0, 0, 0))
clock = pygame.time.Clock()
pygame.mixer.music.play(-1)
s = 0


show_menu()


while game:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                player.change_x = -10
            elif event.key == pygame.K_d:
                player.change_x = 10
            elif event.key == pygame.K_w:
                player.change_y = -10
            elif event.key == pygame.K_s:
                player.change_y = 10

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                player.change_x = 0
            elif event.key == pygame.K_d:
                player.change_x = 0
            elif event.key == pygame.K_w:
                player.change_y = 0
            elif event.key == pygame.K_s:
                player.change_y = 0
        if show == False:
            if s == 0:
                pygame.mixer.music.pause()
                pygame.mixer.music.load('fon.mp3')
                pygame.mixer.music.unpause()
                pygame.mixer.music.play(-1)
                s += 1
                pygame.display.update()
            mune1 = pygame.image.load('fon1.png')
            sc.blit(mune1, (0, 0))

    sc.fill((0, 0, 0))
    if not player.alive:
        sc.blit(text1, (250, 100))
    else:
        all_sprite.update()
        all_sprite.draw(sc)

    pygame.display.flip()
    clock.tick(60)


pygame.quit()