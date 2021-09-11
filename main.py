import pygame, math, random, sys
from pygame.locals import *

# Import Other Files
from classes import *
from levels import *
from settings import *
from variables import *
pygame.init()

pygame.time.set_timer(pygame.USEREVENT, enemyFirerate)

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# -- sprite lists
all_sprites_list = pygame.sprite.Group()

player = Player(WHITE)
all_sprites_list.add(player)

bullet_group = pygame.sprite.Group()
enemybullet_group = pygame.sprite.Group()

enemy_group1 = pygame.sprite.Group()
boss_group1 = pygame.sprite.Group()


wall_groupRight = pygame.sprite.Group()
wall_groupLeft = pygame.sprite.Group()
wall_groupUp = pygame.sprite.Group()
wall_groupDown = pygame.sprite.Group()

# -- SPAWN ROOM CREATION
def spawnRoom():
    x = 0
    y = 0
    for row in blankMap:
        for col in row:
            if col == 1:
                w = Wall(RED, 40, 40, x, y)
                all_sprites_list.add(w)
                wall_group.add(w)
            x = x + 40
        x = 0
        y = y + 40  

    # right
    w = Wall(YELLOW, 10, 240, 1270, 240)
    all_sprites_list.add(w)
    wall_groupRight.add(w)

    # left
    w = Wall(YELLOW, 10, 240, 0, 240)
    all_sprites_list.add(w)
    wall_groupLeft.add(w)

    # up
    w = Wall(YELLOW, 240, 10, 520, 0)
    all_sprites_list.add(w)
    wall_groupUp.add(w)

    # down
    w = Wall(YELLOW, 240, 10, 520, 710)
    all_sprites_list.add(w)
    wall_groupDown.add(w)

