import pygame, math, random
from pygame.locals import *

# Import Other Files
from classes import *
from levels import *
from settings import *
from variables import *
pygame.init()

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# -- sprite lists
all_sprites_list = pygame.sprite.Group()

player = Player(WHITE)
all_sprites_list.add(player)

bullet_group = pygame.sprite.Group()

wall_group = pygame.sprite.Group()
door_group = pygame.sprite.Group()
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
spawnRoom()

# -- MAP GENERATION
def mapCreate():
    x = 0
    y = 0
    z = 0
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
mapCreate()
for row in mapGrid:
    for col in row:
        if col == 1:
            pass
            #print("f")

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
    print(mapx, mapy)
mapDoors()

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        
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
    
    # -- temporary quit
    if keys[pygame.K_p]:
            done = True
    
    # -- STAMINA
    if keys[pygame.K_a] and keys[pygame.K_j] and stamina > 1: 
        player.move(-2,0)
        stamina = stamina - 2
    if keys[pygame.K_d] and keys[pygame.K_j] and stamina > 1:
        player.move(2,0)
        stamina = stamina - 2
    if keys[pygame.K_w] and keys[pygame.K_j] and stamina > 1:
        player.move(0,-2)
        stamina = stamina - 2
    if keys[pygame.K_s] and keys[pygame.K_j] and stamina > 1:
        player.move(0,2)
        stamina = stamina - 2
    if not keys[pygame.K_j]:
        if stamina != 150:
            stamina = stamina + 1

    # -- SHOOTING (requires fixing)
#    if event.type == pygame.MOUSEBUTTONDOWN: 
#        if event.button == 1 and click == False:
#            click = True
#    if click: 
#        x, y = pygame.mouse.get_pos()
#        b = Bullet(WHITE, player.rect.centerx, player.rect.centery, 10, 10, 5, x, y)
#        bullet_group.add(b)
#        all_sprites_list.add(b)
#        click = False

    # --  BULLET WALL COLLISION
#    bulletWall = pygame.sprite.groupcollide(bullet_group, wall_group, True, False)

    # -- PLAYER WALL COLLISION (requires improvement)
    player_hit = pygame.sprite.spritecollide(player, wall_group, False)
    for foo in player_hit:
        player.move(0, 0)
        player.rect.x = player_old_x
        player.rect.y = player_old_y
    player_old_x = player.rect.x
    player_old_y = player.rect.y
    
    # -- PLAYER DOOR COLLISION (BUGGED IN THE CORNERS)
    # Right
    player_doorRight = pygame.sprite.spritecollide(player, wall_groupRight, False)
    for foo in player_doorRight:
        player.rect.x = player.rect.x - 1220
        for foo in door_group:
            foo.delete()
        mapy = mapy + 1
        mapDoors()
        for foo in wall_group:
            foo.rect.x = foo.rect.x - 1280
    # Left
    player_doorLeft = pygame.sprite.spritecollide(player, wall_groupLeft, False)
    for foo in player_doorLeft:
        player.rect.x = player.rect.x + 1220
        for foo in door_group:
            foo.delete()
        mapy = mapy - 1
        mapDoors()
        for foo in wall_group:
            foo.rect.x = foo.rect.x + 1280
    # Up
    player_doorUp = pygame.sprite.spritecollide(player, wall_groupUp, False)
    for foo in player_doorUp:
        player.rect.y = player.rect.y + 660
        for foo in door_group:
            foo.delete()
        mapx = mapx - 1
        mapDoors() 
        for foo in wall_group:
            foo.rect.y = foo.rect.y + 720
    # Down
    player_doorDown = pygame.sprite.spritecollide(player, wall_groupDown, False)
    for foo in player_doorDown:
        player.rect.y = player.rect.y - 660
        for foo in door_group:
            foo.delete()
        mapx = mapx + 1
        mapDoors()
        for foo in wall_group:
            foo.rect.y = foo.rect.y - 720
    
    print(mapx, mapy)
    
    # -- CLOSING OFF DOORS WHERE NECESSARY


    # -- #
    screen.fill(BLACK)
    font = pygame.font.Font(None, 25)
    txt = font.render("stamina count al;ksjdo;k: " + str(stamina), True, WHITE)
    screen.blit(txt, (400, 100))
    
    all_sprites_list.update()

    all_sprites_list.draw(screen)
 
    pygame.display.flip()
 
    clock.tick(240)
 
pygame.quit()