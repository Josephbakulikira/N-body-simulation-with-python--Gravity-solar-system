import pygame
import utils.vector as vector
from constants import *

def updateBody(current, bodies):
    current.acceleration = vector.Vector2()
    for body in bodies:
        if body == current:
            continue
        r = vector.GetDistance2D(current.position, body.position) # distance
        g_force = (current.mass * body.mass)/ pow(r, 2)
        acc = g_force / current.mass # acceleration a=f/m
        diff = body.position - current.position
        current.acceleration = current.acceleration + diff.setMagnitude(acc)


class Body:
    def __init__(self, position, mass, velocity, name="Default", sprite=None, color=(0, 0, 255), radius=20, history_limit=200):
        self.position = position
        self.mass = mass
        self.velocity = velocity
        self.acceleration = vector.Vector2()
        self.color = color
        self.name = name
        self.sprite = sprite
        self.radius = radius
        self.history = []
        self.history_limit = history_limit

    def update(self, dt):
        self.velocity = self.velocity + (self.acceleration * dt)
        self.position = self.position + (self.velocity * dt)

        if len(self.history) > self.history_limit:
            self.history.pop()
        if self.name != "Sun":
            self.history.insert(0, self.position.ParseToInt())

    def draw(self, screen):
        for i in range(len(self.history)):
            if i > 0:
                pygame.draw.line(screen, self.color, self.history[i-1],self.history[i], history_size)

        if self.sprite == None:
            pygame.draw.circle(screen, self.color, self.position.ParseToInt(), self.radius)
        else:
            print("there is a sprite")

    def __repr__(self):
        # debug
        return f"{self.name}-> position: {self.position}, velocity: {self.velocity}, acceleration: {self.acceleration}, mass: {self.mass}"