# -- MAP GENERATION
def mapCreate():
    x = 0
    y = 0
    z = 0
    global originalx
    global originaly
    originalx = 13
    originaly = 13
    
    while z != level1rooms:
        randomNum = random.randint(1, 4)
        randomRoom = random.randint(0, 2)

        # no overlapping
        if mapGrid[originalx][originaly + 1] == 1 and mapGrid[originalx][originaly - 1] == 1 and mapGrid[originalx - 1][originaly] == 1 and mapGrid[originalx + 1][originaly] == 1:
            z = level1rooms
        
        if randomNum == 1:
            if mapGrid[originalx][originaly + 1] == 0:
                randomNum = 1
            else:
                randomNum = random.choice([2, 3, 4])
                if randomNum == 2:
                    if mapGrid[originalx][originaly - 1] == 0:
                        randomNum = 2
                if randomNum == 3:
                    if mapGrid[originalx - 1][originaly] == 0:
                        randomNum = 3
                if randomNum == 4:
                    if mapGrid[originalx + 1][originaly] == 0:
                        randomNum = 4
        
        if randomNum == 2:
            if mapGrid[originalx][originaly - 1] == 0:
                randomNum = 2
            else:
                randomNum = random.choice([1, 3, 4])
                if randomNum == 1:
                    if mapGrid[originalx][originaly + 1] == 0:
                        randomNum = 1
                    else:
                        randomNum = random.choice([3, 4])
                if randomNum == 3:
                    if mapGrid[originalx - 1][originaly] == 0:
                        randomNum = 3
                if randomNum == 4:
                    if mapGrid[originalx + 1][originaly] == 0:
                        randomNum = 4
        
        if randomNum == 3:
            if mapGrid[originalx - 1][originaly] == 0:
                randomNum = 3
            else:
                randomNum = random.choice([1, 2, 4])
                if randomNum == 1:
                    if mapGrid[originalx][originaly + 1] == 0:
                        randomNum = 1
                    else:
                        randomNum = random.choice([2, 4])
                if randomNum == 2:
                    if mapGrid[originalx][originaly - 1] == 0:
                        randomNum = 2
                    else:
                        randomNum = random.choice([1, 4])
                        if randomNum == 1:
                            if mapGrid[originalx][originaly + 1] != 0:
                                randomNum = 4
                if randomNum == 4:
                    if mapGrid[originalx + 1][originaly] == 0:
                        randomNum = 4

        if randomNum == 4:
            if mapGrid[originalx + 1][originaly] == 0:
                randomNum = 4
            else:
                randomNum = random.choice([1, 2, 3])
                if randomNum == 1:
                    if mapGrid[originalx][originaly + 1] == 0:
                        randomNum = 1
                    else:
                        randomNum = random.choice([2, 3])
                        if randomNum == 2:
                            if mapGrid[originalx][originaly - 1] != 0:
                                randomNum = 3
                if randomNum == 2:
                    if mapGrid[originalx][originaly - 1] == 0:
                        randomNum = 2
                    else:
                        randomNum = random.choice([1, 3])
                        if randomNum == 1:
                            if mapGrid[originalx][originaly + 1] != 0:
                                randomNum = 3
                if randomNum == 3:
                    if mapGrid[originalx - 1][originaly] == 0:
                        randomNum = 3
                    else:
                        randomNum = random.choice([1, 2])
                        if randomNum == 1:
                            if mapGrid[originalx][originaly + 1] != 0:
                                randomNum = 2 
                        if randomNum == 2:
                            if mapGrid[originalx][originaly - 1] != 0:  
                                randomNum = 1  

        # right
        if randomNum == 1:
            x = x + 1280
            originaly += 1
            mapGrid[originalx][originaly] = 1
            if z == level1rooms - 1:
                randomRoom = 3
                mapGrid[originalx][originaly] = 2
            for row in myRooms[randomRoom]:
                for col in row:
                    if col == 1:
                        w = Wall(BLUE, 40, 40, x, y)
                        all_sprites_list.add(w)
                        wall_group.add(w)
                    x = x + 40
                if z == 0:
                    x = 0
                else:
                    x = x - 2560
                x = x + 1280
                y = y + 40
        # left
        if randomNum == 2:
            x = x - 1280
            originaly -= 1
            mapGrid[originalx][originaly] = 1
            if z == level1rooms - 1:
                randomRoom = 3
                mapGrid[originalx][originaly] = 2
            for row in myRooms[randomRoom]:
                for col in row:
                    if col == 1:
                        w = Wall(YELLOW, 40, 40, x, y) 
                        all_sprites_list.add(w)
                        wall_group.add(w)
                    x = x + 40
                if z == 0:
                    x = 0
                else:
                    pass
                x = x - 1280
                y = y + 40
        # up
        if randomNum == 3:
            y = y - 720
            originalx -= 1
            mapGrid[originalx][originaly] = 1
            if z == level1rooms - 1:
                randomRoom = 3
                mapGrid[originalx][originaly] = 2
            for row in myRooms[randomRoom]:
                for col in row:
                    if col == 1:
                        w = Wall(GREEN, 40, 40, x, y)
                        all_sprites_list.add(w)
                        wall_group.add(w)
                    x = x + 40
                if z == 0:
                    x = 0
                else:
                    x = x - 1280
                y = y + 40
        # down
        if randomNum == 4:
            y = y + 720
            originalx += 1
            mapGrid[originalx][originaly] = 1
            if z == level1rooms - 1:
                randomRoom = 3
                mapGrid[originalx][originaly] = 2
            for row in myRooms[randomRoom]:
                for col in row:
                    if col == 1:
                        w = Wall(WHITE, 40, 40, x, y)
                        all_sprites_list.add(w)
                        wall_group.add(w)
                    x = x + 40
                if z == 0:
                    x = 0
                else:
                    x = x - 1280
                y = y + 40

        if randomNum == 1:
            y = y - 720
        if randomNum == 2:
            y = y - 720
        if randomNum == 3:
            y = y - 720           
        if randomNum == 4:
            y = y - 720
                 
        z += 1

