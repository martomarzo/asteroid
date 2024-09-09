from circleshape import *
from constants import * 

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x,y,radius)
        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(1, 1)
        
    def draw(self, screen):
        pygame.draw.circle(surface=screen, color= (255,255,255), center = (self.position.x,self.position.y), radius=self.radius, width=2) 
       
    def update(self, dt):
        self.position += self.velocity * dt
       
    
        
    

    