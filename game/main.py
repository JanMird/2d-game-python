import pygame
from tank import tank
from block import block
from enemy import enemy

from random import randint

WIDTH = 800
HEIGHT = 650
FPS = 30

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("tanks")
clock = pygame.time.Clock()


def game():
    forblockwidth = block()
    blockwidth = forblockwidth.rect.width

    all_sprites = pygame.sprite.Group()
    tank_sprites = pygame.sprite.Group()
    bullet_sprites = pygame.sprite.Group()
    block_sprites = pygame.sprite.Group()
    enemy_sprites = pygame.sprite.Group()

    tanka = tank()
    tanka.rect.x = 100
    tanka.rect.y = 200
    all_sprites.add(tanka)
    tank_sprites.add(tanka)

    enemya = enemy()
    enemya.rect.x = 300
    enemya.rect.y = 300
    all_sprites.add(enemya)
    enemy_sprites.add(enemya)

    enemyb = enemy()
    enemyb.rect.x = 550
    enemyb.rect.y = 550
    all_sprites.add(enemyb)
    enemy_sprites.add(enemyb)

    enemyc = enemy()
    enemyc.rect.x = 600
    enemyc.rect.y = 300
    all_sprites.add(enemyc)
    enemy_sprites.add(enemyc)

    enemyd = enemy()
    enemyd.rect.x = 300
    enemyd.rect.y = 600
    all_sprites.add(enemyd)
    enemy_sprites.add(enemyd)

    for _ in range(200):
        while True:
            x = randint(0, screen.get_width() // blockwidth - 1) * blockwidth
            y = randint(3, screen.get_height() // blockwidth - 1) * blockwidth
            check = pygame.Rect(x, y, blockwidth, blockwidth)
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

    running = True
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 'exit'
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    k = tanka.shoot()
                    all_sprites.add(k)
                    bullet_sprites.add(k)
                if event.key == pygame.K_LEFT:
                    keypressedleft = True
                    pressedkeys += 1
                    tanka.direction = 'left'
                elif event.key == pygame.K_RIGHT:
                    keypressedright = True
                    pressedkeys += 1
                    tanka.direction = 'right'
                elif event.key == pygame.K_DOWN:
                    keypresseddown = True
                    pressedkeys += 1
                    tanka.direction = 'down'
                elif event.key == pygame.K_UP:
                    pressedkeys += 1
                    keypressedup = True
                    tanka.direction = 'up'
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
                if pressedkeys != 0:
                    if keypresseddown:
                        tanka.direction = 'down'
                    elif keypressedup:
                        tanka.direction = 'up'
                    elif keypressedright:
                        tanka.direction = 'right'
                    elif keypressedleft:
                        tanka.direction = 'left'

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
                buldied = 0
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
                            buldied = 1
                            break
                    if buldied == 0:
                        for j in enemy_sprites:
                            if j.rect.colliderect(i.rect):
                                all_sprites.remove(i)
                                bullet_sprites.remove(i)
                                j.health -= i.damage
                                buldied = 1
                                break
                    if buldied == 0:
                        for j in tank_sprites:
                            if j.rect.colliderect(i.rect):
                                all_sprites.remove(i)
                                bullet_sprites.remove(i)
                                j.health -= i.damage
                                buldied = 1
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
                for j in enemy_sprites:
                    if j.rect.colliderect(i.rect) and j != i:
                        i.rect.x = i.oldx
                        i.rect.y = i.oldy
                        break
                bul = i.shoot()
                if bul != None:
                    all_sprites.add(bul)
                    bullet_sprites.add(bul)
        for i in all_sprites:
            if i.type != 'bullet':
                if i.health <= 0:
                    all_sprites.remove(i)
                    if i.type == 'block':
                        block_sprites.remove(i)
                    elif i.type == 'enemy':
                        enemy_sprites.remove(i)
                    elif i.type == 'tank':
                        tank_sprites.remove(i)
        if len(tank_sprites) == 0:
            return 'defeat'
        if len(enemy_sprites) == 0:
            return 'victory'

        screen.fill(BLACK)
        all_sprites.draw(screen)
        pygame.display.flip()


button_width = 350
button_height = 65


class button():
    def __init__(self, text, x, y, tsize=50, tcol=BLUE, bg=GREEN, type=None):
        self.type = type
        self.font = pygame.font.SysFont("impact", tsize)
        self.text = self.font.render(text, True, tcol)
        self.text_rect = self.text.get_rect()
        self.but_rect = self.text.get_rect()
        self.but_rect.width = button_width
        self.but_rect.height = button_height
        self.text_rect.center = (x, y)
        self.but_rect.center = (x, y)
        self.state = 0
        self.clicked = 0
        self.rect_col = bg

    def change_but(self, text='txt not stated', tcol=GREEN, bg=BLUE):
        self.text = self.font.render(text, True, tcol)
        self.text_rect = self.text.get_rect()
        self.text_rect.center = self.but_rect.center
        self.rect_col = bg

    def show(self):
        pygame.draw.rect(screen, self.rect_col, self.but_rect)
        screen.blit(self.text, self.text_rect)

    def update(self, text1='movedon', text2='default', tcol=GREEN, bg=RED):
        x, y = pygame.mouse.get_pos()
        if self.state == 0:
            if x <= self.but_rect.x + self.but_rect.width and x >= self.but_rect.x \
                    and y <= self.but_rect.y + self.but_rect.height \
                    and y >= self.but_rect.y:
                self.change_but(text1, tcol, bg)
                self.state = 1
        if self.state == 1:
            if x < self.but_rect.x or x > self.but_rect.x + self.but_rect.width \
                    or y < self.but_rect.y or y > self.but_rect.y + self.but_rect.height:
                self.change_but(text2, tcol=BLUE, bg=GREEN)
                self.state = 0

    def ismouseon(self, pos):
        if pos[0] <= self.but_rect.x + self.but_rect.width and pos[0] >= self.but_rect.x \
                and pos[1] <= self.but_rect.y + self.but_rect.height \
                and pos[1] >= self.but_rect.y:
            return 1
        else:
            return 0


def mainmanu():
    running = True
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 'exit'
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                clickedonbut = 0
                for i in buttons:
                    if i.ismouseon(pos):
                        i.clicked = 1
                        clickedonbut = 1
                        break
                if clickedonbut == 0:
                    for i in buttons:
                        i.clicked = 0
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                for i in buttons:
                    if i.ismouseon(pos) and i.clicked == 1:
                        return i.type
                    i.clicked = 0

        screen.fill(BLACK)
        for i in buttons:
            i.update(text2=i.type)
            i.show()
        pygame.display.update()


buttons = []
button1 = button(text='start', x=400, y=300, tsize=50, tcol=BLUE, bg=GREEN, type='start')
button2 = button(text='exit', x=400, y=450, type='exit')
buttons.append(button1)
buttons.append(button2)

running = True
while running:
    res = mainmanu()
    if res == 'start':
        res = game()
    if res == 'exit':
        running = False
        pygame.quit()

