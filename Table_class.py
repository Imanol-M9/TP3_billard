from Ball_class import Ball, ensemble_balls, collision_dot, speed_ball, speed_p
import json
import main
import time


EPSILON = 0.05


class Table:
    def __init__(self, height, base, balls: list[Ball], friction):
        self.height = height
        self.base = base
        self.friction = friction
        self.balls = balls
        self.data = {}
        self.time = 0

    def reset(self, filename = "current_sim.json"):
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
        for ball in self.balls:
            for p in self.balls:
                if (p.speed[0] <= EPSILON and p.speed[1] <= EPSILON) and (ball.speed[0] <= EPSILON and ball.speed[1] <= EPSILON):
                    pass            
                elif ball.color == p.color:
                    pass
                elif math.sqrt((ball[0] - p[0])**2 + (ball[1] - p[1])**2) >= ball.rayon + p.rayon:
                    pass
                else:
                    n = [
                        p[0] - ball[0] / math.sqrt((ball[0] - p[0])**2 + (ball[1] - p[1])**2),
                        p[1] - ball[1] / math.sqrt((ball[0] - p[0])**2 + (ball[1] - p[1])**2)
                    ]
                    topbottom = ball.rayon + p.rayon - math.sqrt((ball[0] - p[0])**2 + (ball[1] - p[1])**2)
                    v_rel = collision_dot(ball.speed - p.speed, n)

                    ball.position = [
                        ball.position[0] - (topbottom/2) * n[0],
                        ball.position[1] - (topbottom/2) * n[1]
                    ]
                    p.position = [
                        p.position[0] + (topbottom/2) * n[0],
                        p.position[1] + (topbottom/2) * n[1]
                    ]

                    ball.speed = speed_ball(ball, v_rel, n)

table = Table(122, 214, ensemble_balls, 0)
table.reset()
