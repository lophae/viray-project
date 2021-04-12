import pygame, math

class Player(pygame.sprite.Sprite):
    def __init__(self, colour):
        super().__init__()
        self.image = pygame.Surface([20,20])
        self.image.fill(colour)
        self.rect = self.image.get_rect()
        self.rect.x = 640
        self.rect.y = 360
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
    
    def update(self):
        self.x = self.x + self.dx
        self.y = self.y + self.dy
        self.rect.x = int(self.x) - 5
        self.rect.y = int(self.y) - 5

class Enemy1(pygame.sprite.Sprite):
    def __init__(self, colour):
        self.image = pygame.Surface()
        self.image.fill(colour)
        self.rect = self.image.get_rect()

class Wall(pygame.sprite.Sprite):
    def __init__(self, colour, posx, posy):
        self.image = pygame.Surface([60, 60])
        self.image.fill(colour)
        self.rect = self.image.get_rect()
        self.rect.x = posx
        self.rect.y = posy

    def update(self):
        pass