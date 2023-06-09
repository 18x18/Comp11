import pygame, os

def puzzel():
    #PISKEL
    #Lets make a window first
    WIDTH, HEIGHT = 1600, 900
    W, H = WIDTH//2, HEIGHT//2
    pygame.display.set_caption('Game')
    WIN = pygame.display.set_mode((WIDTH, HEIGHT))
    FPS = 60
    VEL = 5
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    GREEN = (0, 255, 0)
    RED = (255, 0, 0)
    BLUE = (0, 0, 255)
    ORANGE = (255, 127, 0)
    PURPLE = (255, 0, 255)
    YELLOW = (255, 255, 0)
    TEAL = (0, 125, 125)
    BLT_SPED = VEL + 3






    square1 = pygame.image.load(os.path.join('square_PNG2.jpg'))
    square2 = pygame.transform.rotate(pygame.transform.scale(square1, (50, 50)),0)

    NEXT_LEVEL = pygame.USEREVENT + 1
    HURT = pygame.USEREVENT+1
    RETURN = pygame.USEREVENT + 1
    PUSH_BACk = VEL * 1.01


    #AFTER EXCRUCIATING EFFORT I HAVE PLACED A SQUARE ON A WHITE WINDOW!!!!!!!!! 9th may
    def display(square, wall, button, door, exi, bullets):
        WIN.fill(WHITE)
        for i in wall:
            pygame.draw.rect(WIN,RED, i)
        for i in door:
            pygame.draw.rect(WIN, BLUE, i)
        for i in button:
            pygame.draw.rect(WIN, GREEN, i)
        pygame.draw.rect(WIN,YELLOW, exi)
        for i in bullets:
            pygame.draw.rect(WIN, ORANGE, i)

        WIN.blit(square2, (square.x, square.y))




        pygame.display.update()

    def display2(square, wall, button, door, exi, bullets,):
        WIN.fill((0, 0, 0))
        pygame.draw.rect(WIN, YELLOW, exi)
        pygame.draw.rect(WIN, WHITE, square)
        for i in door:
            pygame.draw.rect(WIN, ORANGE, i)
        for i in wall:
            pygame.draw.rect(WIN,GREEN, i)
        for i in button:
            pygame.draw.rect(WIN, PURPLE, i)
        for i in bullets:
            pygame.draw.rect(WIN, TEAL, i)
    #   for i in trap:
    #        pygame.draw.rect(WIN, TEAL, i)




        pygame.display.update()




    #BASIC MOVEMENT!!!!!!!!!!!! 1;12 9th mayd
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

    def bllet(keys_pressed, bullet, square): # Bullets, breakable walls...
        if keys_pressed[pygame.K_LCTRL]:
            bullet.append(pygame.Rect(square.x + square.width, square.y + square.height, 20, 20))
        for i in bullet:
            if keys_pressed[pygame.K_w]:
                i.y -= BLT_SPED
            elif keys_pressed[pygame.K_s]:
                i.y += BLT_SPED
            elif keys_pressed[pygame.K_a]:
                i.x -= BLT_SPED
            elif keys_pressed[pygame.K_d]:
                i.x += BLT_SPED
            else:
                i.y -= BLT_SPED
            if i.colliderect(square):
                square = pygame.Rect(square.x, square.y, square.width- 10, square.height- 10)
                VEL += 1
        pygame.display.update()




    def button_func(square, button, door, exi, w, wall):

        for i in button:
            if square.colliderect(i):
                button.remove(i)
                for p in door:
                    p.y -= p.y

    #    for o in trap:
    #       if square.colliderect(o):
    #          pygame.event.post(pygame.event.Event(HURT))


        if square.colliderect(exi):
            if w == 0:
                pygame.event.post(pygame.event.Event(NEXT_LEVEL))
    #       elif w > 0:
    #            pygame.event.post(pygame.event.Event(RETURN))

        left, right, middle = pygame.mouse.get_pressed()
    #    print(pygame.mouse.get_pos())

        for i in wall:
            if left:
                print('left')          
                if i.collidepoint(pygame.mouse.get_pos()):
                    print("Wall clicked on the Player")
                    wall.remove(i)
            if right:
                print('middle')
            if middle:
                print('right')
    #Maybe find a way to break up a wall into  parts so that it dodesn't destroy the whole thing. Hard stuff
                





    def leel2(square):
        left, right, middle = pygame.mouse.get_pressed()
        if square.collidepoint(pygame.mouse.get_pos()):
            if left:
                x = pygame.mouse.get_rel()
                if square.x + 50 >= pygame.mouse.get_pos()[0]:
                    y = 0 
                    while x != y:
                        y += 1
                        square.x += 1

                elif square.x <= pygame.mouse.get_pos()[0]:
                    y = 0
                    while x != y:
                        y += 1
                        square.x -= 1
                    
                elif square.y + 50 >= pygame.mouse.get_pos()[1]:
                    y = 0
                    while x!= y:
                        y += 1
                        square.y += 1
                
                elif square.y <= pygame.mouse.get_pos()[1]:
                    y = 0
                    while x!= y:
                        y += 1
                        square.y -= 1

    def bosss(square):
        if pygame.mouse.get_pressed()[0] == 1:
            print('monleu')



            





    def game():
        w = 0
        bullets =[]
        trap = []
        square = pygame.Rect(W, H, 50, 50)
        border = [pygame.Rect(0 + 50 ,HEIGHT - 100, WIDTH - 100, 50), pygame.Rect(0 + 50, 0 + 50, 50, HEIGHT- 100), pygame.Rect(0 + 50, 0 + 50, WIDTH - 100 , 50), pygame.Rect(WIDTH - 100, 0 + 50, 50, HEIGHT - 100)]
        wall= [pygame.Rect(W + W, H + H, 50, 50)] + border 
        door = [pygame.Rect(WIDTH - 500, H - (H//2), 400, 400) ]
        exi = pygame.Rect(1442 ,400, 40, 40)
            #DOING DOOR AND NEXT LEVEL
        button = [pygame.Rect(W, H - 100, 30, 30),] #pygame.Rect(exi.x + 100, exi.y + 100, 30, 30)]

        health = 5

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

            button_func(square ,button, door, exi, w, wall)

            if w == 0:
                display(square, wall, button, door, exi, bullets)


#            bllet(keys_pressed, bullets, square)

            if event.type == NEXT_LEVEL:
                w += 1
                for d in wall:
                    wall.remove(d)
                for i in border:
                    wall.append(i)
    #                wall =wall +  border


        #       for o in [pygame.Rect(W, 400, 40, 40)]:
        #            trap.append(o)
    #Gotta make it so that it doesn't reset the door each time

        #   if event.type == RETURN:
        #        w = 0
    #         for d in wall:
    #              wall.remove(d)
    #           for i in [pygame.Rect(0 + 50 ,HEIGHT - 100, WIDTH - 100, 50), pygame.Rect(0 + 50, 0 + 50, 50, HEIGHT- 100), pygame.Rect(0 + 50, 0 + 50, WIDTH - 100 , 50), pygame.Rect(WIDTH - 100, 0 + 50, 50, HEIGHT - 100)]:
    #                wall.append(i)
    #                wall =wall +  border
    #         for d in door:
    #              door.remove(d)
    #           for i in [pygame.Rect(WIDTH - 500, H - (H//2), 400, 400)]:
    #                door.append(i)

#            bosss(square,)

    #     if event.type == HURT:
    #          health -= 1
    #           print(health)
    #            continue
#            leel2(square)

            if w >= 1:
                display2(square, wall, button, door, exi,  bullets, )
    #        print(square.x, square.y)

    #     pygame.init()
    #      start_time = pygame.time.get_ticks()
    #       if start_time and pygame.time.get_ticks() > 2000:
    #            exi = pygame.Rect(1442 ,400, 40, 40)


    if __name__ == "__main__":
        game()

    '''
    #I wanna make like physics and collisions, bouncec backs and teleportation? We'll see. puzzel game it shall be?
    #Camera or room based?
        #room based
    #What should i do now?
        #Make maps
        #new features
            #different keys, different uses
            #traps?
            #enemies?
            #Mouse movements (clicking and dragging and stuff.)
            
    #Damn, should i just do like a platformer?
    '''

#What game then?


puzzel()