import pygame
import src.Globals
from src.tank import tank
from src.block import block
from src.enemy import enemy
from src.button import button
import time
from random import randint

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((src.Globals.WIDTH, src.Globals.HEIGHT))
pygame.display.set_caption("tanks")
clock = pygame.time.Clock()


def drawstats(obj, color=src.Globals.DEFAULINTERCOL, \
              x=src.Globals.DEFAULINTERX, y=src.Globals.DEFAULINTERY, size=src.Globals.SMALLTEXTSIZE, \
              screen=screen, time=0, space=src.Globals.INTERSPACE):
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
    text_rect2.center = (x + text_rect.width + space, y)
    screen.blit(text2, text_rect2)


def blockgen(n, all_sprites, block_sprites):
    for _ in range(n):
        while True:
            x = randint(1, screen.get_width() // src.Globals.BLWIDTH - 1) * src.Globals.BLWIDTH
            y = randint(3, screen.get_height() // src.Globals.BLWIDTH - 1) * src.Globals.BLWIDTH
            check = pygame.Rect(x, y, src.Globals.BLWIDTH, src.Globals.BLWIDTH)
            k = 0
            for i in all_sprites:
                if check.colliderect(i.rect):
                    k = 1
            if k == 0:
                break
        a = block(x=x, y=y)
        all_sprites.add(a)
        block_sprites.add(a)


def enemygen(n, all_sprites, enemy_sprites):
    for _ in range(n):
        while True:
            x = randint(1, screen.get_width() // src.Globals.ENTWIDTH - 1) * src.Globals.ENTWIDTH
            y = randint(3, screen.get_height() // src.Globals.ENTWIDTH - 1) * src.Globals.ENTWIDTH
            check = pygame.Rect(x, y, src.Globals.ENTWIDTH, src.Globals.ENTWIDTH)
            k = 0
            for i in all_sprites:
                if check.colliderect(i.rect):
                    k = 1
            if k == 0:
                break
        a = enemy(x=x, y=y)
        all_sprites.add(a)
        enemy_sprites.add(a)


def herocreate(all_sprites, tank_sprites, x=src.Globals.HEROX, y=src.Globals.HEROY):
    tanka = tank()
    tanka.rect.x = x
    tanka.rect.y = y
    all_sprites.add(tanka)
    tank_sprites.add(tanka)
    return tanka


def bulgen(obj, all_sprites, bullet_sprites):
    k = obj.shoot()
    all_sprites.add(k)
    bullet_sprites.add(k)


def bordercreate(all_sprites, bord_sprites):
    leftbord = block(x=0, y=src.Globals.BLWIDTH * 3, width=src.Globals.BORDERWIDTH, \
                     height=src.Globals.BORDERHEIGHT, color=src.Globals.BORDCOL)
    leftbord.type = 'border'
    all_sprites.add(leftbord)
    bord_sprites.add(leftbord)

    rightbord = block(x=src.Globals.WIDTH - src.Globals.BORDERWIDTH, y=src.Globals.BLWIDTH * 3, \
                      width=src.Globals.BORDERWIDTH, \
                      height=src.Globals.BORDERHEIGHT, color=src.Globals.BORDCOL)
    rightbord.type = 'border'
    all_sprites.add(rightbord)
    bord_sprites.add(rightbord)

    topbord = block(x=0, y=src.Globals.BLWIDTH * 3 - src.Globals.BORDERWIDTH, width=src.Globals.WIDTH, \
                    height=src.Globals.BORDERWIDTH, color=src.Globals.BORDCOL)
    topbord.type = 'border'
    all_sprites.add(topbord)
    bord_sprites.add(topbord)

    bottbord = block(x=0, y=src.Globals.HEIGHT - src.Globals.BORDERWIDTH, width=src.Globals.WIDTH, \
                     height=src.Globals.BORDERWIDTH, color=src.Globals.RED)
    bottbord.type = 'border'
    all_sprites.add(bottbord)
    bord_sprites.add(bottbord)


def keypressedreact(r, l, u, d):
    if d:
        return 'down'
    elif u:
        return 'up'
    elif r:
        return 'right'
    elif l:
        return 'left'


def deathscreen(score, screen):
    textstr = 'YOUR SCORE IS ' + str(score)
    st = pygame.font.SysFont('impact', src.Globals.BIGTEXTSIZE)
    text = st.render(textstr, True, src.Globals.GREEN)
    text_rect = text.get_rect()
    text_rect.center = (src.Globals.ENDSCREENSCX, src.Globals.ENDSCREENSCY)
    screen.blit(text, text_rect)
    textstr = 'Press any button'
    st = pygame.font.SysFont('impact', src.Globals.BIGTEXTSIZE)
    text = st.render(textstr, True, src.Globals.GREEN)
    text_rect = text.get_rect()
    text_rect.center = (src.Globals.PRESSANYBUTX, src.Globals.PRESSANYBUTY)
    screen.blit(text, text_rect)


def game():
    blockgentick = 0
    blockgennum = 10
    enemygentick = 0
    enemygennum = src.Globals.STARTENEMYEM + 1
    enemygenincr = 1

    all_sprites = pygame.sprite.Group()
    tank_sprites = pygame.sprite.Group()
    bullet_sprites = pygame.sprite.Group()
    block_sprites = pygame.sprite.Group()
    enemy_sprites = pygame.sprite.Group()
    bord_sprites = pygame.sprite.Group()

    herocreate(all_sprites, tank_sprites)
    bordercreate(all_sprites, bord_sprites)
    enemygen(src.Globals.STARTENEMYEM, all_sprites, enemy_sprites)
    blockgen(src.Globals.STARTBLOCKEM, all_sprites, block_sprites)

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
        clock.tick(src.Globals.FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 'exit'
            if aliveflag == 1:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        for i in tank_sprites:
                            bulgen(i, all_sprites, bullet_sprites)
                    if event.key == pygame.K_LEFT:
                        keypressedleft = True
                        for i in tank_sprites:
                            i.direction = 'left'
                    elif event.key == pygame.K_RIGHT:
                        keypressedright = True
                        for i in tank_sprites:
                            i.direction = 'right'
                    elif event.key == pygame.K_DOWN:
                        keypresseddown = True
                        for i in tank_sprites:
                            i.direction = 'down'
                    elif event.key == pygame.K_UP:
                        keypressedup = True
                        for i in tank_sprites:
                            i.direction = 'up'
                    pressedkeys += 1
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
                        for i in tank_sprites:
                            i.direction = \
                                keypressedreact(r=keypressedright, \
                                                l=keypressedleft, \
                                                d=keypresseddown, \
                                                u=keypressedup)
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
                                or j.type == 'tank' or \
                                j.type == 'border':
                            if j.rect.colliderect(i.rect):
                                if j.type == 'border':
                                    j.health += i.damage
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
                if i.shootcooldown > i.shootfr:
                    bulgen(i, all_sprites, bullet_sprites)
                else:
                    i.shootcooldown += 1
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
        if blockgentick >= src.Globals.STARTBLOCKEM:
            blockgen(blockgennum, all_sprites, block_sprites)
            blockgennum += src.Globals.BLOCKGENINCR
            blockgentick = 0
            for i in tank_sprites:
                i.health += 1

        enemygentick += 1
        if enemygentick >= src.Globals.ENEMYGENCOOLDOWN:
            enemygen(enemygennum, all_sprites, enemy_sprites)
            enemygennum += enemygenincr
            enemygentick = 0

        screen.fill(src.Globals.BLACK)
        all_sprites.draw(screen)
        if aliveflag == 1:
            for i in tank_sprites:
                score = ((time.time() - starttime) * 10 // 1 / 10)
                drawstats(obj=i, time=score)
        else:
            deathscreen(score, screen)

        pygame.display.flip()


def mainmanu():
    buttons = []
    button1 = button(text='start', x=400, y=300, textsize=50, \
                     tcol=src.Globals.BLUE, bg=src.Globals.GREEN, type='start')
    button2 = button(text='exit', x=400, y=450, type='exit')
    buttons.append(button1)
    buttons.append(button2)
    running = True
    while running:
        clock.tick(src.Globals.FPS)
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

        screen.fill(src.Globals.BLACK)
        for i in buttons:
            i.update(text1=i.type, text2=i.type)
            i.show(screen=screen)
        pygame.display.update()


def activecycle():
    running = True
    while running:
        res = mainmanu()
        if res == 'start':
            res = game()
        if res == 'exit':
            running = False
            pygame.quit()

