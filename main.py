import pygame
import utils.vector as vector
import utils.body as body
from event import HandleEvent
from constants import *

screen = pygame.display.set_mode((Width, Height))
clock = pygame.time.Clock()
fps = 60

bodies = []

step = 0.05
speed = 10

#parameters
Sun = body.Body(vector.Vector2(Width//2, Height//2), 100000, vector.Vector2(), "Sun", None, (255, 255, 0), 100)

Planet1 = body.Body(position=vector.Vector2(Width//2 + 200, Height//2  ),
                    mass=1,
                    velocity=vector.Vector2(0, 25),
                    name="Planet1",
                    sprite=None,
                    color=(0, 0, 255),
                    radius=20,
                    history_limit=200)
Planet2 = body.Body(vector.Vector2(Width//2 - 300, Height//2 ), 1, vector.Vector2(0, 15), "Planet2", None, (0, 255, 255), 15, 200)
Planet3 = body.Body(vector.Vector2(Width//2 - 380, Height//2 ), 1, vector.Vector2(0, 15), "Planet2", None, (25, 155, 255), 20, 250)
Planet4 = body.Body(vector.Vector2(Width//2 + 400, Height//2  ), 2, vector.Vector2(0, 17), "Planet2", None, (220, 55, 55), 40, 400)

bodies.append(Sun)
bodies.append(Planet1)
bodies.append(Planet2)
bodies.append(Planet3)
bodies.append(Planet4)

last_ticks = 0; # previous milliseconds
count_ticks = 0

# 0 -> showTrail, 1 -> isDotted
events = [True, False]

run = 1
while run == 1:
    screen.fill(backgroundColor)
    clock.tick(fps)
    delta_time = clock.tick(fps)/1000
    pygame.display.set_caption(f"Nbody Simulation (FrameRate : {int(clock.get_fps())})")


    run = HandleEvent(events)
    showTrail = events[0]
    isDotted = events[1]

    # # Get the delta Time since the last frame update
    ticks        = pygame.time.get_ticks()
    ticksElapsed = ticks - last_ticks
    s_ticks    = ticksElapsed/1000
    last_ticks   = ticks

    count_ticks += s_ticks
    # For a correct approximation you can use time step instead of just a simple loop
    while count_ticks > step:
        for _body in bodies:
            _body.Calculate(bodies)
        for _body in bodies:
            _body.update(step * speed)
        count_ticks -= step
    for _body in bodies:
        _body.draw(screen, showTrail, isDotted)

    pygame.display.flip()

pygame.quit()
