import pygame, math, random, sys
from variables import *
from settings import *

# -- other sprite list
wall_group = pygame.sprite.Group()
door_group = pygame.sprite.Group()
doorclose_group = pygame.sprite.Group()

arraySpeed = [-1, 1] # for basic enemies
bossArraySpeed = [-3, 3] # for boss type 2

class Player(pygame.sprite.Sprite):
    def __init__(self, colour):
        super().__init__()
        self.image = pygame.Surface([40,40])
        self.image.fill(colour)
        self.rect = self.image.get_rect()
        self.rect.x = 620
        self.rect.y = 340
        self.health = 6
        self.healthMax = 6
        self.ammo = 5
        self.ammoMax = 5
        self.stamina = 300
        self.staminaMax = 300

        self.reloadItem = False # attributes for upgrades / abilities
        self.reloadItemCount = 0 
        self.reloadTime = 3500

        self.teleport = False
        self.teleportCount = 0
        self.teleportCountMax = 0

        self.passive = False

        self.bulletSpeedUp = False
        self.bulletSizeUp = False

        self.doubleDam = False
        self.damage = 1
        
    def move(self, x_val, y_val): # method for moving the player
        self.rect.x += x_val 
        self.rect.y += y_val

    def delete(self): # method to remove the sprite
        self.kill()

