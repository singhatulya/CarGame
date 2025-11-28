import pygame

pygame.init()

screen = pygame.display.set_mode((1280, 720))
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    car1 = pygame.image.load("car1.png")
    car1 = pygame.transform.scale(car1, (50,100))
    carx = 640
    cary = 360
    screen.fill((0,255,50))

    screen.blit(car1, (carx,cary))
    pygame.display.update()

pygame.quit()
