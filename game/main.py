import pygame
from tank import tank
from block import block
from enemy import enemy

from random import randint

WIDTH = 800
HEIGHT = 650
FPS = 30

# Задаем цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

twidth = 30
buwidth = 5
blwidth = 30

# Создаем игру и окно
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()

all_sprites = pygame.sprite.Group()
tank_sprites = pygame.sprite.Group()
bullet_sprites = pygame.sprite.Group()
block_sprites = pygame.sprite.Group()
enemy_sprites = pygame.sprite.Group()

tank = tank()
all_sprites.add(tank)
tank_sprites.add(tank)

enemy = enemy()
enemy.rect.x = 300
enemy.rect.y = 300
all_sprites.add(enemy)
enemy_sprites.add(enemy)

for _ in range(200):
    while True:
        x = randint(0, screen.get_width() // blwidth - 1) * blwidth
        y = randint(0, screen.get_height() // blwidth - 1) * blwidth
        check = pygame.Rect(x, y, blwidth, blwidth)
        k = 0
        for i in all_sprites:
            if check.colliderect(i.rect):
                k = 1
        if k == 0:
            break
    a = block()
    a.rect.x = x
    a.rect.y = y
    all_sprites.add(a)
    block_sprites.add(a)

keypressedup = False
keypresseddown = False
keypressedleft = False
keypressedright = False
pressedkeys = 0

# Цикл игры
running = True
while running:
    # Держим цикл на правильной скорости
    clock.tick(FPS)
    # Ввод процесса (события)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                k = tank.shoot()
                all_sprites.add(k)
                bullet_sprites.add(k)
            if event.key == pygame.K_LEFT:
                keypressedleft = True
                pressedkeys += 1
                tank.direction = 'left'
            elif event.key == pygame.K_RIGHT:
                keypressedright = True
                pressedkeys += 1
                tank.direction = 'right'
            elif event.key == pygame.K_DOWN:
                keypresseddown = True
                pressedkeys += 1
                tank.direction = 'down'
            elif event.key == pygame.K_UP:
                pressedkeys += 1
                keypressedup = True
                tank.direction = 'up'
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                keypressedleft = False
            elif event.key == pygame.K_RIGHT:
                keypressedright = False
            elif event.key == pygame.K_DOWN:
                keypresseddown = False
            elif event.key == pygame.K_UP:
                keypressedup = False
            pressedkeys -= 1
            if pressedkeys == 0:
                keypressed = False
            else:
                if keypresseddown:
                    tank.direction = 'down'
                elif keypressedup:
                    tank.direction = 'up'
                elif keypressedright:
                    tank.direction = 'right'
                elif keypressedleft:
                    tank.direction = 'left'

    for i in all_sprites:
        if i.type == 'tank':
            if keypresseddown or keypressedup or keypressedleft or keypressedright:
                i.update()
                for j in block_sprites:
                    if j.rect.colliderect(i.rect):
                        i.rect.x = i.oldx
                        i.rect.y = i.oldy
                        break
                for j in enemy_sprites:
                    if j.rect.colliderect(i.rect):
                        i.rect.x = i.oldx
                        i.rect.y = i.oldy
                        break

        if i.type == 'bullet':
            k = 0
            i.update()
            if i.rect.x > screen.get_width() or i.rect.x + i.rect.width < 0 \
                    or i.rect.y > screen.get_height() or i.rect.y + i.rect.height < 0:
                all_sprites.remove(i)
                bullet_sprites.remove(i)
            else:
                for j in block_sprites:
                    if j.rect.colliderect(i.rect):
                        all_sprites.remove(i)
                        bullet_sprites.remove(i)
                        j.health -= i.damage
                        k = 1
                        break
                if k == 0:
                    for j in enemy_sprites:
                        if j.rect.colliderect(i.rect):
                            all_sprites.remove(i)
                            bullet_sprites.remove(i)
                            j.health -= i.damage
                            k = 1
                            break
                if k == 0:
                    for j in tank_sprites:
                        if j.rect.colliderect(i.rect):
                            all_sprites.remove(i)
                            bullet_sprites.remove(i)
                            j.health -= i.damage
                            k = 1
                            break

        if i.type == 'enemy':
            i.update()
            for j in block_sprites:
                if j.rect.colliderect(i.rect):
                    i.rect.x = i.oldx
                    i.rect.y = i.oldy
                    break
            for j in tank_sprites:
                if j.rect.colliderect(i.rect):
                    i.rect.x = i.oldx
                    i.rect.y = i.oldy
                    break
            k = i.shoot()
            if k != None:
                all_sprites.add(k)
                bullet_sprites.add(k)
    for i in all_sprites:
        if i.type is not 'bullet':
            if i.health <= 0:
                all_sprites.remove(i)
                if i.type == 'block':
                    block_sprites.remove(i)
                elif i.type == 'enemy':
                    enemy_sprites.remove(i)
                elif i.type == 'tank':
                    tank_sprites.remove(i)
    # Рендеринг
    screen.fill(BLACK)
    all_sprites.draw(screen)
    # После отрисовки всего, переворачиваем экран
    pygame.display.flip()

pygame.quit()
