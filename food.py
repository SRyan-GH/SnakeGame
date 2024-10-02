from turtle import Turtle
import random

class Food(Turtle):
    """
    A class to represent the food for the Snake game.

    Inherits from the Turtle class and creates a small blue food object that
    randomly appears on the screen.
    """
    def __init__(self):
        """
        Initializes the food object.

        Sets the shape, size, color, and speed of the food, then places it
        at a random location on the screen.
        """
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color('blue')
        self.speed('fastest')
        self.refresh()


    def refresh(self):
        """
        Moves the food to a new random location on the screen.

        The new position is a multiple of 20 to align with the grid-based movement of the snake.
        """
        randx = 20 * round(random.randint(-280, 280) / 20)
        randy = 20 * round(random.randint(-280, 280) / 20)
        self.goto(randx, randy)
