from Ball_class import Ball, ensemble_balls
import math
import csv
import main
import time


EPSILON = 0.05


class Table:
    def __init__(self, height, base, balls: list[Ball], friction):
        self.height = height
        self.base = base
        self.friction = friction
        self.balls = balls
        self.fields = ["Time", "Position_White", "Speed_White"]
        self.rows = []
        self.time = 0

    def reset(self):
        filename = "current_sim.csv"
        # opening the file with w+ mode truncates the file
        f = open(filename, "w+")
        f.close()
        with open(filename, "a", newline="") as file:
            csvwriter = csv.writer(file)
            csvwriter.writerow(self.fields)

    def step_and_write(self, info, filename="current_sim.csv"):

        with open(filename, "a", newline="") as file:
            self.rows = []
            # self.rows = tuple(([info], [0], [0]))
            # if self.friction <= EPSILON:
            #     while self.balls[0].collision_with_wall(self.base, self.height):
            #         self.rows.append(
            #             (self.time, self.balls[0].position, self.balls[0].speed)
            #         )
            #         self.balls[0].step(self.friction)
            #         self.time += 1

            # else:
            # while self.balls[0].ismobile(EPSILON):
            # self.rows.append(
            #     (self.time, self.balls[0].position, self.balls[0].speed)
            # )
            # self.balls[0].step(self.friction)
            # self.time += 1

            self.rows.append((info))
            csvwriter = csv.writer(file)
            csvwriter.writerows(self.rows)


table = Table(122, 214, ensemble_balls, 0)
table.reset()
