import pygame

def HandleEvent(events):
    running = 1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = 0
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_ESCAPE:
                running = 0
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_t: # show trail toggle
                events[0] = not events[0]
            if event.key == pygame.K_r:
                events[1] = not events[1] # trail is dotted toggle
            if event.key == pygame.K_SPACE:
                events[2] = not events[2] # pause & continue

    return running