class Bullet(pygame.sprite.Sprite):
    def __init__(self, colour, posx, posy, targetx, targety, speed, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(colour)
        self.rect = self.image.get_rect()
        angle = math.atan2(targety-posy, targetx-posx) # get angle to target in radians
        self.dx = math.cos(angle) * speed
        self.dy = math.sin(angle) * speed
        self.x = posx
        self.y = posy
    
    def move(self): # method to automatically move the bullet sprite across the screen
        self.x = self.x + self.dx
        self.y = self.y + self.dy
        self.rect.x = int(self.x) - 5
        self.rect.y = int(self.y) - 5

    def delete(self): # method to remove the sprite
        self.kill()

class Wall(pygame.sprite.Sprite): # sprite used for the door openings 
    def __init__(self, colour, width, height, posx, posy):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(colour)
        self.rect = self.image.get_rect()
        self.rect.x = posx
        self.rect.y = posy

    def delete(self): # method to remove the sprite
        self.kill()

class Wall2(pygame.sprite.Sprite): # sprite for the walls of the room
    def __init__(self, width, height, posx, posy):
        super().__init__()
        wall_img = pygame.image.load("assets/wall.png") # using imported image
        self.image = pygame.Surface([width, height])
        self.image.blit(wall_img,(0,0))
        self.rect = self.image.get_rect()
        self.rect.x = posx
        self.rect.y = posy

    def delete(self): # method to remove the sprite
        self.kill()

class Teleporter(pygame.sprite.Sprite): 
    def __init__(self):
        super().__init__()
        tp_img = pygame.image.load("assets/teleporter.png") # using imported image
        self.image = pygame.Surface([40,40])
        self.image.blit(tp_img,(0,0))
        self.rect = self.image.get_rect()
        self.rect.x = 620
        self.rect.y = 340
    
    def delete(self): # method to remove the sprite
        self.kill()

class enemyBullet(pygame.sprite.Sprite):
    def __init__(self, posx, posy, targetx, targety):
        super().__init__()
        self.image = pygame.Surface([10, 10])
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        angle = math.atan2(targety-posy, targetx-posx) # get angle to target in radians
        self.dx = math.cos(angle) * 1.5
        self.dy = math.sin(angle) * 1.5
        self.x = posx
        self.y = posy

    def update(self): # method to automatically move bullet sprite 
        self.x = self.x + self.dx
        self.y = self.y + self.dy
        self.rect.x = int(self.x)
        self.rect.y = int(self.y)

    def delete(self): # get angle to target in radians
        self.kill() 

class Enemy1(pygame.sprite.Sprite):
    def __init__(self, colour):
        super().__init__()
        self.image = pygame.Surface([30, 30])
        self.image.fill(colour)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(560,680)
        self.rect.y = random.randint(320,400)
        self.speed_x = arraySpeed[random.randint(0, 1)] # randomised direction of the sprite
        self.speed_y = arraySpeed[random.randint(0, 1)]
    
    def update(self): # update method that controls the automatic movement of enemy sprites
        self.rect.x = self.rect.x + self.speed_x
        self.rect.y = self.rect.y + self.speed_y
        enemyWall = pygame.sprite.spritecollide(self, wall_group, False)
        enemyDoor = pygame.sprite.spritecollide(self, door_group, False)
        enemycloseDoor = pygame.sprite.spritecollide(self, doorclose_group, False)

        # checking for collisions with different sprites
        for foo in enemyWall:
            self.speed_x = arraySpeed[random.randint(0, 1)]
            self.speed_y = arraySpeed[random.randint(0, 1)]
            self.rect.x = self.old_x
            self.rect.y = self.old_y
        for foo in enemyDoor:
            self.speed_x = arraySpeed[random.randint(0, 1)]
            self.speed_y = arraySpeed[random.randint(0, 1)]
            self.rect.x = self.old_x
            self.rect.y = self.old_y
        for foo in enemycloseDoor:
            self.speed_x = arraySpeed[random.randint(0, 1)]
            self.speed_y = arraySpeed[random.randint(0, 1)]
            self.rect.x = self.old_x
            self.rect.y = self.old_y

        self.old_x = self.rect.x
        self.old_y = self.rect.y
        
    def delete(self): # method to remove sprite
        self.kill()

class Enemy2(pygame.sprite.Sprite):
    def __init__(self, colour, move):
        super().__init__()
        self.image = pygame.Surface([30,30])
        self.image.fill(colour)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(340, 980)
        self.rect.y = 360
        self.move = move

    def update(self): # method to move this enemy sprite back and forth, at a 
                      # consistent speed
        if self.move == 1:
            self.rect.x += 2
        if self.move == 2:
            self.rect.x -= 2

        if self.rect.x < 80:
            self.move = 1
        if self.rect.x > 1200:
            self.move = 2

    def delete(self):
        self.kill()

class Enemy3(pygame.sprite.Sprite):
    def __init__(self, colour):
        super().__init__()
        self.image = pygame.Surface([35,35])
        self.image.fill(colour)
        self.rect = self.image.get_rect()
        self.rect.x = random.choice([60,1180])
        self.rect.y = random.choice([60,620])
    
    def update(self): # method to randomly teleport this enemy sprite across the corners
                      # of the room
        randomT = random.randint(1,125)
        if randomT == 50:
            self.rect.x = random.choice([60, 1180])
            self.rect.y = random.choice([60, 620])

    def delete(self):
        self.kill

class Boss1(pygame.sprite.Sprite):
    def __init__(self, colour, targety, targetx):
        super().__init__()
        self.image = pygame.Surface([60, 60])
        self.image.fill(colour)
        self.rect = self.image.get_rect()
        self.rect.x = 640
        self.rect.y = 360
        self.x = 580
        self.y = 300
        self.target_x = targetx
        self.target_y = targety
        angle = math.atan2(self.target_y-self.rect.y, self.target_x-self.rect.x) # get angle to target in radians
        self.dx = math.cos(angle) * 4
        self.dy = math.sin(angle) * 4
        self.health = 12

    def attack(self): # boss sprite is moved towards the location of the target
        self.x = self.x + self.dx
        self.y = self.y + self.dy
        self.rect.x = int(self.x)
        self.rect.y = int(self.y)
    
    def stop(self, targety, targetx): # this method is called whenever the boss hits a wall
        angle = math.atan2(targety-self.rect.y, targetx-self.rect.x)
        self.dx = 0
        self.dy = 0
        self.dx = math.cos(angle) * 4
        self.dy = math.sin(angle) * 4
    
    def update(self): # checks the health of the boss
        font = pygame.font.Font(None, 25)
        if self.health == 0:
            self.kill()
        elif self.health > 0:
            txt = font.render("boss health: " + str(self.health), True, WHITE)
            screen.blit(txt, (60, 200))

class Boss2(pygame.sprite.Sprite):
    def __init__(self, colour):
        super().__init__()
        self.image = pygame.Surface([70, 70])
        self.image.fill(colour)
        self.rect = self.image.get_rect()
        self.rect.x = 640
        self.rect.y = 360
        self.speed_x = bossArraySpeed[random.randint(0, 1)] # random direction chosen
        self.speed_y = bossArraySpeed[random.randint(0, 1)]
        self.health = 10

    # update method that controls the automatic movement of enemy sprites
    def update(self):
        self.rect.x = self.rect.x + self.speed_x
        self.rect.y = self.rect.y + self.speed_y
        bossWall = pygame.sprite.spritecollide(self, wall_group, False)
        bossDoor = pygame.sprite.spritecollide(self, door_group, False)
        bosscloseDoor = pygame.sprite.spritecollide(self, doorclose_group, False)

        for foo in bossWall: # checking for collisions with other sprites
            self.speed_x = bossArraySpeed[random.randint(0,1)]
            self.speed_y = bossArraySpeed[random.randint(0,1)]
            self.rect.x = self.old_x
            self.rect.y = self.old_y
        for foo in bossDoor:
            self.speed_x = bossArraySpeed[random.randint(0,1)]
            self.speed_y = bossArraySpeed[random.randint(0,1)]
            self.rect.x = self.old_x
            self.rect.y = self.old_y
        for foo in bosscloseDoor:
            self.speed_x = bossArraySpeed[random.randint(0,1)]
            self.speed_y = bossArraySpeed[random.randint(0,1)]
            self.rect.x = self.old_x
            self.rect.y = self.old_y
        
        self.old_x = self.rect.x
        self.old_y = self.rect.y

        font = pygame.font.Font(None, 25)
        if self.health == 0:
            self.kill()
        elif self.health > 0:
            txt = font.render("boss health: " + str(self.health), True, WHITE)
            screen.blit(txt, (60, 200))  
            
class Boss3(pygame.sprite.Sprite):
    def __init__(self, colour):
        super().__init__()
        self.image = pygame.Surface([65, 65])
        self.image.fill(colour)
        self.rect = self.image.get_rect()
        self.rect.x = 640
        self.rect.y = 360
        self.health = 8

    def update(self): # boss sprite is teleported randomly across the entire area of the room
        randomT = random.randint(1,125) # The chance of the boss teleporting is 1/125
        if randomT == 50:
            self.rect.x = random.randrange(200, 1080)
            self.rect.y = random.randrange(200, 580)

        font = pygame.font.Font(None, 25)
        if self.health == 0:
            self.kill()
        elif self.health > 0:
            txt = font.render("boss health: " + str(self.health), True, WHITE)
            screen.blit(txt, (60, 200))  

class MiniMap(pygame.sprite.Sprite):
    def __init__(self, colour, xc, yc):
        super().__init__()
        self.image = pygame.Surface([30, 20])
        self.image.fill(colour)
        self.rect = self.image.get_rect()
        self.rect.x = xc
        self.rect.y = yc

    def delete(self):
        self.kill()

class MiniPlayer(pygame.sprite.Sprite):
    def __init__(self, colour, xc, yc):
        super().__init__()
        self.image = pygame.Surface([10, 10])
        self.image.fill(colour)
        self.rect = self.image.get_rect()
        self.rect.x = xc
        self.rect.y = yc

    def delete(self):
        self.kill()

class Chest(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        chest_img = pygame.image.load("assets/chest_1.png") # using imported image
        self.image = pygame.Surface([20,20])
        self.image.blit(chest_img,(0,0))
        self.rect = self.image.get_rect()
        self.rect.x = 630
        self.rect.y = 350
    
    def delete(self):
        self.kill()