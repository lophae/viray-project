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

teleporter_group = pygame.sprite.Group()

map_group = pygame.sprite.Group()
mapP_group = pygame.sprite.Group()

chest_group = pygame.sprite.Group()

p = MiniPlayer(BLUE, 1470, 105)
mapP_group.add(p)

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
    global enemyCount
    enemyCount = random.randint(1,3)
    for foo in range(enemyCount):
        e = Enemy1(PURPLE)
        all_sprites_list.add(e)
        enemy_group1.add(e)

def bossSpawn():
    global enemyCount
    enemyCount = 1
    b = Boss1(PURPLE, player.rect.centery, player.rect.centerx)
    all_sprites_list.add(b)
    boss_group1.add(b)
    doorClose()

def deleteWall():
    global mapGrid

    for foo in wall_group:
        foo.delete()
    for foo in teleporter_group:
        foo.delete()
    for foo in door_group:
        foo.delete()
    for foo in doorclose_group:
        foo.delete()
    for foo in wall_groupDown:
        foo.delete()
    for foo in wall_groupLeft:
        foo.delete()
    for foo in wall_groupUp:
        foo.delete()
    for foo in wall_groupRight:
        foo.delete()
    for foo in map_group:
        foo.delete()
    for foo in chest_group:
        foo.delete()
    
    mapGrid = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

def teleport():
    global mapx, mapy, level1rooms

    level1rooms += 2
    player.rect.x = 620
    player.rect.y = 340
    p.rect.x = 1470
    p.rect.y = 105
    #player.health = 200

    mapx = 13
    mapy = 13

    deleteWall()
    spawnRoom(), mapCreate(), mapDoors(), miniMap(0)


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

def spriteLocate(direction):
    if direction == 1:
        for foo in wall_group:
            foo.rect.x = foo.rect.x - 1280
        for foo in teleporter_group:
            foo.rect.x = foo.rect.x - 1280
        for foo in chest_group:
            foo.rect.x = foo.rect.x - 1280
        for foo in bullet_group:
            foo.delete()

    if direction == 2:
        for foo in wall_group:
            foo.rect.x = foo.rect.x + 1280
        for foo in teleporter_group:
            foo.rect.x = foo.rect.x + 1280
        for foo in chest_group:
            foo.rect.x = foo.rect.x + 1280
        for foo in bullet_group:
            foo.delete()

    if direction == 3:
        for foo in wall_group:
            foo.rect.y = foo.rect.y + 720
        for foo in teleporter_group:
            foo.rect.y = foo.rect.y + 720
        for foo in chest_group:
            foo.rect.y = foo.rect.y + 720
        for foo in bullet_group:
            foo.delete()

    if direction == 4:
        for foo in wall_group:
            foo.rect.y = foo.rect.y - 720
        for foo in teleporter_group:
            foo.rect.y = foo.rect.y - 720
        for foo in chest_group:
            foo.rect.y = foo.rect.y - 720
        for foo in bullet_group:
            foo.delete()

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

def bossAttack1():
    bossWall = pygame.sprite.groupcollide(boss_group1, wall_group, False, False)
    bossWall2 = pygame.sprite.groupcollide(boss_group1, doorclose_group, False, False)
    for foo in boss_group1:
        foo.attack()
        for x in bossWall:
            foo.stop(player.rect.y, player.rect.x)
        for y in bossWall2:
            foo.stop(player.rect.y, player.rect.x)
    
def miniMap(direction):
    global minimapx, minimapy

    if direction == 0:
        minimapx = 1460
        minimapy = 100
        m = MiniMap(WHITE, 1460, 100)
        map_group.add(m)

    if direction == 1:
        minimapx += 40
        m = MiniMap(WHITE, minimapx, minimapy)
        map_group.add(m)
        p.rect.x += 40

    if direction == 2:
        minimapx -= 40
        m = MiniMap(WHITE, minimapx, minimapy)
        map_group.add(m)
        p.rect.x -= 40

    if direction == 3:
        minimapy -= 30
        m = MiniMap(WHITE, minimapx, minimapy)
        map_group.add(m)
        p.rect.y -= 30

    if direction == 4:
        minimapy += 30
        m = MiniMap(WHITE, minimapx, minimapy)
        map_group.add(m)
        p.rect.y += 30

def createChest():
    global chestA
    chance = random.randint(1,1)
    if chance == 1:
        c = Chest(BROWN)
        all_sprites_list.add(c)
        chest_group.add(c)
    chestA = False

def abilities(): # from room chests
    global coins
    randomAbility = random.randint(1,8)
    coins = coins - 5
    if randomAbility == 1: # +1 to max health
        player.healthMax += 1
    if randomAbility == 2 or randomAbility == 3 or randomAbility == 4:
        if player.health < player.healthMax:
            player.health += 1 # +1 to current health, but if health is max, does nothing
        else:
            abilities() # re-roll the number to get a different item
    if randomAbility == 5 or randomAbility == 6:
        player.ammoMax += 1 # +1 to max ammo
    if randomAbility == 7 or randomAbility == 8:
        player.staminaMax += 50 # increase to stamina
    
    if coins < 0: # bug fix
        coins = 0

