import pygame, random

WIDTH, HEIGHT = 1600, 900
W, H = WIDTH//2, HEIGHT//2
FPS = 60
VEL = 10

works = print('works')

pygame.init()
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hello World")
WHITE = (255, 255, 255)
PURPLE = (125, 0, 255)
RED = (255, 0, 0)

def display(head, apple):
    WIN.fill(WHITE)
    pygame.draw.rect(WIN, PURPLE, head)
    pygame.draw.rect(WIN, RED, apple)
    works

    pygame.display.update()

def movement(keys_pressed, head):

    if keys_pressed[pygame.K_LEFT] and head.x - VEL > 0: # LEFT
        head.x -= VEL
                    #no out of bounds
    if keys_pressed[pygame.K_RIGHT] and head.x + VEL + head.width < WIDTH: # RIGHT
        head.x += VEL
    if keys_pressed[pygame.K_UP] and head.y - VEL : # UP
        head.y -= VEL
    if keys_pressed[pygame.K_DOWN] and head.y + VEL + head.height: # DOWN
        head.y += VEL
    print('worKs')

def eat(head, apple):
    for i in apple:
        if head.colliderect(i):
            apple.remove(i)
            apple.append(pygame.Rect(random.randint(0, W), random.randint(0, H), 30, 30))



def main():
    head = pygame.Rect(W, 400, 50, 50)
    apple = [pygame.Rect(random.randint(0, W), random.randint(0, H), 30, 30)]
    keys_pressed = pygame.key.get_pressed()
    

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                #MOVE THIS FOR QUIT
                pygame.quit()

            display(head, apple)
            movement(keys_pressed, head)
            eat(head, apple)

    pygame.quit()

if __name__ == "__main__":
    main()





