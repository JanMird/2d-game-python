import pygame
from tank import tank
from block import block
from enemy import enemy
from button import button
import time

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

smalltextsize = 34
bigtextsize = 68
defaulinterx = 350
defaulintery = 30
defaultintercol = RED
interspace = 30


def game():
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)

    startblockem = 200
    blockgencooldown = FPS * 15
    blockgentick = 0
    blockgennum = 10
    blockgenincr = 1
    startenemyem = 3
    enemygencooldown = FPS * 15
    enemygentick = 0
    enemygennum = startenemyem + 1
    enemygenincr = 1

    smalltextsize = 34
    bigtextsize = 68
    defaulinterx = 350
    defaulintery = 30
    defaultintercol = RED
    interspace = 30

    smalltextsize = 34
    bigtextsize = 68
    defaulinterx = 350
    defaulintery = 30
    defaultintercol = RED
    interspace = 30

    def drawstats(obj, textstr='default text', color=defaultintercol, \
                  x=defaulinterx, y=defaulintery, size=smalltextsize, \
                  screen=screen, time=0):
        textstr = 'HEALTH : ' + str(obj.health)
        st = pygame.font.SysFont('impact', size)
        text = st.render(textstr, True, color)
        text_rect = text.get_rect()
        text_rect.center = (x, y)
        screen.blit(text, text_rect)
        textstr2 = 'TIME : ' + str(time)
        st = pygame.font.SysFont('impact', size)
        text2 = st.render(textstr2, True, color)
        text_rect2 = text.get_rect()
        text_rect2.center = (x + text_rect.width + interspace, y)
        screen.blit(text2, text_rect2)

    def blockgen(n):
        for _ in range(n):
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
            a = block(x=x, y=y)
            all_sprites.add(a)
            block_sprites.add(a)

    def enemygen(n):
        for _ in range(n):
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
            a = enemy(x=x, y=y)
            all_sprites.add(a)
            enemy_sprites.add(a)

    forblockwidth = block()
    blockwidth = forblockwidth.rect.width

    all_sprites = pygame.sprite.Group()
    tank_sprites = pygame.sprite.Group()
    bullet_sprites = pygame.sprite.Group()
    block_sprites = pygame.sprite.Group()
    enemy_sprites = pygame.sprite.Group()
    bord_sprites = pygame.sprite.Group()

    tanka = tank()
    tanka.rect.x = 100
    tanka.rect.y = 200
    all_sprites.add(tanka)
    tank_sprites.add(tanka)

    enemygen(startenemyem)

    borderwidth = 10
    borderheight = HEIGHT - blockwidth

    leftbord = block(x=0, y=blockwidth * 3, width=borderwidth, \
                     height=borderheight, color=RED)
    leftbord.type = 'border'
    all_sprites.add(leftbord)
    bord_sprites.add(leftbord)

    rightbord = block(x=WIDTH - borderwidth, y=blockwidth * 3, \
                      width=borderwidth, \
                      height=borderheight, color=RED)
    rightbord.type = 'border'
    all_sprites.add(rightbord)
    bord_sprites.add(rightbord)

    topbord = block(x=0, y=blockwidth * 3 - borderwidth, width=WIDTH, \
                    height=borderwidth, color=RED)
    topbord.type = 'border'
    all_sprites.add(topbord)
    bord_sprites.add(topbord)

    bottbord = block(x=0, y=HEIGHT - borderwidth, width=WIDTH, \
                     height=borderwidth, color=RED)
    bottbord.type = 'border'
    all_sprites.add(bottbord)
    bord_sprites.add(bottbord)

    blockgen(startblockem)

    keypressedup = False
    keypresseddown = False
    keypressedleft = False
    keypressedright = False
    pressedkeys = 0

    starttime = time.time()

    aliveflag = 1
    score = 0
    running = True
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 'exit'
            if aliveflag == 1:
                if event.type == pygame.KEYDOWN:
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
            else:
                if event.type == pygame.KEYDOWN or \
                        event.type == pygame.MOUSEBUTTONDOWN:
                    return 'defeat'

        for i in all_sprites:
            if i.type == 'tank':
                if keypresseddown or keypressedup or keypressedleft \
                        or keypressedright:
                    i.update()
                    for j in all_sprites:
                        if j.type == 'block' or j.type == 'enemy' \
                                or j.type == 'border':
                            if j.rect.colliderect(i.rect):
                                i.rect.x = i.oldx
                                i.rect.y = i.oldy
                                break

            if i.type == 'bullet':
                i.update()
                if i.rect.x > screen.get_width() or \
                        i.rect.x + i.rect.width < 0 or \
                        i.rect.y > screen.get_height() or \
                        i.rect.y + i.rect.height < 0:
                    all_sprites.remove(i)
                    bullet_sprites.remove(i)
                else:
                    for j in all_sprites:
                        if j.type == 'block' or j.type == 'enemy' \
                                or j.type == 'tank':
                            if j.rect.colliderect(i.rect):
                                all_sprites.remove(i)
                                bullet_sprites.remove(i)
                                j.health -= i.damage
                                break

            if i.type == 'enemy':
                i.update()
                for j in all_sprites:
                    if j.type == 'tank' or j.type == 'block' or \
                            j.type == 'border' or j.type == 'enemy':
                        if j.rect.colliderect(i.rect) and i is not j:
                            i.rect.x = i.oldx
                            i.rect.y = i.oldy
                            break
                bul = i.shoot()
                if bul is not None:
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
            aliveflag = 0

        blockgentick += 1
        if blockgentick >= blockgencooldown:
            blockgen(blockgennum)
            blockgennum += blockgenincr
            blockgentick = 0
            for i in tank_sprites:
                i.health += 1

        enemygentick += 1
        if enemygentick >= enemygencooldown:
            enemygen(enemygennum)
            enemygennum += enemygenincr
            enemygentick = 0

        screen.fill(BLACK)
        all_sprites.draw(screen)
        if aliveflag == 1:
            for i in tank_sprites:
                score = ((time.time() - starttime) * 10 // 1 / 10)
                drawstats(obj=i, time=score)
        else:
            textstr = 'SCORE IS ' + str(score)
            st = pygame.font.SysFont('impact', bigtextsize)
            text = st.render(textstr, True, GREEN)
            text_rect = text.get_rect()
            text_rect.center = (WIDTH // 2, HEIGHT // 2)
            screen.blit(text, text_rect)
            textstr = 'Press any button'
            st = pygame.font.SysFont('impact', bigtextsize)
            text = st.render(textstr, True, GREEN)
            text_rect = text.get_rect()
            text_rect.center = (WIDTH // 2, HEIGHT // 2 + bigtextsize * 2)
            screen.blit(text, text_rect)

        pygame.display.flip()


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
            i.update(text1=i.type, text2=i.type)
            i.show(screen=screen)
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

