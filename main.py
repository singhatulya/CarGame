import pygame

pygame.init()

clock = pygame.time.Clock()

v = 0
ease = 0.1
maximum = 5
target = 0

screen = pygame.display.set_mode((1280, 720))
running = True
carx = 640
cary = 600
car1 = pygame.image.load("car1.png")
car1 = pygame.transform.scale(car1, (50,100))
bg = pygame.image.load("bg.png").convert()

while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    
    screen.blit(bg, (0,-90))

    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT] or key[pygame.K_a]:
        target = -maximum
    elif key[pygame.K_RIGHT] or key[pygame.K_d]:
        target = maximum
    else:
        target = 0

    v += (target - v) * ease
    carx += v
    
    carx = max(480, min(carx, 750))

    screen.blit(car1, (carx,cary))
    pygame.display.flip()
    
    clock.tick(75)

pygame.quit()
