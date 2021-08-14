import pygame

def HandleEvent():
    running = 1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = 0
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_ESCAPE:
                running = 0
    return running
