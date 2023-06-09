import pygame, os


#Lets make a window first
WIDTH, HEIGHT = 1600, 900
W, H = WIDTH//2, HEIGHT//2
pygame.display.set_caption('Game')
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
FPS = 60
VEL= 5
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)



square1 = pygame.image.load(os.path.join('square_PNG2.jpg'))
square2 = pygame.transform.rotate(pygame.transform.scale(square1, (50, 50)),0)

NEXT_LEVEL = pygame.USEREVENT + 1
PUSH_BACk = VEL * 2


#AFTER EXCRUCIATING EFFORT I HAVE PLACED A SQUARE ON A WHITE WINDOW!!!!!!!!! 9th may
def display(square, wall, button, door, exi):
    WIN.fill(WHITE)
    for i in door:
        pygame.draw.rect(WIN, (1, 1, 254), i)
    for i in wall:
        pygame.draw.rect(WIN,(255,0,0), i)
    for i in button:
        pygame.draw.rect(WIN, (0, 255, 0), i)
    pygame.draw.rect(WIN, (255, 255, 0), exi)

    WIN.blit(square2, (square.x, square.y))

    pygame.display.update()


#BASIC MOVEMENT!!!!!!!!!!!! 1;12 9th may
def movement(keys_pressed, square, wall, x, door): # WE gotta dwamake collision with wall
        # FOR EACH ITEM ADDED TO THE FOR LOOP, THE FASTER THE VEL GETS. (I'm thinking it repeats x amount of times. So divide by x amount of times.)
        #Maybe do a wall function?
        if keys_pressed[pygame.K_w] and square.y > 0 : #UP
            square.y -= VEL // x
            if square.colliderect(wall) or square.colliderect(door):
                square.y += PUSH_BACk
        if keys_pressed[pygame.K_s] and square.y + square.height < HEIGHT: #down
            square.y += VEL // x
            if square.colliderect(wall) or square.colliderect(door):
                square.y -= PUSH_BACk
        if keys_pressed[pygame.K_a] and square.x > 0: #Left
            square.x -= VEL // x
            if square.colliderect(wall) or square.colliderect(door):
                square.x += PUSH_BACk
        if keys_pressed[pygame.K_d] and square.x  + square.width < WIDTH: #Right
            square.x += VEL // x
            if square.colliderect(wall) or square.colliderect(door):
                square.x -= PUSH_BACk


def button_func(square, button, door, exi):
    for i in button:
        if square.colliderect(i):
            button.remove(i)
            for p in door:
                p.y -= p.y

            print('workS')


    if square.colliderect(exi):
        pygame.event.post(pygame.event.Event(NEXT_LEVEL))


def next_level():
    pygame.event.post





        





def game():
    air_time = 10
    square = pygame.Rect(W, H, 50, 50)
    wall = [pygame.Rect(W-60 ,H + 60, 50, 50), pygame.Rect(70, 30, 450, 300), pygame.Rect(WIDTH - 50, 0, 100 , HEIGHT), pygame.Rect(W-100 ,H + 150, 300, 50)]
    button = [pygame.Rect(W, H - 100, 30, 30), ]
    door = [pygame.Rect(W + 600, H//2, 200, 300), ]
    for o in door:
        exi = pygame.Rect(o.x + (o.x//2) , o.y+ (o.y), 40, 40)
        #DOING DOOR AND NEXT LEVEL

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                #MOVE THIS FOR QUIT
                pygame.quit()


        keys_pressed = pygame.key.get_pressed()
        x = len(wall)
        for y in door:
            for i in wall:
                movement(keys_pressed, square, i, x, y)  
        display(square, wall, button, door, exi)
        button_func(square ,button, door, exi)

        if event.type == NEXT_LEVEL:
            print('wOrks')

if __name__ == "__main__":
    game()

#I wanna make like physics and collisions, bouncec backs and teleportation? We'll see. puzzel game it shall be?
#Camera or room based?

