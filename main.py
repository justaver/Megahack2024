from pedestrian import Pedestrian
from intersection import Intersection
import pygame



class Simulation: 
    def __init__(self): 
        self.FPS = 1
        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((1920, 1080))
        self.pedestrianList = list()
        pygame.event.set_allowed([
            pygame.QUIT, 
            pygame.KEYDOWN
        ])
        self.intersection = Intersection(self.screen)
        
    def loop(self):  
        self.screen.fill("black")
        while True: 
            keys = pygame.key.get_pressed()
            for event in pygame.event.get(): 
                if(event.type == pygame.QUIT): 
                    return
                if(keys[pygame.K_SPACE]): 
                    self.pedestrianList.append(Pedestrian())
                    print(self.pedestrianList)
            self.intersection.draw()
            pygame.display.flip()
            pygame.display.update()
            self.clock.tick(self.FPS)
       

if __name__ == "__main__": 
    simulation = Simulation()
    simulation.loop()

