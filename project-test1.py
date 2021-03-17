import pygame, math, random
from pygame.locals import *

# Import Other Files
from classes import Player, Bullet
from levels import file1

print(file1)

# Colours
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

pygame.init()

# Adding sprites to groups
all_sprites_list = pygame.sprite.Group()
player = Player(WHITE)
all_sprites_list.add(player)
all_sprites_list

bullet_group = pygame.sprite.Group()

clock = pygame.time.Clock()
stamina = 150

# Screen Settings
size = (1500, 750)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Test1")

# Loop until the user clicks the close button.
done = False

# Register mouse onclick
click = False
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    
    keys = pygame.key.get_pressed() # player movement
    if keys[pygame.K_a]:
        player.move(-1,0)
    if keys[pygame.K_d]:
        player.move(1,0)
    if keys[pygame.K_w]:
        player.move(0,-1)
    if keys[pygame.K_s]:
        player.move(0,1)
    
    if keys[pygame.K_a] and keys[pygame.K_j] and stamina > 1: # player stamina
        player.move(-4,0)
        stamina = stamina - 2
    if keys[pygame.K_d] and keys[pygame.K_j] and stamina > 1:
        player.move(4,0)
        stamina = stamina - 2
    if keys[pygame.K_w] and keys[pygame.K_j] and stamina > 1:
        player.move(0,-4)
        stamina = stamina - 2
    if keys[pygame.K_s] and keys[pygame.K_j] and stamina > 1:
        player.move(0,4)
        stamina = stamina - 2

    if not keys[pygame.K_j]: # key for stamina
        if stamina != 150:
            stamina = stamina + 1

    if event.type == MOUSEBUTTONDOWN: # register mouse down
        if event.button == 1 and click == False:
            click = True
        
    if click: # shoot if mouse click
        x, y = pygame.mouse.get_pos()
        b = Bullet(WHITE, player.rect.centerx, player.rect.centery, 10, 10, 5, x, y)
        bullet_group.add(b)
        all_sprites_list.add(b)
        click = False

    
    # -- #
    screen.fill(BLACK)
    font = pygame.font.Font(None, 25)
    txt = font.render("press 'j' to sprint    " + str(stamina), True, WHITE)
    screen.blit(txt, (400, 100))
    
    all_sprites_list.update()

    all_sprites_list.draw(screen)
 
    pygame.display.flip()
 
    clock.tick(60)
 
pygame.quit()