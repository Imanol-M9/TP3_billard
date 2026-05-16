import numpy as np
import math
import main


class Ball:
    def __init__(
        self,
        color: str,
        position: list[float] = [0, 0, 0, 0],
        angle: float = 0,
        norm: float = 0,
        objet_canva=None,
    ):
        self.color = color
        self.position = position
        self.angle = np.radians(angle)
        self.norm = norm
        self.speed = np.array(
            [
                np.cos(self.angle) * self.norm,
                np.sin(self.angle) * self.norm,
            ]
        )
        self.rayon = main.RAYON
        self.objet_canva = objet_canva

    # def deplacement(self):
    #     None

    def set_mouvement(self, angle: float, norm: float):
        self.angle = angle
        self.norm = norm
        self.speed = [
            np.cos(self.angle) * self.norm,
            np.sin(self.angle) * self.norm,
        ]

    def set_position(self, coo: list):
        self.position = coo

    def set_position_mouvement(self):
        self.position = (
            self.position[0] + self.speed[0],
            self.position[1] + self.speed[1],
            self.position[2] + self.speed[0],
            self.position[3] + self.speed[1],
        )

    def set_canva(self, objet_can):
        self.objet_canva = objet_can

    def collision_with_wall(self):
        pmin = np.array([main.BORDURE + main.RAYON, main.BORDURE + main.RAYON])
        pmax = np.array(
            [
                main.LONGEUR - main.BORDURE - main.RAYON,
                main.HAUTEUR - main.BORDURE - main.RAYON,
            ]
        )
        # print(f"pmin{pmin}, pmax{pmax}      ball:{np.array(self.centre())}")
        if np.any(np.array(self.centre()) <= pmin) or np.any(
            np.array(self.centre()) >= pmax
        ):
            # self.angle = -(180-self.angle)
            print("_________________Collision avec le mur___________________")
            # print(f"centre{np.array(self.centre())[0]}")
            # print(f"ex info ban {pmin}")
            if np.array(self.centre())[0] <= pmin[0]:
                print("coll a gauche")
                self.position = (
                    50,
                    self.position[1],
                    50 + 2 * main.RAYON,
                    self.position[3],
                )
                n = np.array([1, 0])
                self.speed = self.speed - 2 * np.dot(np.array(self.speed), n) * n

            if np.array(self.centre())[1] <= pmin[1]:
                print("coll haut")
                self.position = (
                    self.position[0],
                    50,
                    self.position[2],
                    50 + 2 * main.RAYON,
                )
                n = np.array([0, 1])
                self.speed = self.speed - 2 * np.dot(np.array(self.speed), n) * n

            if (self.centre())[0] >= pmax[0]:
                print("coll a droit")
                n = np.array([-1, 0])
                self.speed = self.speed - 2 * np.dot(np.array(self.speed), n) * n

            if np.array(self.centre())[1] >= pmax[1]:
                print("coll bas")
                n = np.array([0, -1])
                self.speed = self.speed - 2 * np.dot(np.array(self.speed), n) * n

    # def ismobile(self, epsilon):
    #     if math.sqrt(self.speed[0] ** 2 + self.speed[1] ** 2) >= epsilon:
    #         return True
    #     else:
    #         return False

    # def speed_shift(self, Z: str):
    #     match Z:
    #         case "x" | "X":
    #             self.speed[0] *= -1
    #         case "y" | "Y":
    #             self.speed[1] *= 1
    #         case _:
    #             print(
    #                 "Erreur de Changement de vitesse: La vitesse n'a pas été proprement changé."
    #             )

    def next_step(self):
        # print(n)
        # print((np.array([-main.EPSILON, -main.EPSILON])))
        # print((np.array([main.EPSILON, main.EPSILON])))

        self.collision_with_wall()
        # print("norm avant sep",self.norm)
        if (-main.EPSILON) <= self.norm <= main.EPSILON:
            print("zero")
            self.norm = 0
            self.speed[0] = 0
        else:
            self.norm = self.norm * (1 - main.FROTEMENT * main.PAT / 100)
            self.speed[0] = self.speed[0] * (1 - main.FROTEMENT * main.PAT / 100)
            self.speed[1] = self.speed[1] * (1 - main.FROTEMENT * main.PAT / 100)

    def step(self, friction, step: float = 0.025):
        self.speed = self.speed * (1 - friction * step)

        self.position = self.position + self.speed * step

        self.norm = np.linalg.norm(self.speed)

    def centre(self):
        return (
            self.position[2] - main.RAYON,
            self.position[3] - main.RAYON,
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


white = Ball("White")
red = Ball("red")
purple = Ball("purple")
blue = Ball("blue")
orange = Ball("orange")
yellow = Ball("yellow")
black = Ball("black")


# ensemble_balls = {
#     "white": white,
#     "red": red,
#     "purple": purple,
#     "blue": blue,
#     "orange": orange,
#     "yellow": yellow,
#     "black": black,
# }
ensemble_balls = {
    "white": white,
    # "red": red,
}
