import pygame # type: ignore
import random
from circleshape import CircleShape
from constants import *


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        random_angle = random.uniform(20, 50)

        a = self.velocity.rotate(random_angle)
        b = self.velocity.rotate(-random_angle)

        new_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid.velocity = a * 1.2
        asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid.velocity = b * 1.2

        
        
        
        
        #self.velocity = self.velocity.rotate(random_angle)
        #self.radius =- ASTEROID_MIN_RADIUS
        #pygame.draw.circle(screen, "white", self.position, self.radius, 2)
                
        #new_asteroid1 = new_asteroid1.Asteroid(self.position, self.radius - ASTEROID_MIN_RADIUS)
        #new_asteroid1.velocity = self.velocity.rotate(random_angle)
        #new_asteroid1.draw()
        #new_asteroid2 = new_asteroid2.Asteroid
        #new_asteroid2.velocity = self.velocity.rotate(-random_angle)
        #new_asteroid2.radius = self.radius - ASTEROID_MIN_RADIUS
        #new_asteroid2.draw()

        
        

