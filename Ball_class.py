import numpy as np
import math

class Ball:
    def __init__(self, color:str, position:list[float]=[0, 0], angle:float=0, norm:float=0):
        self.color = color
        self.position = position
        self.angle = np.radians(angle)
        self.norm = norm
        self.speed = np.array([np.cos(self.angle)*self.norm, np.sin(self.angle)*self.norm])
        self.rayon = 5
    
    def collision_with_wall(self, base, height):
        pmin = np.array([[self.rayon, self.rayon]])
        pmax = np.array([[base - self.rayon, height - self.rayon]])

        if np.any(self.position <= pmin) or np.any(self.position >= pmax):
            #determiner quelle mur
            if self.position[0] + self.rayon >= base: #mur x+
                self.position[0] = base - self.rayon - 0.001
                n = np.array([-1,0])
            elif self.position[0] - self.rayon <= 0: #mur x-
                self.position[0] = 0 + self.rayon + 0.001
                n = np.array([1,0])
            elif self.position[1] + self.rayon >= height: #mur y+
                self.position[1] = height - self.rayon - 0.001
                n = np.array([0,-1])
            elif self.position[1] - self.rayon <= 0: #mur y-
                self.position[1] = 0 + self.rayon + 0.001
                n = np.array([0,1])
            
            self.speed = self.speed - 2 * np.dot(self.speed, n) * n
            
            
            
        
    
    def ismobile(self, epsilon):
        if math.sqrt(self.speed[0] **2 + self.speed[1] **2) >= epsilon:
            return True
        else:
            return False
        
        
        
        
            
    def speed_shift(self, Z: str):
        match Z:
            case "x"|"X":
                self.speed[0] *= -1
            case "y"|"Y":
                self.speed[1] *= -1
            case _:
                print("Erreur de Changement de vitesse: La vitesse n'a pas été proprement changé.")
    
    
    def step(self, friction, step:float= 0.025):
        self.speed = self.speed * (1 - friction * step)
        
        self.position = self.position + self.speed*step
