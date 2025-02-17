#import pygame
import pygame
#imports constants
from constants import *
#player class that inherits CircleShape
from circleshape import CircleShape
from shot import Shot
class Player(CircleShape):
    def __init__(self,x,y):
        super().__init__(x,y,PLAYER_RADIUS)
        self.rotation = 0
    
    # player visual shape (hitbox is circle)
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    #drawing player shape
    def draw(self,screen):
        pygame.draw.polygon(screen,"white",self.triangle(),2)
    #rotation degree calculator
    def rotate(self,rotation):
        self.rotation += (PLAYER_TURN_SPEED * rotation)
    #update rotation
    def update(self, dt):
        keys = pygame.key.get_pressed()
        #rotates counterclockwise
        if keys[pygame.K_a]:
            self.rotate(-dt)
        #rotates clockwise
        if keys[pygame.K_d]:
            self.rotate(dt)
        #moves forward
        if keys[pygame.K_w]:
            self.move(dt)
        #moves back
        if keys[pygame.K_s]:
            self.move(-dt)
        #shoots
        if keys[pygame.K_SPACE]:
            self.shoot()
    #moves player forward
    def move(self,dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt
    #creates a shot at the player position
    def shoot(self):
        shot = Shot(self.position.x, self.position.y)
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        shot.velocity = forward * PLAYER_SHOOT_SPEED