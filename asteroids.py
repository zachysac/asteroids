import pygame
from constants import *
from circleshape import CircleShape

def Asteroid(CircleShape):
    def __init__(self,x,y,radius):
        super.__init__(x,y,ASTEROID_MIN_RADIUS)
    def draw(self,screen):
        pygame.draw.circle(screen,"white",(self.x,self.y),ASTEROID_MIN_RADIUS,2)
    def update(self,dt):
        self.velocity += self.velocity * dt