import pygame
import utils.vector as vector
import utils.body as body
from event import HandleEvent
from constants import *

screen = pygame.display.set_mode((Width, Height))
clock = pygame.time.Clock()
fps = 60
speed = 10

bodies = []

#parameters
Sun = body.Body(vector.Vector2(Width//2, Height//2), 100000, vector.Vector2(), "Sun", None, (255, 255, 0), 100)
Planet1 = body.Body(vector.Vector2(Width//2 + 200, Height//2  ), 1, vector.Vector2(0, 20), "Planet1", None, (0, 0, 255), 20, 300)
Planet2 = body.Body(vector.Vector2(Width//2 - 300, Height//2 ), 1, vector.Vector2(0, 15), "Planet2", None, (0, 255, 255), 20, 400)
Planet3 = body.Body(vector.Vector2(Width//2 - 380, Height//2 ), 1, vector.Vector2(0, 15), "Planet2", None, (25, 155, 255), 20, 400)
Planet4 = body.Body(vector.Vector2(Width//2 , Height//2 - 300 ), 1, vector.Vector2(20, 0), "Planet2", None, (220, 55, 55), 20, 400)


bodies.append(Sun)
bodies.append(Planet1)
bodies.append(Planet2)
bodies.append(Planet3)
bodies.append(Planet4)



run = 1
while run == 1:
    screen.fill(backgroundColor)
    clock.tick(fps)
    delta_time = clock.tick(fps)/1000
    pygame.display.set_caption(f"Nbody Simulation (FrameRate : {int(clock.get_fps())})")
    run = HandleEvent()

    # For a correct approximation you can use time step instead of just a simple loop
    for _body in bodies:
        body.updateBody(_body, bodies)
        _body.update(delta_time * speed)
        _body.draw(screen)

    pygame.display.flip()

pygame.quit()
