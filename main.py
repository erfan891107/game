import pygame
from Map_game import map
from pygame.locals import Rect

#display

WIDTH, HEIGHT = 1200, 600
display = pygame.display.set_mode((WIDTH, HEIGHT))

#gamer_skin

#colors

BLACK  = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

x, y = 75, 75

gamer = Rect ([x, y, 25, 25])

clock = pygame.time.Clock()

x_change, y_change = 0, 0

has_power = True
show_bridge = False
space_power = False

game = True

x, y = 0, 0


def plot_player(direction):
    player = pygame.image.load(f"player {direction}.PNG")
    player = pygame.transform.scale(player,(25, 25))
    return player

def collide_player_rects(gamer, rects):
    for mane in rects:
        if pygame.Rect.colliderect(gamer, mane):
            return True
    return False


def x_change_gamer():
    gamer.x -= x_change
    gamer.y -= y_change
    
def not_gravity():
    for i in range (5) :
        gamer.y -= 1

def space_xy():
    for i in range (30) :
        gamer.x += 0
        gamer.y += -1

        x_change = 0
        y_change = -1

direction = "right"

while game:
    #QUIT
    display.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False

    keys = pygame.key.get_pressed()

    # RIGHT
    if keys[pygame.K_RIGHT] :
        gamer.x += 5
        gamer.y += 0
  
        x_change = 5
        y_change = 0
        direction = "right"
    # LEFT
    if keys[pygame.K_LEFT] :
        gamer.x += -5
        gamer.y += 0

        x_change = -5
        y_change = 0
        direction = "left"

    player = plot_player(direction)

    if keys[pygame.K_e]:
        if has_power:

            for i in range (150):
                if direction == "right":
                    gamer.x += 1
                    x_change = 1
                else:
                    gamer.x -= 1
                    x_change = -1

            has_power = False


    gamer.x %= WIDTH
    gamer.y %= HEIGHT
    
    if collide_player_rects(gamer,  map.levels[1]["wall"]):
    
        x_change_gamer()
    
    if collide_player_rects(gamer, map.levels[1]["mane_1"]):
            
        x_change_gamer()

    if collide_player_rects(gamer,  map.levels[1]["bridge_1"]):

        x_change_gamer() 
    
    if collide_player_rects(gamer,  map.levels[1]["mane_2"]):

        x_change_gamer()   

    if collide_player_rects(gamer, map.levels[1]["bridge_2"]):

        x_change_gamer() 



    for i in range (5) :
        gamer.y += 1
    
    if keys[pygame.K_SPACE] and collide_player_rects(gamer,  map.levels[1]["wall"]):
        space_xy()
                    
    for mane in map.levels[1]["mane_1"]:
        if 1024 < gamer.x and 1050 > gamer.x :
            space_power = True
        if space_power == True and  keys[pygame.K_c] and pygame.Rect.colliderect(gamer, mane) :
                
            gamer.x += 0
            gamer.y += -100

            x_change = 0
            y_change = -100 

            space_power = False

        if pygame.Rect.colliderect(gamer, mane) :
            if keys[pygame.K_SPACE]:
                space_xy() 


    if keys[pygame.K_SPACE] and collide_player_rects(gamer, map.levels[1]["bridge_1"]):
        space_xy()

    if keys[pygame.K_SPACE] and collide_player_rects(gamer, map.levels[1]["mane_2"]):
        space_xy()

    if keys[pygame.K_SPACE] and collide_player_rects(gamer, map.levels[1]["bridge_2"]):
        space_xy()
      
    if collide_player_rects(gamer,  map.levels[1]["mane_1"]):
            if gamer.x >= 950 :
                show_bridge = True
 
    if show_bridge:
        for mane in map.levels[1]["bridge_1"] :
            pygame.draw.rect(display, RED, [mane.x, mane.y, mane.width, mane.height])

    if collide_player_rects(gamer,  map.levels[1]["wall"]):
        not_gravity()

    if collide_player_rects(gamer,  map.levels[1]["mane_1"]):
        not_gravity()

    if show_bridge and collide_player_rects(gamer,  map.levels[1]["bridge_1"]):
        not_gravity()

    if collide_player_rects(gamer,  map.levels[1]["mane_2"]):
        not_gravity()

    if collide_player_rects(gamer,  map.levels[1]["bridge_2"]):
        not_gravity()


    map.draw_rects(display, 1, "wall")
    map.draw_rects(display, 1, "mane_1")
    map.draw_rects(display, 1, "mane_2")
    map.draw_rects(display, 1, "bridge_2")


    display.blit(player, [gamer.x, gamer.y])

    pygame.display.update()

    clock.tick(50)    