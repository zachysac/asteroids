#player class that inherits CircleShape
from circleshape import CircleShape
from constants import PLAYER_RADIUS
class Player(CircleShape):
    def __init__(self,x,y):
        self.x = x
        self.y = y
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