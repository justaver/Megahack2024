from pedestrian import Pedestrian
from intersection import Intersection
import pygame

position1 = (0, 0)
position2 = (0, 0)
position3 = (0, 0)
position4 = (0, 0)

class Simulation: 
    def __init__(self): 
        self.FPS = 30
        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((1920, 1080))
        self.pedestrianList = list()
        pygame.event.set_allowed([
            pygame.QUIT, 
            pygame.KEYDOWN
        ])
        self.intersection = Intersection(self.screen)
        self.spawnElig = True
        
    def loop(self):  
        self.screen.fill("black")
        while True: 
            keys = pygame.key.get_pressed()
            self.intersection.draw()
            for event in pygame.event.get(): 
                if(event.type == pygame.QUIT): 
                    return
                
                if(self.spawnElig): 
                    if(keys[pygame.K_SPACE]): 
                        self.pedestrianList.append(Pedestrian())
                        self.spawnElig = False
                        #print(self.pedestrianList[len(self.pedestrianList) -1].start)
                else: 
                    if(not keys[pygame.K_SPACE]): 
                        self.spawnElig = True

                for pedestrian in self.pedestrianList: 
                    if(pedestrian.start == 1): 
                        pygame.draw.circle(self.screen, (0,0,255), (300, 150), 15)
                    if(pedestrian.start == 2): 
                        pygame.draw.circle(self.screen, (0,0,255), (1250, 150), 15)
                    if(pedestrian.start == 3): 
                        pygame.draw.circle(self.screen, (0,0,255), (1250, 1000), 15)
                    if(pedestrian.start == 4): 
                        pygame.draw.circle(self.screen, (0,0,255), (300,1000), 15)

            pygame.display.flip()
            pygame.display.update()
            self.clock.tick(self.FPS)
       

if __name__ == "__main__": 
    simulation = Simulation()
    simulation.loop()