def mapDoors():
    x = 0
    y = 0
    if mapGrid[mapx][mapy + 1] == 0:
        for row in door:
            for col in row:
                if col == 1:
                    w = Wall(RED, 40, 40, x, y)
                    all_sprites_list.add(w)
                    door_group.add(w)
                x = x + 40
            x = 0
            y = y + 40
    x = 0
    y = 0
    if mapGrid[mapx][mapy - 1] == 0:
        for row in door:
            for col in row:
                if col == 2:
                    w = Wall(RED, 40, 40, x, y)
                    all_sprites_list.add(w)
                    door_group.add(w)
                x = x + 40
            x = 0
            y = y + 40
    x = 0
    y = 0
    if mapGrid[mapx - 1][mapy] == 0:
        for row in door:
            for col in row:
                if col == 3:
                    w = Wall(RED, 40, 40, x, y)
                    all_sprites_list.add(w)
                    door_group.add(w)
                x = x + 40
            x = 0
            y = y + 40
    x = 0
    y = 0
    if mapGrid[mapx + 1][mapy] == 0:
        for row in door:
            for col in row:
                if col == 4:
                    w = Wall(RED, 40, 40, x, y)
                    all_sprites_list.add(w)
                    door_group.add(w)
                x = x + 40
            x = 0
            y = y + 40

def inventory():
    pass

def enemySpawn():
    e = Enemy1(PURPLE, 50, 50, player.rect.x, player.rect.y)
    all_sprites_list.add(e)
    enemy_group1.add(e)

def bossSpawn():
    b = Boss1(PURPLE)
    all_sprites_list.add(b)
    boss_group1.add(b)
    doorClose()


def projectileCollision():
    bulletWall = pygame.sprite.groupcollide(bullet_group, wall_group, True, False)
    bulletWall = pygame.sprite.groupcollide(bullet_group, door_group, True, False)
    bulletWall = pygame.sprite.groupcollide(bullet_group, wall_groupDown, True, False)
    bulletWall = pygame.sprite.groupcollide(bullet_group, wall_groupLeft, True, False)
    bulletWall = pygame.sprite.groupcollide(bullet_group, wall_groupRight, True, False)
    bulletWall = pygame.sprite.groupcollide(bullet_group, wall_groupUp, True, False)
    bulletWall = pygame.sprite.groupcollide(bullet_group, doorclose_group, True, False)
    enemybulletWall = pygame.sprite.groupcollide(enemybullet_group, wall_group, True, False)
    enemybulletWall = pygame.sprite.groupcollide(enemybullet_group, door_group, True, False)
    enemybulletWall = pygame.sprite.groupcollide(enemybullet_group, wall_groupDown, True, False)
    enemybulletWall = pygame.sprite.groupcollide(enemybullet_group, wall_groupLeft, True, False)
    enemybulletWall = pygame.sprite.groupcollide(enemybullet_group, wall_groupRight, True, False)
    enemybulletWall = pygame.sprite.groupcollide(enemybullet_group, wall_groupUp, True, False)
    enemybulletWall = pygame.sprite.groupcollide(enemybullet_group, doorclose_group, True, False)
    
def doorClose():
    global enemyCount
    enemyCount = 1

    # right
    w = Wall(RED, 10, 240, 1240, 240)
    all_sprites_list.add(w)
    doorclose_group.add(w)

    # left
    w = Wall(RED, 10, 240, 30, 240)
    all_sprites_list.add(w)
    doorclose_group.add(w)

    # up
    w = Wall(RED, 240, 10, 520, 30)
    all_sprites_list.add(w)
    doorclose_group.add(w)

    # down
    w = Wall(RED, 240, 10, 520, 680)
    all_sprites_list.add(w)
    doorclose_group.add(w)

pygame.time.set_timer(pygame.USEREVENT, 150)
def enemyShoot():
    for event in pygame.event.get():
        if event.type == pygame.USEREVENT:
            for foo in enemy_group1:
                x = foo.rect.centerx
                y = foo.rect.centery
                eb = enemyBullet(x, y, player.rect.centerx, player.rect.centery)
                enemybullet_group.add(eb)
                all_sprites_list.add(eb)

