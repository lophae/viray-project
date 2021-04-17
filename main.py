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
            elif col == 3:
                w = Wall(YELLOW, 10, 40, x + 30, y)
                all_sprites_list.add(w)
                wall_groupRight.add(w)
            elif col == 2:
                w = Wall(YELLOW, 10, 40, x, y)
                all_sprites_list.add(w)
                wall_groupLeft.add(w)
            elif col == 4:
                w = Wall(YELLOW, 40, 10, x, y)
                all_sprites_list.add(w)
                wall_groupUp.add(w)
            elif col == 5:
                w = Wall(YELLOW, 40, 10, x, y + 30)
                all_sprites_list.add(w)
                wall_groupDown.add(w)
            x = x + 40
        x = 0
        y = y + 40
spawnRoom()

def mapCreate():
    x = 0
    y = 0
    z = 0
    originalx = 13
    originaly = 13
    previousNum = 0
    while z != level1rooms:
        randomNum = random.randint(1, 4)
        randomRoom = random.randint(0, 2)

        # no overlapping
        if randomNum == 1:
            if mapGrid[originalx][originaly + 1] == 1:
                while randomNum == 1:
                    randomNum = random.randint(1, 4)
        if randomNum == 2:
            if mapGrid[originalx][originaly - 1] == 1:
                while randomNum == 2:
                    randomNum = random.randint(1, 4)
        if randomNum == 3:
            if mapGrid[originalx - 1][originaly] == 1:
                while randomNum == 3:
                    randomNum = random.randint(1, 4)
        if randomNum == 4:
            if mapGrid[originalx + 1][originaly] == 1:
                while randomNum == 4:
                    randomNum = random.randint(1, 4)

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
        previousNum = randomNum
        z += 1
mapCreate() 

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
        player.rect.x = player.rect.x - 610
        for foo in wall_group:
            foo.rect.x = foo.rect.x - 640
    # Left
    player_doorLeft = pygame.sprite.spritecollide(player, wall_groupLeft, False)
    for foo in player_doorLeft:
        player.rect.x = player.rect.x + 610
        for foo in wall_group:
            foo.rect.x = foo.rect.x + 640
    # Up
    player_doorUp = pygame.sprite.spritecollide(player, wall_groupUp, False)
    for foo in player_doorUp:
        player.rect.y = player.rect.y + 330
        for foo in wall_group:
            foo.rect.y = foo.rect.y + 360
    # Down
    player_doorDown = pygame.sprite.spritecollide(player, wall_groupDown, False)
    for foo in player_doorDown:
        player.rect.y = player.rect.y - 330
        for foo in wall_group:
            foo.rect.y = foo.rect.y - 360

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