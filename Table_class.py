from Ball_class import Ball
import math
import csv
#from interface import HAUTEUR, LONGEUR, BORDURE, RAYON


EPSILON = 0.05

class Table:
    def __init__(self, height, base, balls: list[Ball], friction):
        self.height = height
        self.base = base
        self.friction = friction
        self.balls = balls
    
    def step_and_write(self, filename="current_sim.csv"):
        fields = ["Time", "Position_White", "Speed_White"]
        rows = []
        time = 0

        with open(filename, "w", newline="") as file:
            

            if self.friction <= EPSILON:
                while self.balls[0].collision_with_wall(self.base, self.height):
                    rows.append((time, self.balls[0].position, self.balls[0].speed))
                    self.balls[0].step(self.friction)
                    time += 1

            else:
                while self.balls[0].ismobile(EPSILON):
                    rows.append((time, self.balls[0].position, self.balls[0].speed))
                    self.balls[0].step(self.friction)
                    time += 1

            
            rows.append((time, self.balls[0].position, self.balls[0].speed))
            csvwriter = csv.writer(file)
            csvwriter.writerow(fields)
            csvwriter.writerows(rows)









white = Ball("White", [100,100], 0, 5, 0)
table = Table(122, 214, [white], 0)
table.step_and_write()