# -------- Main Program Loop -----------
def game():
    global done, stamina, mapx, mapy, level1rooms, level2rooms, clocktick, player_x, player_y, enemyCount, mapGrid, pausetext
    mapGrid = mapGridReset
    running = True
    spawnRoom(), mapCreate(), mapDoors()
    #print(mapGrid)
    while not done:
        # --- Main event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_l: running = False
                if event.key == pygame.K_m: running = True

            if running == True:

                # -- PLAYER SHOOT
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if event.button == 1:
                            x, y = pygame.mouse.get_pos()
                            b = Bullet(WHITE, player.rect.centerx, player.rect.centery, 10, 10, 4, x, y)
                            all_sprites_list.add(b)
                            bullet_group.add(b)

                # -- MOVEMENT
                keys = pygame.key.get_pressed()
                if keys[pygame.K_a]:
                    player.move(-1,0)
                if keys[pygame.K_d]:
                    player.move(1,0)
                if keys[pygame.K_w]:
                    player.move(0,-1)
                if keys[pygame.K_s]:
                    player.move(0,1)

                # -- INVENTORY
                if keys[pygame.K_t]:
                    inventory()
                
                # -- MENU
                if keys[pygame.K_p]:
                    quit()

                # -- STAMINA
                if keys[pygame.K_a] and keys[pygame.K_LSHIFT] and stamina > 1: 
                    player.move(-2,0)
                    stamina = stamina - 2
                if keys[pygame.K_d] and keys[pygame.K_LSHIFT] and stamina > 1:
                    player.move(2,0)
                    stamina = stamina - 2
                if keys[pygame.K_w] and keys[pygame.K_LSHIFT] and stamina > 1:
                    player.move(0,-2)
                    stamina = stamina - 2
                if keys[pygame.K_s] and keys[pygame.K_LSHIFT] and stamina > 1:
                    player.move(0,2)
                    stamina = stamina - 2
                if not keys[pygame.K_LSHIFT] or (keys[pygame.K_LSHIFT] and (not keys[pygame.K_a] and not keys[pygame.K_d] and not keys[pygame.K_w] and not keys[pygame.K_s])):
                    if stamina != 300:
                        stamina = stamina + 1

                # -- SHOOTING
                for b in bullet_group:
                    b.move()

                # --  BULLET WALL COLLISION 
                projectileCollision()
                
                # -- BULLET ENEMY COLLISION
                enemyBulletCollide = pygame.sprite.groupcollide(bullet_group, enemy_group1, True, True)
                for foo in enemyBulletCollide:
                    enemyCount -= 1

                # -- DOOR OPEN WHEN ENEMY COUNT == 0
                if enemyCount == 0:
                    for all in doorclose_group:
                        all.delete()

                # -- PLAYER WALL COLLISION (requires improvement)
                player_hit = pygame.sprite.spritecollide(player, wall_group, False)
                for foo in player_hit:
                    #player.move(0, 0)
                    player.rect.x = player_old_x
                    player.rect.y = player_old_y
                    
                player_hitDoor = pygame.sprite.spritecollide(player, door_group, False)
                for foo in player_hitDoor:
                    #player.move(0, 0)
                    player.rect.x = player_old_x
                    player.rect.y = player_old_y
                
                player_closeDoor = pygame.sprite.spritecollide(player, doorclose_group, False)
                for foo in player_closeDoor:
                    player.rect.x = player_old_x
                    player.rect.y = player_old_y

                player_old_x = player.rect.x
                player_old_y = player.rect.y

                # -- PLAYER DOOR COLLISION
                # 1 = unvisited, 2 = boss, 3 = visited
                # Right
                player_doorRight = pygame.sprite.spritecollide(player, wall_groupRight, False)
                for foo in player_doorRight:
                    player.rect.x = player.rect.x - 1180
                    for foo in door_group:
                        foo.delete()
                    mapGrid[mapx][mapy] = 3
                    mapy = mapy + 1
                    mapDoors()
                    if mapGrid[mapx][mapy] != 3 and mapGrid[mapx][mapy] != 2:
                        doorClose()
                        for foo in enemy_group1:
                            foo.delete()
                        enemySpawn()
                    elif mapGrid[mapx][mapy] == 2:
                        bossSpawn()

                    for foo in wall_group:
                        foo.rect.x = foo.rect.x - 1280
                    for foo in bullet_group:
                        foo.delete()
                # Left
                player_doorLeft = pygame.sprite.spritecollide(player, wall_groupLeft, False)
                for foo in player_doorLeft:
                    player.rect.x = player.rect.x + 1180
                    for foo in door_group:
                        foo.delete()
                    mapGrid[mapx][mapy] = 3
                    mapy = mapy - 1
                    mapDoors()
                    if mapGrid[mapx][mapy] != 3 and mapGrid[mapx][mapy] != 2:
                        doorClose()
                        for foo in enemy_group1:
                            foo.delete()
                        enemySpawn()
                    elif mapGrid[mapx][mapy] == 2:
                        bossSpawn()

                    for foo in wall_group:
                        foo.rect.x = foo.rect.x + 1280
                    for foo in bullet_group:
                        foo.delete()
                # Up
                player_doorUp = pygame.sprite.spritecollide(player, wall_groupUp, False)
                for foo in player_doorUp:
                    player.rect.y = player.rect.y + 620
                    for foo in door_group:
                        foo.delete()
                    mapGrid[mapx][mapy] = 3
                    mapx = mapx - 1
                    mapDoors()
                    if mapGrid[mapx][mapy] != 3 and mapGrid[mapx][mapy] != 2:
                        doorClose()
                        for foo in enemy_group1:
                            foo.delete()
                        enemySpawn() 
                    elif mapGrid[mapx][mapy] == 2:
                        bossSpawn()

                    for foo in wall_group:
                        foo.rect.y = foo.rect.y + 720
                    for foo in bullet_group:
                        foo.delete()
                # Down
                player_doorDown = pygame.sprite.spritecollide(player, wall_groupDown, False)
                for foo in player_doorDown:
                    player.rect.y = player.rect.y - 620
                    for foo in door_group:
                        foo.delete()               
                    mapGrid[mapx][mapy] = 3
                    mapx = mapx + 1
                    mapDoors()
                    if mapGrid[mapx][mapy] != 3 and mapGrid[mapx][mapy] != 2:
                        doorClose()
                        for foo in enemy_group1:
                            foo.delete()
                        enemySpawn()    
                    elif mapGrid[mapx][mapy] == 2:
                        bossSpawn()           

                    for foo in wall_group:
                        foo.rect.y = foo.rect.y - 720
                    for foo in bullet_group:
                        foo.delete()

                # -- ENEMY 1 SHOOTING
                enemyShoot()
                
                # -- #
                screen.fill(BLACK)
                font = pygame.font.Font(None, 25)
                
                all_sprites_list.update()
                enemybullet_group.update()

                all_sprites_list.draw(screen)
                pygame.draw.rect(screen, BLACK, (1280,0,384,720))
                
                txt = font.render("stamina count: " + str(stamina), True, BLACK)
                screen.blit(txt, (10, 10))
                txt2 = font.render("press [c] for inventory", True, BLACK)
                #screen.blit(txt2, (10, 690))
                txt3 = font.render("press [p] to quit", True, WHITE)
                screen.blit(txt3, (1284, 700))

            elif running == False:
                font = pygame.font.Font(None, 25)
                pausetext = font.render("PAUSED", True, WHITE)
                screen.fill(BLACK)
                screen.blit(pausetext, (10, 10))

        pygame.display.flip()
        clock.tick(clocktick)

