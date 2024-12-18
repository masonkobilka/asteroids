import pygame
from circleshape import CircleShape
from constants import *
import random


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, 'white', self.position, self.radius, width = 2)

    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self):
        if self.radius <= ASTEROID_MIN_RADIUS:
            self.kill()
        if self.radius > ASTEROID_MIN_RADIUS:
            for i in range(2):
                asteroid = Asteroid(self.position[0], self.position[1], self.radius - ASTEROID_MIN_RADIUS)
                if i % 2 == 1:
                    asteroid.velocity = self.velocity.rotate(random.uniform(20, 50))
                else:
                    asteroid.velocity = -1 * (self.velocity.rotate(random.uniform(20, 50)))
                asteroid.velocity *= 1.2
        self.kill()