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
        self.rayon = main.cfg["RAYON"]
        self.objet_canva = objet_canva

    def set_mouvement(self, angle: float, norm: float):
        self.angle = angle
        self.norm = norm
        self.speed = np.array(
            [
                np.cos(self.angle) * self.norm,
                np.sin(self.angle) * self.norm,
            ]
        )

    def set_position(self, coo: list):
        self.position = coo

    def set_position_par_centre(self, centre_donner):
        self.position = (
            centre_donner[0] - main.cfg["RAYON"],
            centre_donner[1] - main.cfg["RAYON"],
            centre_donner[0] + main.cfg["RAYON"],
            centre_donner[0] + main.cfg["RAYON"],
        )

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
        pmin = np.array(
            [
                main.cfg["BORDURE"] + main.cfg["RAYON"],
                main.cfg["BORDURE"] + main.cfg["RAYON"],
            ]
        )
        pmax = np.array(
            [
                main.cfg["LONGEUR"] - main.cfg["BORDURE"] - main.cfg["RAYON"],
                main.cfg["HAUTEUR"] - main.cfg["BORDURE"] - main.cfg["RAYON"],
            ]
        )
        if np.any(np.array(self.centre()) <= pmin) or np.any(
            np.array(self.centre()) >= pmax
        ):
            if np.array(self.centre())[0] <= pmin[0]:
                self.position = (
                    main.cfg["BORDURE"],
                    self.position[1],
                    main.cfg["BORDURE"] + 2 * main.cfg["RAYON"],
                    self.position[3],
                )
                n = np.array([1, 0])
                self.speed = self.speed - 2 * np.dot(np.array(self.speed), n) * n

            if np.array(self.centre())[1] <= pmin[1]:
                self.position = (
                    self.position[0],
                    main.cfg["BORDURE"],
                    self.position[2],
                    main.cfg["BORDURE"] + 2 * main.cfg["RAYON"],
                )
                n = np.array([0, 1])
                self.speed = self.speed - 2 * np.dot(np.array(self.speed), n) * n

            if (self.centre())[0] >= pmax[0]:
                n = np.array([-1, 0])
                self.speed = self.speed - 2 * np.dot(np.array(self.speed), n) * n

            if np.array(self.centre())[1] >= pmax[1]:
                n = np.array([0, -1])
                self.speed = self.speed - 2 * np.dot(np.array(self.speed), n) * n

    def friction(self):

        if (-main.cfg["EPSILON"]) <= self.norm <= main.cfg["EPSILON"]:
            self.norm = 0
            self.speed = [0, 0]
        else:
            self.norm = self.norm * (1 - main.cfg["FROTEMENT"] * main.cfg["PAT"] / 100)
            self.speed[0] = self.speed[0] * (
                1 - main.cfg["FROTEMENT"] * main.cfg["PAT"] / 100
            )
            self.speed[1] = self.speed[1] * (
                1 - main.cfg["FROTEMENT"] * main.cfg["PAT"] / 100
            )

    def step(self, friction, step: float = 0.025):
        self.speed = self.speed * (1 - friction * step)

        self.position = self.position + self.speed * step

        self.norm = np.linalg.norm(self.speed)

    def coll_avec_ball(self, ensemble_a_chec):
        for ball_a_chec in ensemble_a_chec:
            autre_ball = ensemble_a_chec[ball_a_chec]
            if self == autre_ball:
                pass
            elif np.any(self.speed) == 0 and np.any(autre_ball.speed) == 0:
                pass
            # a ce moment il y a un collision entre deux ball
            elif (
                np.linalg.norm(np.array(self.centre()) - np.array(autre_ball.centre()))
                <= main.cfg["RAYON"] * 2
            ):
                n = (
                    np.array(autre_ball.centre()) - np.array(self.centre())
                ) / np.linalg.norm(
                    np.array(autre_ball.centre()) - np.array(self.centre())
                )
                chevauchement = 2 * main.cfg["RAYON"] - np.linalg.norm(
                    np.array(autre_ball.centre()) - np.array(self.centre())
                )
                self.set_position_par_centre = (
                    np.array(self.centre()) - (chevauchement / 2) * n
                )
                ensemble_balls[ball_a_chec].set_position_par_centre = (
                    np.array(autre_ball.centre()) + (chevauchement / 2) * n
                )
                n = (
                    np.array(autre_ball.centre()) - np.array(self.centre())
                ) / np.linalg.norm(
                    np.array(autre_ball.centre()) - np.array(self.centre())
                )
                v_rel = np.dot(self.speed - autre_ball.speed, n)

                if v_rel > 0:
                    self.speed = self.speed - v_rel * n
                    ensemble_balls[ball_a_chec].speed = autre_ball.speed + v_rel * n
                    self.norm = np.linalg.norm(self.speed)

    """ centre aurais pu etre un attribue mais j'ai la flem de la devoir penser a un endroit un la
    recalculer a chaque fram donc je le calcule, de tout facon c'est deux soustraction, c'est
    pas un gros truc a fair """

    def centre(self):
        return (
            self.position[2] - main.cfg["RAYON"],
            self.position[3] - main.cfg["RAYON"],
        )


white = Ball("White")
red = Ball("red")
purple = Ball("purple")
blue = Ball("blue")
orange = Ball("orange")
yellow = Ball("yellow")
black = Ball("black")
violet = Ball("violet")
teal = Ball("teal")
indianred4 = Ball("indianred4")
midnightblue = Ball("midnightblue")
darkgreen = Ball("darkgreen")
maroon = Ball("maroon")
indigo = Ball("indigo")
tan = Ball("tan")
olive = Ball("olive")

ensemble_balls = {
    "white": white,
    "red": red,
    "purple": purple,
    "blue": blue,
    "orange": orange,
    "yellow": yellow,
    "black": black,
    "violet": violet,
    "teal": teal,
    "indianred4": indianred4,
    "midnightblue": midnightblue,
    "darkgreen": darkgreen,
    "maroon": maroon,
    "indigo": indigo,
    "tan": tan,
    "olive": olive,
}
