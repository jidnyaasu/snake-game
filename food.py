import time
from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("red")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        rand_list = [x for x in range(-260, 280, 20)]
        random_x = random.choice(rand_list)
        random_y = random.choice(rand_list)
        self.goto(random_x, random_y)
        # self.blink()

    def hide(self):
        self.hideturtle()

    def show(self):
        self.showturtle()
