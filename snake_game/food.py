from turtle import Turtle
import random
from typing import Any

# food class: setting up dimensions/attributes, then random spawn locations for when snake dies/resets.
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("YELLOW")
        self.penup()
        self.shapesize(stretch_len=1, stretch_wid=1)
        self.speed("fastest")
        self.refresh()
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)
    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)