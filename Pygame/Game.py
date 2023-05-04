#1: 15: 39

import time
import pygame
import os
#Font library
pygame.font.init()
pygame.mixer.init()

#dimensions for the game space
WIDTH, HEIGHT = 900, 500

#sets up the actual window in which one can play
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("First Game!")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

#.Rect = rectangle
#x, y position. WIDTH and HEIGHT
#// is divide rounded or something
BORDER = pygame.Rect(0, HEIGHT//2- 10, WIDTH, 10)

BULLET_HIT_SOUND = pygame.mixer.Sound(os.path.join('Assets', 'hq-explosion-6288.mp3'))
BULLET_FIRE_SOUND = pygame.mixer.Sound(os.path.join('Assets', 'blaster-2-81267.mp3'))

HEALTH_FONT = pygame.font.SysFont('comicsans', 30)
WINNER_FONT = pygame.font.SysFont('comicsans', 100)
CREDIT_FONT = pygame.font.SysFont('comicsans', 10)
MOVES_FONT = pygame.font.SysFont('comicsans', 10)
#FPS keeps the quality consistent
FPS = 60
VEL = 5
BULLET_VEL = 7
MAX_BULLETS = 3
DASH = 15
COOLDOWN = 2
SLOW = []

#Size of the sprite
SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 55, 40

#eVENT #NUMBERS MEAN WHICH ID EVENT IS
YELLOW_HIT = pygame.USEREVENT + 1
RED_HIT = pygame.USEREVENT + 2

#Image yellow
YELLOW_SPACESHIP_IMAGE = pygame.image.load(
    os.path.join('Assets', 'Gray2.png'))
YELLOW_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(
    YELLOW_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 0)
#Image red
RED_SPACESHIP_IMAGE = pygame.image.load(
    os.path.join('Assets', 'gray3.png'))
RED_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(
    RED_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 360)

SPACE = pygame.transform.scale(pygame.image.load(
    os.path.join("Assets", '262425-PLANET-SPACE.jpg')), (WIDTH, HEIGHT))


#puts the window on
def draw_window(red, yellow, red_bullets, yellow_bullets, red_health, yellow_health):   
    WIN.blit(SPACE, (0, 0))
#If you dont draw a backround on every single frame, pygame doesn't delete the last image showing it even though it's done
    #WIN.fill(WHITE) # Hidden because it blocks the set backround above
    pygame.draw.rect(WIN, BLACK, BORDER)

    red_health_text = HEALTH_FONT.render(
        "Health: " + str(red_health), 1, WHITE)
            #redinstrucs
    red_instructions = MOVES_FONT.render('-arrow keys to move -rctrl to shoot -rshift to speed up', 1, WHITE)

    yellow_health_text = HEALTH_FONT.render(
        "Health: " + str(yellow_health), 1, WHITE)
    
    #YELLOWISTIUCION
    yellow_instructions = MOVES_FONT.render('-wasd to move -ctrl to shoot -lshift to speed up', 1, WHITE)
    WIN.blit(red_health_text, (WIDTH - red_health_text.get_width() - 10, 10))
        #iadlwghbiaw
    WIN.blit(red_instructions, (WIDTH - red_instructions.get_width() - 10, 1))
    WIN.blit(yellow_instructions, (yellow_health_text.get_height() - 10 , 1))

    WIN.blit(yellow_health_text, (10, 10))

#puts the ships on with blit (puts a layer on it)
    WIN.blit(YELLOW_SPACESHIP, (yellow.x, yellow.y))
    WIN.blit(RED_SPACESHIP, (red.x, red.y))

    for bullet in red_bullets:
        pygame.draw.rect(WIN, RED, bullet)

    for bullet in yellow_bullets:
        pygame.draw.rect(WIN, YELLOW, bullet)        

    pygame.display.update()

def yellow_handle_movement(keys_pressed, yellow):
    if keys_pressed[pygame.K_a] and yellow.x - VEL > 0: # LEFT
        yellow.x -= VEL
                        #WIDTH
    if keys_pressed[pygame.K_d] and yellow.x + VEL + yellow.width < WIDTH: # RIGHT
        yellow.x += VEL
    if keys_pressed[pygame.K_w] and yellow.y - VEL > 0: # UP
        yellow.y -= VEL
                    #border.y
    if keys_pressed[pygame.K_s] and yellow.y + VEL + yellow.height < BORDER.y: # DOWN
        yellow.y += VEL


    if keys_pressed[pygame.K_a]and yellow.x - DASH > 0 and keys_pressed[pygame.K_LSHIFT] : # Ledt
        yellow.x -= DASH
    if keys_pressed[pygame.K_d] and yellow.x + DASH + yellow.width < WIDTH and keys_pressed[pygame.K_LSHIFT]: #Right
        yellow.x += DASH
    if keys_pressed[pygame.K_w] and yellow.y - DASH > 0 and keys_pressed[pygame.K_LSHIFT]: #up 
        yellow.y -= DASH
    if keys_pressed[pygame.K_s] and yellow.y + DASH + yellow.height < BORDER.y and keys_pressed[pygame.K_LSHIFT]:#down
#        SLOW.append('slow')
        yellow.y += DASH

def red_handle_movement(keys_pressed, red):

                    #made it impossible to go out of bounds
    if keys_pressed[pygame.K_LEFT] and red.x - VEL > 0: # LEFT
        red.x -= VEL
                    #no out of bounds
    if keys_pressed[pygame.K_RIGHT] and red.x + VEL + red.width < WIDTH: # RIGHT
        red.x += VEL
    if keys_pressed[pygame.K_UP] and red.y - VEL > BORDER.y + 10: # UP
        red.y -= VEL
    if keys_pressed[pygame.K_DOWN] and red.y + VEL + red.height < HEIGHT - 15: # DOWN
        red.y += VEL

        #TRY TO <AKE DASH
        #NOW TRY TO MERGE THIS WITH EVERYTHING ELSE
#    for x in SLOW:
#        if x == 'slow':
#            RVEL = 1
#            
#            RVEL = 5
    if keys_pressed[pygame.K_LEFT]and red.x - DASH > 0 and keys_pressed[pygame.K_RSHIFT] : # Ledt
        red.x -= DASH
    if keys_pressed[pygame.K_RIGHT] and red.x + DASH + red.width < WIDTH and keys_pressed[pygame.K_RSHIFT]: #Right
        red.x += DASH
    if keys_pressed[pygame.K_UP] and red.y - DASH > BORDER.y + 12 and keys_pressed[pygame.K_RSHIFT]: #up 
        red.y -= DASH
    if keys_pressed[pygame.K_DOWN] and red.y + DASH + red.height < HEIGHT - 15 and keys_pressed[pygame.K_RSHIFT]:#down
#        SLOW.append('slow')
        red.y += DASH

        





def handle_bullets(yellow_bullets, red_bullets, yellow, red):
    for bullet in yellow_bullets:
                    #Made into a y axis
        bullet.y += BULLET_VEL
#This only works if both objects are rectangles apparantly
        if red.colliderect(bullet):
#Events can affect other functions or something       
            pygame.event.post(pygame.event.Event(RED_HIT))
            yellow_bullets.remove(bullet)
                    #made y axis and HEIGHT from WIDTH, >=
        elif bullet.y >= HEIGHT:
            yellow_bullets.remove(bullet)

    for bullet in red_bullets:  
                    #y axis, <=
        bullet.y -= BULLET_VEL
        if yellow.colliderect(bullet):
            pygame.event.post(pygame.event.Event(YELLOW_HIT))
            red_bullets.remove(bullet)
                #y
        elif bullet.y <= 0:
            red_bullets.remove(bullet)

def draw_winner(text, due):
    draw_text = WINNER_FONT.render(text, 1, WHITE)
    draw_text2 = CREDIT_FONT.render(due, 1, WHITE)
    WIN.blit(draw_text, (WIDTH/2 - draw_text.get_width()/
                         2, HEIGHT/2 - draw_text.get_height()/2))
    WIN.blit(draw_text2, (1, HEIGHT/2 - draw_text2.get_height()))
    pygame.display.update()
# DELAY WORKS BY MULTIPLYING NUMBER OF SECONDS TIMES 1000! SO THIS IS 5 seconds
    pygame.time.delay(3000)

def main():
#Coordinates for the ship
            #made different
    red = pygame.Rect(WIDTH//2, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    yellow = pygame.Rect(WIDTH//2, 100, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)

    red_bullets = []
    yellow_bullets = []

    red_health = 10
    yellow_health = 10

#putting it actually
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                #MOVE THIS FOR QUIT
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LCTRL and len(yellow_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(
                                # // 2 and remove the -2 # BULLET SHAPE
                        yellow.x + yellow.width//2, yellow.y + yellow.height//2, 5, 10)
                    yellow_bullets.append(bullet)
                    BULLET_FIRE_SOUND.play()

                if event.key == pygame.K_RCTRL and len(red_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(
#// is non decimal division?
                                #CHANFE # BULLET SHAPE
                        red.x + red.width//2, red.y + red.height//2 , 5, 10)
                    red_bullets.append(bullet)
                    BULLET_FIRE_SOUND.play()

        #print(red_bullets, yellow_bullets) # Shows the bullet location
            if event.type == RED_HIT:
                red_health -= 1
                BULLET_HIT_SOUND.play()

            if event.type == YELLOW_HIT:
                yellow_health -= 1
                BULLET_HIT_SOUND.play()

        credit = "Spaceship sprites by Lowich on itch"

        winner_text =""
        if red_health <= 0:
            winner_text = "Yellow Wins!"

        if yellow_health <= 0:
            winner_text = "Red Wins!"

        if winner_text != "":
            draw_winner(winner_text, credit)
            break


        keys_pressed = pygame.key.get_pressed()
        yellow_handle_movement(keys_pressed, yellow)
        red_handle_movement(keys_pressed, red)

        handle_bullets(yellow_bullets, red_bullets, yellow, red)

        draw_window(red, yellow, red_bullets, yellow_bullets, red_health, yellow_health)

    main()
    #IF WANT TO CONTINUE REPLACE QUIT WITH: main()
    #MOVE THIS FOR QUIT

#runs # edited
if __name__ == "__main__":
    main()
