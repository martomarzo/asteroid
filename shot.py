from circleshape import *
from constants import *

class Shot(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius,)
        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 1)
        self.rotation = 0
        
    def draw(self, screen):
        pygame.draw.circle(surface=screen, color= (255,255,255), center = (self.position.x,self.position.y), radius=self.radius, width=1) 
       
    def update(self, dt):
        self.position += self.velocity * dt
        
        
