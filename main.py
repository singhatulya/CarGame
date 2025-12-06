def reset_game():
    global carx, v, score, over, msg, scoretime
    global car2_rect, scroll, carscroll, maximum

    carx = 640
    v = 0
    score = 0
    over = False
    msg = "Move Left and Right using Arrow Keys."

    scroll = 8
    carscroll = 3
    maximum = 5

    car2_rect.y = random.randint(miny, 50)
    car2_rect.x = random.randint(minx, maxx)

    scoretime = time.time()
