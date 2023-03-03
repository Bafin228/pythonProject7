import pygame
import random
import menu
import win

sc = pygame.display.set_mode((800, 500))
pygame.display.set_caption('Вкусно и точка')
x = 200
y = 100
FPS = 30
game = True
color = (0, 255, 0)
color1 = (0, 33, 55)
pygame.init()
pygame.mixer.music.load('music/zombie.mp3')


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, img='images/monkey.png'):
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
        self.t = True

    def update(self):
        if pygame.sprite.spritecollide(self, terpila_list, False):
            self.alive = False
        if self.do_take:
            zakaz.take -= 1
            print(zakaz.take)
        self.rect.x += self.change_x
        self.rect.y += self.change_y
        # проверим врезается ли в стены или в ченибудь игрок
        stol_false = pygame.sprite.spritecollide(self, self.stol, False)
        if stol_false:
            self.rect.x -= self.change_x
            self.rect.y -= self.change_y
            return
        stol_false = pygame.sprite.spritecollide(self, wall_list, False)
        if stol_false:
            self.rect.x -= self.change_x
            self.rect.y -= self.change_y
            return
        stol_false = pygame.sprite.spritecollide(self, gstol_list, False)
        if self.do_take and self.t and stol_false:
            zakaz.take -= 1
            print(zakaz.take)
        else:
            zakaz.take = 180
        # чтобы стал забираться нужно зажать D
        if stol_false:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    self.t = False
                else:
                    self.t = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a:
                    self.t = False
                else:
                    self.t = True
            # я и бабка возле стола
            if pygame.sprite.spritecollide(babka, gstol_list, False):
                self.alive = False
            self.rect.x -= self.change_x
            self.rect.y -= self.change_y
            if zakaz.visible == 0 and stol_false:
                if zakaz.take > 0:
                    self.do_take = True
                if zakaz.take <= 0 and stol_false:
                    pygame.mixer.music.pause()
                    pygame.mixer.music.load('music/win.mp3')
                    pygame.mixer.music.unpause()
                    pygame.mixer.music.play(-1)
                    win.show_win()
                    pygame.display.update()

            return


class Gstol(pygame.sprite.Sprite):
    def __init__(self, x, y, img='images/glavni stol.png'):
        super().__init__()
        self.image = pygame.image.load(img).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.x = x


class DefaultStol(pygame.sprite.Sprite):
    def __init__(self, x, y, img='images/stol.png'):
        super().__init__()
        self.image = pygame.image.load(img).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class Babka(pygame.sprite.Sprite):
    def __init__(self, x, y, img='images/babka.png'):
        super().__init__()
        self.image = pygame.image.load(img).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.start = x
        self.stop = x + 120
        self.directionx = 1
        self.directiony = 1
        self.sleep = 0
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
        if random.randint(0, 1000) < 7:
            self.sleep = 80


class Terpila(pygame.sprite.Sprite):
    def __init__(self, x, y, img='images/terpila.png'):
        super().__init__()
        self.image = pygame.image.load(img).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x * -1
        self.rect.y = y * -1
        self.visible = False
        self.visible_cnt = 0

    def show(self):
        self.visible_cnt = random.randint(20, 50)

    def update(self):
        if self.visible_cnt > 0:
            self.visible_cnt -= 1
            if self.visible_cnt <= 0:
                self.visible_cnt = 0
                self.visible = True
                self.rect.x = self.rect.x * -1
                self.rect.y = self.rect.y * -1
        if self.visible == True:
            if self.rect.y < 150:
                self.rect.y += 1
            elif self.rect.y > 150:
                self.rect.y -= 1
            elif self.rect.x < 400:
                self.rect.x += 1
            elif self.rect.x > 400:
                self.rect.x -= 1
            else:
                self.visible = False
                self.rect.x = 350 * -1
                self.rect.y = 400 * -1
                zakaz.hide()


class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y, widht, height):
        super().__init__()

        self.image = pygame.Surface([widht, height])
        self.image.fill(color1)
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x


class Zakaz(pygame.sprite.Sprite):
    def __init__(self, x, y, img='images/eda.png'):
        super().__init__()
        self.image = pygame.image.load(img).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x * -1
        self.rect.y = y * -1
        self.visible = random.randint(30, 50)
        self.take = 180

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
        self.visible = random.randint(30, 50)


all_sprite = pygame.sprite.Group()
stol_list = pygame.sprite.Group()

stol_coords = [
    [450, 330],
    [450, 100],
    [450, 50],
    [250, 200],
    [250, 150],
    [250, 100],
    [250, 50],
    [250, 260],
    [250, 310],
    [450, 400]
]

wall_coords = [
    [0, 0, 10, 500],
    [790, 0, 10, 500],
    [10, 0, 790, 10],
    [0, 490, 790, 10]
]

for coord in stol_coords:
    stol = DefaultStol(coord[0], coord[1])
    stol_list.add(stol)
    all_sprite.add(stol)

wall_list = pygame.sprite.Group()
for coord1 in wall_coords:
    wall = Wall(coord1[0], coord1[1], coord1[2], coord1[3])
    wall_list.add(wall)
    all_sprite.add(wall)

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

# babka
babka = Babka(580, 150)
all_sprite.add(babka)
terpila = Terpila(350, 400)
terpila_list = pygame.sprite.Group()
terpila_list.add(terpila)
all_sprite.add(terpila)
font = pygame.font.SysFont('Arial', 100, True)
text1 = font.render('GAME OVER', True, (0, 0, 0))
text2 = font.render('Заказ украден', True, (0, 0, 0))
clock = pygame.time.Clock()
pygame.mixer.music.play(-1)
s = 0

menu.show_menu()

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
        if menu.show == False:
            if s == 0:
                pygame.mixer.music.pause()
                pygame.mixer.music.load('music/fon.mp3')
                pygame.mixer.music.unpause()
                pygame.mixer.music.play(-1)
                s += 1
                pygame.display.update()

    sc.fill((255, 255, 153))
    if not player.alive:
        sc.blit(text1, (250, 100))
        pygame.mixer.music.pause()


    else:
        all_sprite.update()
        all_sprite.draw(sc)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
