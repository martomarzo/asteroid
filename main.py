
import pygame
from constants import * 
from player import *
from asteroid import *
from asteroidfield import *




def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    
    clock= pygame.time.Clock()
    dt = 0
    
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")    
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids,updatable,drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (updatable,drawable,shots)
    
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2, PLAYER_RADIUS)
    asteroid_field = AsteroidField()
    

    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill(color = (0,0,0))
        
        dt=clock.tick_busy_loop(60)/1000
        
        for item in updatable:
            item.update(dt)
        for item in asteroids:
            if item.collision(player) == True:
                print("Game Over!")
                raise SystemExit 
            else:
                pass
        for item in drawable:
            item.draw(screen)        
        
        pygame.display.flip()
        clock.tick(60)            
        
        
        
    
    
if __name__ == "__main__":
    main()
    

