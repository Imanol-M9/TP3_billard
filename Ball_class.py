import numpy as np
import math
import main


class Ball:
    def __init__(
        self,
        color: str,
        position: list[float] = [0, 0],
        angle: float = 0,
        norm: float = 0
    ):
        self.color = color
        self.position = position
        self.angle = np.radians(angle)
        self.norm = norm
        self.speed = np.array(
            [np.cos(self.angle) * self.norm, np.sin(self.angle) * self.norm]
        )
        self.rayon = 5

    def set_mouvement(self, angle: float, norm: float):
        self.angle = angle
        self.norm = norm

    def collision_with_wall(self, base, height):
        pmin = np.array([[self.rayon, self.rayon]])
        pmax = np.array([[base - self.rayon, height - self.rayon]])

        if np.any(self.position <= pmin) or np.any(self.position >= pmax):
            print("Collision avec le mur")
            return False
        return True

    def ismobile(self, epsilon):
        if math.sqrt(self.speed[0] ** 2 + self.speed[1] ** 2) >= epsilon:
            return True
        else:
            return False

    def speed_shift(self, Z: str):
        match Z:
            case "x" | "X":
                self.speed[0] *= -1
            case "y" | "Y":
                self.speed[1] *= 1
            case _:
                print(
                    "Erreur de Changement de vitesse: La vitesse n'a pas été proprement changé."
                )

    def step(self, friction, step: float = 0.025):
        self.speed = self.speed * (1 - friction * step)

        self.position = self.position + self.speed * step

        self.norm = np.linalg.norm(self.speed)

    def centre(self, coordoner: tuple):
        return (
            coordoner[0] - main.RAYON,
            coordoner[1] - main.RAYON,
        )
def collision_dot(Delta_v, n):
    return np.dot(Delta_v, n)

def speed_ball(ball, v_rel, n):
    v1 = ball.speef
    if v_rel > 0:
        v1 = ball.speed - v_rel * n
    return v1

def speed_p(p, v_rel, n):
    v1 = p.speef
    if v_rel > 0:
        v1 = p.speed + v_rel * n
    return v1



white = Ball("White", [100, 100], 1, 1)
red = Ball("Red", [200, 200], 0, 0)

ensemble_balls = {
    "white" : white,
    "red" : red
}
