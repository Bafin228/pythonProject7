import pygame

sc = pygame.display.set_mode((700, 700))
clock = pygame.time.Clock()

x = 200
y = 100
fat = 10
FPS = 30
pos = (x, y, fat, fat)
game = True
color = (0, 255, 0)

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