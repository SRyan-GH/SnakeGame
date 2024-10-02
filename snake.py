from turtle import Turtle

class Snake:
    """
    A class to represent the snake in the Snake game.

    Manages the snake's segments, movement, and controls for changing direction.
    """

    def __init__(self):
        """
        Initializes the snake object.

        Creates an initial snake with three segments and sets up its movement behavior.
        """
        self.segments = []
        self.create_snake()


    def new_segment(self, position):
        """
        Adds a new segment to the snake at the specified position.

        Args:
            position (tuple): The (x, y) coordinates where the new segment will be placed.
        """
        new_turtle = Turtle()
        new_turtle.shape('square')
        new_turtle.color('white')
        new_turtle.penup()
        new_turtle.goto(position)
        self.segments.append(new_turtle)


    def add_segment(self):
        """
        Adds a new segment to the end of the snake.

        The new segment is added at the position of the last segment.
        """
        self.new_segment(self.segments[-1].position())



    def create_snake(self):
        """
        Creates the initial three-segment snake.

        Each segment is placed 20 units apart horizontally.
        """
        for i in range(3):
            pos = (-20 * i, 0)
            self.new_segment(pos)


    def move(self):
        """
        Moves the snake forward by moving each segment to the position of the previous segment.

        The head moves forward by 20 units.
        """
        for i in range(len(self.segments) - 1, 0, -1):
            forward_pos = self.segments[i - 1].position()
            self.segments[i].goto(forward_pos)
        self.segments[0].forward(20)


    def move_up(self):
        """
        Changes the snake's direction to upward.

        The snake can only move up if it's not currently moving down.
        """
        if self.segments[0].heading() != 270:
            self.segments[0].setheading(90)


    def move_down(self):
        """
        Changes the snake's direction to downward.

        The snake can only move down if it's not currently moving up.
        """
        if self.segments[0].heading() != 90:
            self.segments[0].setheading(270)


    def move_left(self):
        """
        Changes the snake's direction to left.

        The snake can only move left if it's not currently moving right.
        """
        if self.segments[0].heading() != 0:
            self.segments[0].setheading(180)


    def move_right(self):
        """
        Changes the snake's direction to right.

        The snake can only move right if it's not currently moving left.
        """
        if self.segments[0].heading() != 180:
            self.segments[0].setheading(0)

