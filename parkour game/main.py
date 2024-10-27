import pygame
from map_game import map
from pygame.locals import Rect
pygame.init()

#display

WIDTH, HEIGHT = 1200, 600
display = pygame.display.set_mode((WIDTH, HEIGHT))

#colors

BLACK  = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)

x, y = 75, 75

font = pygame.font.Font("pixel_font/upheavtt.ttf", 60)
write_score = font.render((f"SCORE:0"), True, WHITE)

gamer = Rect ([x, y, 25, 25])
coins = [Rect([850, 165, 25, 25])]
gun_trap = Rect ([55, 520, 100, 25])
finish_level_1 = Rect ([1075, 396, 60, 60])

clock = pygame.time.Clock()

x_change, y_change = 0, 0
score_number = 0
wait_time = 0

Trap_Ammo_x = 125
Trap_Ammo = [Rect ([Trap_Ammo_x, 500, 10, 5])]

space_power_1 = True
space_power_2 = True
space_power_3 = True
show_bridge = False
class_hint_show = False
gameover = False
game = True

x, y = 0, 0

score = pygame.image.load("score.PNG")
score = pygame.transform.scale(score,(25, 25))

trap = pygame.image.load("trap.PNG")
trap = pygame.transform.scale(trap,(100, 25))

finish = pygame.image.load("finish.PNG")
finish = pygame.transform.scale(finish,(60, 60))

def plot_player(direction):
    player = pygame.image.load(f"player {direction}.PNG")
    player = pygame.transform.scale(player,(25, 25))
    return player

def collide_player_rects(gamer, rects):
    for mane in rects:
        if pygame.Rect.colliderect(gamer, mane):
            return True
    return False

def collide_player_coins(gamer, coins):
    for coin in coins:
        if pygame.Rect.colliderect(gamer, coin):
            coins.remove(coin)
            return True
    return False

def collide_player_trap(Trap_Ammo, rects):
    for mane in rects:
        if pygame.Rect.colliderect(Trap_Ammo, mane):
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
    if keys[pygame.K_d] :
        gamer.x += 5
        gamer.y += 0
  
        x_change = 5
        y_change = 0
        direction = "right"
    # LEFT
    if keys[pygame.K_a] :
        gamer.x += -5
        gamer.y += 0

        x_change = -5
        y_change = 0
        direction = "left"

    player = plot_player(direction)

    if space_power_1 == True and keys[pygame.K_e] and direction == "right":
    
        gamer.x += 150
        x_change = 150
        space_power_1 = False

    if space_power_1 == True and keys[pygame.K_e] and direction == "left":
        gamer.x -= 150
        x_change = -150
        space_power_1 = False

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
                    
    if space_power_2 == True and  keys[pygame.K_SPACE] and collide_player_rects(gamer, map.levels[1]["mane_1"]) and 1024 < gamer.x and 1050 > gamer.x :
        gamer.x += 0
        gamer.y += -100
        x_change = 0
        y_change = -100 

        space_power_2 = False

    if space_power_3 == True and  keys[pygame.K_SPACE] and collide_player_rects(gamer,  map.levels[1]["mane_2"]) and 50 < gamer.x and 100 > gamer.x and direction == "right":
        gamer.x += 75
        gamer.y += -75
        x_change = 75
        y_change = -75

    if keys[pygame.K_SPACE] and collide_player_rects(gamer, map.levels[1]["mane_1"]):
        space_xy()

    if keys[pygame.K_SPACE] and collide_player_rects(gamer, map.levels[1]["mane_2"]):
        space_xy()

    if keys[pygame.K_SPACE] and collide_player_rects(gamer, map.levels[1]["bridge_2"]):
        space_xy()
      
    if collide_player_rects(gamer,  map.levels[1]["mane_1"]) and gamer.x >= 950 :
        show_bridge = True

    if show_bridge == True :
        map.draw_rects(display, 1, "bridge_1")
        if keys[pygame.K_SPACE] and collide_player_rects(gamer, map.levels[1]["bridge_1"]):
            space_xy()

    if collide_player_rects(gamer,  map.levels[1]["wall"]):
        not_gravity()

    if collide_player_rects(gamer,  map.levels[1]["mane_1"]):
        not_gravity()

    if show_bridge == True and collide_player_rects(gamer,  map.levels[1]["bridge_1"]):
        not_gravity()

    if collide_player_rects(gamer,  map.levels[1]["mane_2"]):
        not_gravity()

    if collide_player_rects(gamer,  map.levels[1]["bridge_2"]):
        not_gravity()    

    if collide_player_coins(gamer,  coins):
        score_number += 1
        write_score = font.render((f"SCORE:{score_number}"), True, WHITE)

    if show_bridge == True and gamer.x <= 700 : 
        class_hint_show = True 

    Trap_Ammo = [Rect ([Trap_Ammo_x, 525, 10, 5])]
    Trap_Ammo_x += 5
    
    if collide_player_trap(Trap_Ammo[0],  map.levels[1]["wall"]):
        Trap_Ammo_x = 125

    if collide_player_rects(gamer,  Trap_Ammo) :
        gameover = True

    map.draw_rects(display, 1, "wall")
    map.draw_rects(display, 1, "mane_1")
    map.draw_rects(display, 1, "mane_2")
    map.draw_rects(display, 1, "bridge_2")

    for mane in Trap_Ammo :
        pygame.draw.rect(display, RED, [mane.x, mane.y, mane.width, mane.height])  
    display.blit(write_score,(5, -10)) 
    display.blit(player, [gamer.x, gamer.y])
    for c in coins:
        display.blit(score, [c.x, c.y])
    display.blit(trap, [gun_trap.x, gun_trap.y])
    display.blit(finish, [finish_level_1.x, finish_level_1.y])

    if class_hint_show == True :
        font_class = pygame.font.Font("pixel_font/upheavtt.ttf", 20)
        class_hint = font_class.render(("press (e) to use class"), True, WHITE)
        display.blit(class_hint,(505, 300))   

    if gameover == True :
        font_gameover = pygame.font.Font("pixel_font/upheavtt.ttf", 200)
        game_over = font_gameover.render(("GAME OVER"), True, WHITE)
        display.fill(BLACK)
        display.blit(game_over,(75, 150))        
        game = False

    if collide_player_rects(gamer,  map.levels[1]["finish"]):
        font_win = pygame.font.Font("pixel_font/upheavtt.ttf", 200)
        win = font_win.render(("WIN"), True, WHITE)
        display.fill(BLACK)
        display.blit(win,(425, 150))   
        game = False

    pygame.display.update()
    if not game:
        pygame.time.wait(10000)
    clock.tick(50)    