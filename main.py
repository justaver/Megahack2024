

class Intersection: 

    def __init__(self): 
        self.q1Count = 0
        self.q2Count = 0
        self.q3Count = 0
        self.q4Count = 0
        self.scramble = True
        self.q1toq2 = False
        self.q2toq3 = False
        self.q3toq4 = False
        self.q4toq1 = False

    def draw(self): 
        #draw based on active crosswalks
        return

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
        if((self.q1Count + self.q2Count + self.q3Count + self.q4Count) > THRESHOLD): 
            

            
            

        


