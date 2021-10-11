import pygame, math, random, sys
from variables import *
from settings import *

wall_group = pygame.sprite.Group()
door_group = pygame.sprite.Group()
doorclose_group = pygame.sprite.Group()

class Player(pygame.sprite.Sprite):
    def __init__(self, colour):
        super().__init__()
        self.image = pygame.Surface([40,40])
        self.image.fill(colour)
        self.rect = self.image.get_rect()
        self.rect.x = 620
        self.rect.y = 340
        self.health = 200 
        
    def move(self, x_val, y_val):
        self.rect.x += x_val 
        self.rect.y += y_val

    def delete(self):
        self.kill()

class Bullet(pygame.sprite.Sprite):
    def __init__(self, colour, posx, posy, width, height, speed, targetx, targety):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(colour)
        self.rect = self.image.get_rect()
        angle = math.atan2(targety-posy, targetx-posx) # get angle to target in radians
        self.dx = math.cos(angle) * speed
        self.dy = math.sin(angle) * speed
        self.x = posx
        self.y = posy
    
    def move(self):
        self.x = self.x + self.dx
        self.y = self.y + self.dy
        self.rect.x = int(self.x) - 5
        self.rect.y = int(self.y) - 5

    def delete(self):
        self.kill()

class Wall(pygame.sprite.Sprite):
    def __init__(self, colour, width, height, posx, posy):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(colour)
        self.rect = self.image.get_rect()
        self.rect.x = posx
        self.rect.y = posy

    def delete(self):
        self.kill()

class Teleporter(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([20,20])
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.rect.x = 630
        self.rect.y = 360
    
    def delete(self):
        self.kill()

class enemyBullet(pygame.sprite.Sprite):
    def __init__(self, posx, posy, targetx, targety):
        super().__init__()
        self.image = pygame.Surface([10, 10])
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        angle = math.atan2(targety-posy, targetx-posx) 
        self.dx = math.cos(angle) * 1.5
        self.dy = math.sin(angle) * 1.5
        self.x = posx
        self.y = posy

    def update(self):
        self.x = self.x + self.dx
        self.y = self.y + self.dy
        self.rect.x = int(self.x)
        self.rect.y = int(self.y)

    def delete(self):
        self.kill() 

class Enemy1(pygame.sprite.Sprite):
    def __init__(self, colour):
        super().__init__()
        self.image = pygame.Surface([30, 30])
        self.image.fill(colour)
        self.rect = self.image.get_rect()
        self.rect.x = 50
        self.rect.y = 50
        self.speed_x = arraySpeed[random.randint(0, 1)]
        self.speed_y = arraySpeed[random.randint(0, 1)]
    
    def update(self):
        self.rect.x = self.rect.x + self.speed_x
        self.rect.y = self.rect.y + self.speed_y
        enemyWall = pygame.sprite.spritecollide(self, wall_group, False)
        enemyDoor = pygame.sprite.spritecollide(self, door_group, False)
        enemycloseDoor = pygame.sprite.spritecollide(self, doorclose_group, False)

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
        
    def delete(self):
        self.kill()

class Enemy2(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

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
        angle = math.atan2(self.target_y-self.rect.y, self.target_x-self.rect.x)
        self.dx = math.cos(angle) * 4
        self.dy = math.sin(angle) * 4
        self.health = 25

    def attack(self):
        self.x = self.x + self.dx
        self.y = self.y + self.dy
        self.rect.x = int(self.x)
        self.rect.y = int(self.y)
    
    def stop(self, targety, targetx):
        angle = math.atan2(targety-self.rect.y, targetx-self.rect.x)
        self.dx = 0
        self.dy = 0
        self.dx = math.cos(angle) * 3
        self.dy = math.sin(angle) * 3
    
    def update(self):
        font = pygame.font.Font(None, 25)
        if self.health == 0:
            self.kill()
        elif self.health > 0:
            txt = font.render("boss health: " + str(self.health), True, WHITE)
            screen.blit(txt, (60, 200))