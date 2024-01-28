from time import time
import pygame
COUNTTHRESHOLD = 1
TIMETHRESHOLD = 120 
crossImage = pygame.image.load("2024-01-28_00-38.png")
crossImage.set_colorkey((0, 0, 0))

class Intersection: 

    def __init__(self, screen): 
        self.q1Peds = list()
        self.q2Peds = list()
        self.q3Peds = list()
        self.q4Peds = list()
        self.scrambleEnable = True
        self.scramble = False
        self.q1toq2 = True
        self.q2toq3 = True
        self.q3toq4 = True
        self.q4toq1 = True
        self.q1toq3 = True
        self.q4toq2 = True
        self.pedSignal1 = False
        self.pedSignal2 = False
        self.pedSignal3 = False
        self.pedSignal4 = False
        self.auditorySignal1 = "Wait"
        self.auditorySignal2 = "Wait"
        self.auditorySignal3 = "Wait"
        self.auditorySignal4 = "Wait"
        self.lastSwitch = time()
        self.screen = screen 

    def draw(self): 
        pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(175, 550, 200, 100), 1)
        pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(1175, 550, 200, 100), 1)

        if(self.q4toq1):  
            pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(200, 200, 150, 30))
            pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(200, 250, 150, 30))
            pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(200, 300, 150, 30))
            pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(200, 350, 150, 30))
            pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(200, 400, 150, 30))
            pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(200, 450, 150, 30))
            pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(200, 500, 150, 30))
            pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(200, 675, 150, 30))
            pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(200, 725, 150, 30))
            pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(200, 775, 150, 30))
            pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(200, 825, 150, 30))
            pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(200, 875, 150, 30))
    
        if(self.q2toq3): 
            pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(1200, 200, 150, 30))
            pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(1200, 250, 150, 30))
            pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(1200, 300, 150, 30))
            pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(1200, 350, 150, 30))
            pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(1200, 400, 150, 30))
            pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(1200, 450, 150, 30))
            pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(1200, 500, 150, 30))
            pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(1200, 675, 150, 30))
            pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(1200, 725, 150, 30))
            pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(1200, 775, 150, 30))
            pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(1200, 825, 150, 30))
            pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(1200, 875, 150, 30))

        if(self.q1toq2): 
            pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(400, 50, 30, 150))
            pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(450, 50, 30, 150))
            pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(500, 50, 30, 150))
            pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(550, 50, 30, 150))
            pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(600, 50, 30, 150))
            pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(650, 50, 30, 150))
            pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(700, 50, 30, 150))
            pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(750, 50, 30, 150))
            pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(800, 50, 30, 150))
            pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(850, 50, 30, 150))
            pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(900, 50, 30, 150))
            pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(950, 50, 30, 150))
            pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(1000, 50, 30, 150))
            pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(1050, 50, 30, 150))
            pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(1100, 50, 30, 150))
            pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(1150, 50, 30, 150))


        if(self.q2toq3): 
            pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(400, 900, 30, 125))
            pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(450, 900, 30, 125))
            pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(500, 900, 30, 125))
            pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(550, 900, 30, 125))
            pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(600, 900, 30, 125))
            pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(650, 900, 30, 125))
            pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(700, 900, 30, 125))
            pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(750, 900, 30, 125))
            pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(800, 900, 30, 125))
            pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(850, 900, 30, 125))
            pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(900, 900, 30, 125))
            pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(950, 900, 30, 125))
            pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(1000, 900, 30, 125))
            pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(1050, 900, 30, 125))
            pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(1100, 900, 30, 125))
            pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(1150, 900, 30, 125))

        if(self.q3toq4): 
            self.screen.blit(pygame.transform.rotate(crossImage, -40), (350, 200))
            self.screen.blit(pygame.transform.rotate(crossImage, -40), (400, 240))
            self.screen.blit(pygame.transform.rotate(crossImage, -40), (450, 280))
            self.screen.blit(pygame.transform.rotate(crossImage, -40), (500, 320))
            self.screen.blit(pygame.transform.rotate(crossImage, -40), (550, 360))
            self.screen.blit(pygame.transform.rotate(crossImage, -40), (600, 400))
            self.screen.blit(pygame.transform.rotate(crossImage, -40), (650, 440))
            self.screen.blit(pygame.transform.rotate(crossImage, -40), (700, 480))
            self.screen.blit(pygame.transform.rotate(crossImage, -40), (750, 520))
            self.screen.blit(pygame.transform.rotate(crossImage, -40), (800, 560))
            self.screen.blit(pygame.transform.rotate(crossImage, -40), (850, 600))
            self.screen.blit(pygame.transform.rotate(crossImage, -40), (900, 640))
            self.screen.blit(pygame.transform.rotate(crossImage, -40), (950, 680))
            self.screen.blit(pygame.transform.rotate(crossImage, -40), (1000, 720))

        

    def update(self, q1=None, q2=None, q3=None, q4=None): 
        if(q1):
            self.q1Count += 1
        if(q2): 
            self.q2Count += 1
        if(q3): 
            self.q3Count += 1
        if(q4): 
            self.q4Count += 1
    
    def eval(self): 
        temp = [self.q1Count, self.q2Count, self.q3Count, self.q4Count]
        if(((self.q1Count + self.q2Count + self.q3Count + self.q4Count) > COUNTTHRESHOLD) or ((time() - self.lastSwitch) > TIMETHRESHOLD)): 
            thresh = max(temp)/2
            if((self.q1Count >= thresh) and (self.q2Count >= thresh) and (self.q3Count >= thresh) and (self.q4Count >= thresh)): 
                self.scramble = True
            else: 
                return
                    



