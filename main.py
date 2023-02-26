import pygame
import random

sc = pygame.display.set_mode((800, 500))
clock = pygame.time.Clock()
stoli = ['stoli\glavni stol.png', 'stoli\table govna3.png']
x = 200
y = 100
fat = 10
FPS = 30
pos = (x, y, fat, fat)
game = True
color = (0, 255, 0)


class Player(pygame.sprite.Sprite):
    def __init__(self, img='begun.png'):
        super().__init__()
        self.image = pygame.image.load(img).convert_alpha()
        self.rect = self.image.get_rect()
        self.alive = True
        self.b = pygame.sprite.Group()
        self.stol = None

    def update(self):
        # проверим врезается ли в стены или в ченибудь игрок
        stol_false = pygame.sprite.spritecollide(self, self.stol, False)


class Gstol(pygame.sprite.Sprite):
    def __init__(self, x1, y1, img='stoli\glavni stol.png'):
        super.__init__()
        self.image0 = pygame.image.load(img).convert_alpha()
        self.rect0 = self.image0.get_rect()
        self.rect0.x1 = x1
        self.rect0.y1 = y1

class DefaultStol(pygame.sprite.Sprite):
    def __init__(self, x, y, img='stoli\table govna3.png'):
        super().__init__()
        self.image = pygame.image.load(img).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
class Babka(pygame.sprite.Sprite):
    def __init__(self, x, y, img = 'babka.png'):
        super().__init__()
        self.image = pygame.image.load(img).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.start = x


class Terpila(pygame.sprite.Sprite):
    def __init__(self, x, y, img = 'terpila'):
        super().__init__()
        self.image = pygame.image.load(img).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y




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
    pos = (x, y, fat, fat)
    sc.fill((0, 0, 0))
    pygame.draw.rect(sc, color, pos,)
    pygame.display.update()

pygame.quit()