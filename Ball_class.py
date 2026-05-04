import numpy as np

class Ball:
    def __init__(self, position:list[float]=[0, 0], angle:float=0, norm:float=0):
        self.position = position
        self.angle = np.radians(angle)
        self.norm = norm
        self.speed = np.array([np.cos(self.angle)*self.norm, np.sin(self.angle)*self.norm])
        self.rayon = 5
    
    def step(self, step:float):
        self.position = self.position + self.speed*step
