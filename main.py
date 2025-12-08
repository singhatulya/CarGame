import pygame
import random
import time
import os

pygame.init()

highscore_file = "high.txt"

clock = pygame.time.Clock()

v = 0
ease = 0.1
maximum = 5
target = 0
score = 0
over = False
msg = "Move Left and Right using Arrow Keys."

scoretime = time.time()

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
scoret = pygame.font.Font("Tomorrow-Regular.ttf", 30)
txt = pygame.font.Font("Tomorrow-Regular.ttf", 20)

def reset_game():
    global carx, v, score, over, msg, scoretime
    global car2_rect, scroll, carscroll, maximum

    carx = 640
    v = 0
    score = 0
    over = False 
    msg = "Move Left and Right using Arrow Keys."

    scroll = 8 + score // 5
    carscroll = 3 + score // 55
    maximum = 5

    car2_rect.y = random.randint(miny, 50)
    car2_rect.x = random.randint(minx, maxx)

    scoretime = time.time()

if os.path.exists(highscore_file):
    with open(highscore_file, "r") as f:
        try:
            highscore = int(f.read())
        except:
            highscore = 0
else:
    highscore = 0

while running:
        
    text = font.render("Intense Car Game", True, (0,100,0))
    score_text = scoret.render(f"Score: {score}", True, (0, 20, 0))
    txtm = txt.render(msg, True, (0,0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    if not over:
        scroll = 8 + score // 250
        carscroll = 3 + score // 200


    bgy += scroll
    car2_rect.y += carscroll

    current_time = time.time()

    if not over and current_time - scoretime >= 0.125:
        score += 1
        scoretime = current_time

    if bgy >= 720:
        bgy -= 720

    if car2_rect.y > 730:
        car2_rect.y = random.randint(miny, 50)
        car2_rect.x = random.randint(minx, maxx)

    

    car1_rect.x = carx
    car1_rect.y = cary  
    
    if car2_rect.colliderect(car1_rect) and not over:
        scroll = 0
        carscroll = 0
        maximum = 0
        over = True
        msg = "Game Over! Press R to Restart."

        if score > highscore:
            highscore = score
            with open(highscore_file, "w") as f:
                f.write(str(highscore))

    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT] or key[pygame.K_a]:
        target = -maximum
    elif key[pygame.K_RIGHT] or key[pygame.K_d]:
        target = maximum
    
    else:
        target = 0

    if key[pygame.K_r ]and over:
        reset_game()

    v += (target - v) * ease
    carx += v
    
    carx = max(490, min(carx, 730))

    

    screen.blit(bg, (0,bgy))
    screen.blit(bg, (0,bgy-720))
    screen.blit(car2, car2_rect)
    screen.blit(text, (20,20))
    screen.blit(score_text, (20, 100))
    screen.blit(car1, (carx,cary))
    screen.blit(txtm, (20, 140))
    high_text = scoret.render(f"High Score: {highscore}", True, (0, 20, 0))
    screen.blit(high_text, (20, 170))

    
    pygame.display.flip()
    
    clock.tick(75)

pygame.quit()
