import pygame
import random

pygame.init()

clock = pygame.time.Clock()

v = 0
ease = 0.1
maximum = 5
target = 0

pygame.display.set_caption("Car Game")
screen = pygame.display.set_mode((1280, 720))
running = True
carx = 640
cary = 600
car1 = pygame.image.load("car1.png")
car1 = pygame.transform.scale(car1, (50,100))
car1_rect = car1.get_rect()
#Enemy Car Settings---
maxy = 730
miny = -500
maxx = 700
minx = 500
#---------------------

car2 = pygame.image.load("car2.png")
car2 = pygame.transform.scale(car2, (50,100))



bg = pygame.image.load("bg.png").convert()
bgy = 0
scroll = 8
carscroll = 3

car2_rect = car2.get_rect()
car2_rect.y = random.randint(miny, 50)
car2_rect.x = random.randint(minx, maxx)

font = pygame.font.Font("Tomorrow-Regular.ttf", 50)

while running:
        
    text = font.render("Intense Car Game", True, (0,100,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    
    bgy += scroll
    car2_rect.y += carscroll

    if bgy >= 720:
        bgy -= 720

    if car2_rect.y > 730:
        car2_rect.y = random.randint(miny, 50)
        car2_rect.x = random.randint(minx, maxx)

    screen.blit(bg, (0,bgy))
    screen.blit(bg, (0,bgy-720))
    screen.blit(car2, car2_rect)
    screen.blit(text, (20,20))

    car1_rect.x = carx
    car1_rect.y = cary  
    
    if car2_rect.colliderect(car1_rect):
        print("Collsion!")

    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT] or key[pygame.K_a]:
        target = -maximum
    elif key[pygame.K_RIGHT] or key[pygame.K_d]:
        target = maximum
    else:
        target = 0

    v += (target - v) * ease
    carx += v
    
    carx = max(490, min(carx, 730))

    screen.blit(car1, (carx,cary))
    pygame.display.flip()
    
    clock.tick(75)

pygame.quit()