def abilitiesBoss(): # from boss drops
    randomItem = random.randint(1,1)

    if randomItem == 1:
        player.teleport = True
        player.teleportCountMax += 1
        player.teleportCount += 1
        

# -------- Main Program Loop -----------
def game():
    global done, stamina, mapx, mapy, level1rooms, level2rooms, clocktick, player_x, player_y, enemyCount, bossCount, mapGrid, coins, chestA
    global collision_immune, collision_time, collision_det
    global reloading, reloadT, reload_det
    mapGrid = mapGridReset
    running = True
    spawnRoom(), mapCreate(), mapDoors(), miniMap(0)

    while not done:
        # --- Main event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_l: running = False
                if event.key == pygame.K_m: running = True
                if event.key == pygame.K_p: quit()

            if running == True and reloading == False:
                # -- PLAYER SHOOT
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1: # left click
                        player.ammo -= 1
                        x, y = pygame.mouse.get_pos()
                        b = Bullet(WHITE, player.rect.centerx, player.rect.centery, 10, 10, 4, x, y)
                        all_sprites_list.add(b)
                        bullet_group.add(b)
            
            # EXTRA ABILITY (teleport)
            if player.teleport == True:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 3 and player.teleportCount > 0: # right click
                        x, y = pygame.mouse.get_pos()
                        if (x < 1280): # or (player.rect.x != oldx and player.rect.y != oldy): 
                            player.teleportCount -= 1
                            oldx = player.rect.x
                            oldy = player.rect.y
                            player.rect.x = x
                            player.rect.y = y
                            if (player.rect.x == oldx and player.rect.y == oldy and player.teleportCount < (player.teleportCountMax + 1)):
                                player.teleportCount += 1
                            

        if running == True:
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
            
            # -- STAMINA
            if keys[pygame.K_a] and keys[pygame.K_LSHIFT] and player.stamina > 1: 
                player.move(-2,0)
                player.stamina = player.stamina - 2
            if keys[pygame.K_d] and keys[pygame.K_LSHIFT] and player.stamina > 1:
                player.move(2,0)
                player.stamina = player.stamina - 2
            if keys[pygame.K_w] and keys[pygame.K_LSHIFT] and player.stamina > 1:
                player.move(0,-2)
                player.stamina = player.stamina - 2
            if keys[pygame.K_s] and keys[pygame.K_LSHIFT] and player.stamina > 1:
                player.move(0,2)
                player.stamina = player.stamina - 2
            if not keys[pygame.K_LSHIFT] or (keys[pygame.K_LSHIFT] and (not keys[pygame.K_a] and not keys[pygame.K_d] and not keys[pygame.K_w] and not keys[pygame.K_s])):
                if player.stamina != player.staminaMax:
                    player.stamina = player.stamina + 1

            # -- SHOOTING
            for b in bullet_group:
                b.move()

            # -- PLAYER RELOAD
            if reload_det == True:
                if (pygame.time.get_ticks() - reloadT) > 1500:
                    player.ammo = player.ammoMax
                    reloading = False
                    reload_det = False

            if player.ammo < 1 and reload_det == False:
                reloading = True
                reloadT = pygame.time.get_ticks()
                reload_det = True
            
            if player.ammo < player.ammoMax and player.ammo > 0:
                if keys[pygame.K_r]:
                    reloading = True
                    reloadT = pygame.time.get_ticks()
                    reload_det = True

            # -- EXTRA ITEMS

                    
            # --  BULLET WALL COLLISION 
            projectileCollision()
            
            # -- BULLET ENEMY COLLISION
            enemyBulletCollide = pygame.sprite.groupcollide(bullet_group, enemy_group1, True, True)
            for foo in enemyBulletCollide:
                enemyCount -= 1
                coins += 1

            # -- BULLET BOSS COLLISION
            bossBulletCollide = pygame.sprite.groupcollide(bullet_group, boss_group1, True, False)
            for foo in bossBulletCollide:
                for x in boss_group1:
                    x.health = x.health - 1

            # -- DOOR OPEN WHEN ENEMY COUNT == 0
            if enemyCount == 0:
                for all in doorclose_group:
                    all.delete()
                enemyCount = 1
                chestA = True

            # -- DOOR OPEN AND TELEPORTER WHEN BOSS DIES
            for all in boss_group1:
                if all.health == 0:
                    coins += 4
                    abilitiesBoss()

                    t = Teleporter()
                    all_sprites_list.add(t)
                    teleporter_group.add(t)
                    for all in doorclose_group:
                        all.delete()

            # -- PLAYER WALL COLLISION 
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

            # -- PLAYER ENEMY COLLISION
            if collision_immune == False:

                player_hitEb = pygame.sprite.spritecollide(player, enemybullet_group, True)
                for foo in player_hitEb:
                    collision_immune = True
                    collision_det = True
                    player.health -= 1
                
                player_hitB = pygame.sprite.spritecollide(player, boss_group1, False)
                for foo in player_hitB:
                    collision_immune = True
                    collision_det = True
                    player.health -= 1

                player_hitE = pygame.sprite.spritecollide(player, enemy_group1, True)
                for foo in player_hitE:
                    collision_immune = True
                    collision_det = True
                    player.health -= 1
                    enemyCount -= 1
            
            if (pygame.time.get_ticks() - collision_time) > 1500:
                collision_immune = False
                player.image.fill(WHITE)
            
            if collision_det == True:
                collision_time = pygame.time.get_ticks()
                player.image.fill(RED)
                collision_immune = True
                collision_det = False

            # -- PLAYER DOOR COLLISION
            # 1 = unvisited, 2 = boss, 3 = visited
            # Right
            player_doorRight = pygame.sprite.spritecollide(player, wall_groupRight, False)
            for foo in player_doorRight:
                player.rect.x = player.rect.x - 1180
                miniMap(1)
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
                spriteLocate(1)

            # Left
            player_doorLeft = pygame.sprite.spritecollide(player, wall_groupLeft, False)
            for foo in player_doorLeft:
                player.rect.x = player.rect.x + 1180
                miniMap(2)
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
                spriteLocate(2)

            # Up
            player_doorUp = pygame.sprite.spritecollide(player, wall_groupUp, False)
            for foo in player_doorUp:
                player.rect.y = player.rect.y + 620
                miniMap(3) 
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
                spriteLocate(3)

            # Down
            player_doorDown = pygame.sprite.spritecollide(player, wall_groupDown, False)
            for foo in player_doorDown:
                player.rect.y = player.rect.y - 620
                miniMap(4)
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
                spriteLocate(4)           

            # -- PLAYER TELEPORTER COLLISION
            playerTeleport = pygame.sprite.spritecollide(player, teleporter_group, False)
            for foo in playerTeleport:
                print("teleport")
                teleport()
                print(mapGrid)

            # -- ENEMY attack
            enemyShoot()
            bossAttack1()

            # -- #
            screen.fill(BLACK)
            font = pygame.font.Font(None, 25)
            font2 = pygame.font.Font(None, 60)
            fonttest = pygame.font.Font(None, 100)
            fonttest2 = pygame.font.Font(None, 40)
            
            all_sprites_list.update()
            enemybullet_group.update()

            all_sprites_list.draw(screen)
            pygame.draw.rect(screen, BLACK, (1280,0,384,720))
            map_group.draw(screen)
            mapP_group.draw(screen)

            txthealth = font.render("Health: " + str(player.health) + " / " + str(player.healthMax), True, WHITE)
            screen.blit(txthealth,(1286, 260))
            txtsta = font.render("Stamina: " + str(player.stamina) + " / " + str(player.staminaMax), True, WHITE)
            screen.blit(txtsta, (1286, 280))
            txtamm = font.render("Ammo: " + str(player.ammo) + " / " + str(player.ammoMax), True, WHITE)
            screen.blit(txtamm, (1286, 300))
            txtmon = font.render("Coins: " + str(coins) + "                      (5 coins to open a chest)", True, WHITE)
            screen.blit(txtmon, (1286, 320))
            txtsc = font.render("Score: ", True, WHITE)
            screen.blit(txtsc, (1286, 340))

            txtrel = font.render("press [r] to reload", True, WHITE)
            screen.blit(txtrel, (1284, 660))
            txtq = font.render("press [p] to quit", True, WHITE)
            screen.blit(txtq, (1284, 700))
            txtp = font.render("press [l] to pause", True, WHITE)
            screen.blit(txtp, (1284, 680))

            # -- ITEM SIMPLE DISPLAY
            txtItems = fonttest2.render("Items", True, WHITE)
            screen.blit(txtItems, (1435, 380))
            txtTeleport = font.render("teleport [rightclick]: " + str(player.teleportCount) + " / " + str(player.teleportCountMax), True, WHITE)
            if player.teleport == True:
                screen.blit(txtTeleport, (1286, 410))

            txtdeath = font2.render("YOU DIED", True, RED)

            # -- PLAYER DEATH
            if player.health < 1:
                player.delete()
                player.health = 0
                running = False
            
            # -- PLAYER CHEST / ITEM
            if chestA == True:
                createChest()

            # -- ITEMS AND ABILITIES FROM CHESTS
            if coins > 4:
                chest_buy = pygame.sprite.spritecollide(player, chest_group, True)
                for foo in chest_buy:
                    abilities()

        elif running == False:
            if player.health < 1:       
                screen.blit(txtdeath, (540, 360))
            else:
                font = pygame.font.Font(None, 50)
                pausetext = font.render("PAUSED", True, WHITE)
                txtu = font.render("press [m] to un-pause", True, WHITE)
                screen.fill(BLACK)
                screen.blit(pausetext, (10, 10))
                screen.blit(txtu, (10, 50))
    
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