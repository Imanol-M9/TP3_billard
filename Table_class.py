from Ball_class import Ball, ensemble_balls, collision_dot, speed_ball, speed_p
import json
import math
import main
import time
import numpy as np


EPSILON = 0.05


class Table:
    def __init__(self, height, base, balls: list[Ball], friction):
        self.height = height
        self.base = base
        self.friction = friction
        self.balls = balls
        self.data = []
        self.time = 0

    def reset(self, filename="current_sim.json"):
        # opening the file with w+ mode truncates the file -__-
        with open(filename, "w") as f:
            json.dump({}, f)

    def step_and_write(self, info: tuple, filename="current_sim.json"):

        with open(filename, "r") as f:
            file = json.load(f)

        file[str(info[0])] = info[1:]
        with open(filename, "w") as f:
            json.dump(file, f, indent=1)
        self.data = file

    def collision_with_ball(self):
        for ball_1 in self.balls:
            for ball_2 in self.balls:
                print(ball_1, ball_2, "SSSSSSSSSSSSSSSS")

                if (
                    ensemble_balls[ball_1].speed[0] <= EPSILON
                    and ensemble_balls[ball_2].speed[1] <= EPSILON
                ):
                    print("bouge pas")
                elif ball_1.color == ball_2.color:
                    print("same balle")

                elif (
                    math.sqrt(
                        (ball_1.centre - ball_2.centre) ** 2
                        + (ball_1[1] - ball_2[1]) ** 2
                    )
                    >= ball.rayon + ball_2.rayon
                ):
                    print(f"{ball_1, ball_1.vitesse, ball_2}")
                else:
                    n = [
                        ball_2[0]
                        - ball_1[0]
                        / math.sqrt(
                            (ball_1[0] - ball_2[0]) ** 2 + (ball_1[1] - ball_2[1]) ** 2
                        ),
                        ball_2[1]
                        - ball_1[1]
                        / math.sqrt(
                            (ball_1[0] - ball_2[0]) ** 2 + (ball_1[1] - ball_2[1]) ** 2
                        ),
                    ]
                    topbottom = (
                        ball_1.rayon
                        + ball_2.rayon
                        - math.sqrt(
                            (ball_1[0] - ball_2[0]) ** 2 + (ball_1[1] - ball_2[1]) ** 2
                        )
                    )
                    v_rel = collision_dot(ball_1.speed - ball_2.speed, n)

                    ball_1.position = [
                        ball_1.position[0] - (topbottom / 2) * n[0],
                        ball_1.position[1] - (topbottom / 2) * n[1],
                    ]
                    ball_2.position = [
                        ball_2.position[0] + (topbottom / 2) * n[0],
                        ball_2.position[1] + (topbottom / 2) * n[1],
                    ]

                    ball_1.speed = speed_ball(ball_1, v_rel, n)

    def collision_bande(self):
        for ball in self.balls:
            if ensemble_balls[ball].norm == 0:
                None
            else:
                # print(ball, ensemble_balls[ball].centre(ensemble_balls[ball].position))
                # print(
                #     main.BORDURE + main.RAYON,
                #     main.BORDURE + main.LONGEUR - main.RAYON,
                #     main.BORDURE + main.HAUTEUR - main.RAYON,
                # )
                if (
                    main.LONGEUR-main.RAYON-main.BORDURE <= ensemble_balls[f"{ball}"].centre()[0]
                ):
                    print(
                        f"_________________collision___mur_droit_______________{ensemble_balls[f'{ball}']}"
                    )
                    # ensemble_balls[ball].position = (main.BORDURE,ensemble_balls[ball].position[1],main.BORDURE+main.RAYON,ensemble_balls[ball].position[3])
                    print("avant")
                    print(
                        math.degrees(ensemble_balls[f"{ball}"].angle),
                        ensemble_balls[f"{ball}"].norm,
                    )
                    ensemble_balls[f"{ball}"].speed = ensemble_balls[f"{ball}"].speed - 2 * np.dot(ensemble_balls[f"{ball}"].speed, np.array([1,0])) * np.array([1,0])
                    print(
                        math.degrees(ensemble_balls[f"{ball}"].angle),
                        ensemble_balls[f"{ball}"].norm,
                    )
                if ensemble_balls[f"{ball}"].centre()[0]<= main.BORDURE + main.RAYON:
                    ensemble_balls[f"{ball}"].speed = ensemble_balls[f"{ball}"].speed - 2 * np.dot(ensemble_balls[f"{ball}"].speed, np.array([-1,0])) * np.array([-1,0])
                    print(
                        f"_________________collision___mur_gauche_______________{ensemble_balls[f'{ball}']}"
                    )
                    print("avant")
                    print(
                        math.degrees(ensemble_balls[f"{ball}"].angle),
                        ensemble_balls[f"{ball}"].norm,
                    )
                    ensemble_balls[f"{ball}"].set_mouvement(
                        ensemble_balls[f"{ball}"].angle - 180,
                        ensemble_balls[f"{ball}"].norm,
                    )
                    print("apres")
                    print(
                        math.degrees(ensemble_balls[f"{ball}"].angle),
                        ensemble_balls[f"{ball}"].norm,
                    )
                    ensemble_balls[f"{ball}"].set_mouvement(
                        ensemble_balls[f"{ball}"].angle - 180,
                        ensemble_balls[f"{ball}"].norm,
                    )
                else:
                    return None


table = Table(122, 214, ensemble_balls, 0)
table.reset()


for ball in table.balls:
    print(ball)