def mainMenu():
    menu = True
    screen.fill(BLACK)
    font = pygame.font.Font(None, 100)
    txt = font.render("[main menu]", True, WHITE)
    starttxt = font.render("[start]", True, BLACK)
    quittxt = font.render("[quit]", True, BLACK)
    buttonStart = pygame.Rect(100, 300, 400, 100)
    buttonQuit = pygame.Rect(100, 550, 400, 100)

    while menu is True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                menu = False
            
            if event.type == pygame.MOUSEMOTION:
                mouse_pos = event.pos
                if buttonStart.collidepoint(mouse_pos):
                    starttxt = font.render("[start]", True, RED)
                else:
                    starttxt = font.render("[start]", True, BLACK)

                if buttonQuit.collidepoint(mouse_pos):
                    quittxt = font.render("[quit]", True, RED)
                else:
                    quittxt = font.render("[quit]", True, BLACK)

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                if buttonStart.collidepoint(mouse_pos):
                    game()
                elif buttonQuit.collidepoint(mouse_pos):
                    menu = False
        
        pygame.draw.rect(screen, [255, 255, 255], buttonStart)
        pygame.draw.rect(screen, [255, 255, 255], buttonQuit)
        screen.blit(starttxt, (100, 310))
        screen.blit(quittxt, (100, 560))
        screen.blit(txt, (100, 100))
        pygame.display.flip()
        clock.tick(240)

mainMenu()

pygame.quit()
quit()