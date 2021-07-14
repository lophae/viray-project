import pygame, math
from variables import *
from settings import *

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
    def __init__(self, colour, posx, posy, targetx, targety):
        super().__init__()
        self.image = pygame.Surface([30, 30])
        self.image.fill(colour)
        self.rect = self.image.get_rect()
        self.rect.x = 50
        self.rect.y = 50
    
    def move(self):
        #self.x = self.x + self.dx
        #self.y = self.y + self.dy
        #self.rect.x = int(self.x)
        #self.rect.y = int(self.y)
        pass

    def shoot(self):
        #eb = enemyBullet(self.rect.x, self.rect.y, Player.rect.x, Player.rect.y)
        #enemybullet_group.add(eb)
        pass

    def delete(self):
        self.kill()

class Pause(pygame.sprite.Sprite):
    def __init__(self, colour):
        super().__init__()
        self.image = pygame.Surface([200, 200])
        self.image.fill(colour)
        self.rect = self.image.get_rect()
        self.rect.x = 10
        self.rect.y = 10

        
        