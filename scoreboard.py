from turtle import Turtle

class Scoreboard(Turtle):
    """
    A class to represent the scoreboard for the Snake game.

    Inherits from the Turtle class and manages the display of the current score
    and the 'Game Over' message.
    """
    def __init__(self):
        """
        Initializes the scoreboard.

        Sets the initial score to 0, positions the scoreboard at the top of the screen,
        and writes the initial score in white.
        """
        super().__init__()
        self.score = 0
        self.penup()
        self.goto(0, 270)
        self.color('white')
        self.write(f'Score: {self.score}', align='center', font=('Courier', 20, 'normal'))
        self.hideturtle()


    def increase_score(self):
        """
        Updates the score by clearing the previous score and incrementing by 1.

        Rewrites the updated score on the screen.
        """
        self.clear()
        self.score += 1
        self.write(f'Score: {self.score}', align='center', font=('Courier', 20, 'normal'))


    def game_over(self):
        """
        Displays the 'GAME OVER' message at the center of the screen.

        This is called when the player loses the game.
        """
        self.goto(0, 0)
        self.write('GAME OVER', align='center', font=('Courier', 20, 'normal'))


