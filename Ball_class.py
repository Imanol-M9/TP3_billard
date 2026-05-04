import numpy as np

class Ball:
    def __init__(self, color:str, position:list[float]=[0, 0], angle:float=0, norm:float=0, friction:float = 0):
        self.color = color
        self.position = position
        self.angle = np.radians(angle)
        self.norm = norm
        self.speed = np.array([np.cos(self.angle)*self.norm, np.sin(self.angle)*self.norm])
        self.rayon = 5
        self.friction = friction
    
    def collision_with_wall(self, base, height):
        pmin = np.array([[self.rayon, self.rayon]])
        pmax = np.array([[base - self.rayon, height - self.rayon]])

        if np.any(self.position <= pmin) or np.any(self.position >= pmax):
            print("Collision avec le mur")
            return False
        return True

    def speed_shift(self, Z: str):
        match Z:
            case "x"|"X":
                self.speed[0,0] *= -1
            case "y"|"Y":
                self.speed[0,1] *= 1
            case _:
                print("Erreur de Changement de vitesse: La vitesse n'a pas été proprement changé.")
    
    
    def step(self, step:float):
        self.speed = self.speed * (1 - self.friction * step)
        
        self.position = self.position + self.speed*step
