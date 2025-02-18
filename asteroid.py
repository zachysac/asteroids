import pygame
import random
from circleshape import CircleShape
from constants import *


class Asteroid(CircleShape):
    def __init__(self,x,y,radius):
        super().__init__(x,y,radius)

    def draw(self,screen):
        pygame.draw.circle(screen,"white",self.position,self.radius,2)

    def update(self,dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            rand = random.uniform(20,50)
            new_vect_1 = pygame.math.Vector2.rotate(self.velocity,rand)
            new_vect_2 = pygame.math.Vector2.rotate(self.velocity,-rand)
            new_rad = self.radius - ASTEROID_MIN_RADIUS
            new_ast_1 = Asteroid(self.position.x,self.position.y,new_rad)
            new_ast_2 = Asteroid(self.position.x,self.position.y,new_rad)
            new_ast_1.velocity = new_vect_1 * 1.2
            new_ast_2.velocity = new_vect_2 * 1.2