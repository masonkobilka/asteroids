from circleshape import CircleShape
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED, SHOT_RADIUS, PLAYER_SHOOT_SPEED, PLAYER_SHOOT_COOLDOWN
import pygame

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shot_cooldown = 0

    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        points = self.triangle()
        pygame.draw.polygon(screen, 'white', points, width = 2)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def update(self, dt):
        self.shot_cooldown -= dt
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-1 * dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_d]:
            self.move(-1 * dt)
        if keys[pygame.K_SPACE]:
            self.shoot()

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self):
        if self.shot_cooldown <= 0:
            velocity = pygame.Vector2(0, 1).rotate(self.rotation)
            velocity *= PLAYER_SHOOT_SPEED
            Shot(self.position[0], self.position[1], SHOT_RADIUS, velocity)
            self.shot_cooldown = PLAYER_SHOOT_COOLDOWN


class Shot(CircleShape):
    def __init__(self, x, y, radius, velocity):
        super().__init__(x, y, radius)
        self.velocity = velocity

    def update(self, dt):
        self.position += self.velocity * dt

    def draw(self, screen):
        pygame.draw.circle(screen, 'white', self.position, self.radius, width = 2)