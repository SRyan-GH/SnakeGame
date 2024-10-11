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
        self.high_score = self.get_highscore()
        self.penup()
        self.goto(0, 270)
        self.color('white')
        self.update_scoreboard()
        self.hideturtle()


    @staticmethod
    def get_highscore():
        """
        Retrieves the current high score from the 'data.txt' file.

        Returns:
            int: The high score as an integer read from the file.
        """
        with open(file='data.txt') as data:
            return int(data.read())


    def update_highscore(self):
        """
        Updates the high score in the 'data.txt' file by writing the current `high_score` attribute value to the file.
        """
        with open(file='data.txt', mode='w') as data:
            data.write(str(self.high_score))


    def update_scoreboard(self):
        """
        Clears the current scoreboard and updates it with the current score and high score.
        This method writes a formatted string displaying the current score and high score.
        """
        self.clear()
        self.write(f'Score: {self.score} High Score: {self.high_score}', align='center', font=('Courier', 20, 'normal'))


    def increase_score(self):
        """
        Updates the score by clearing the previous score and incrementing by 1.

        Rewrites the updated score on the screen.
        """
        self.score += 1
        self.update_scoreboard()


    def reset_scoreboard(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.update_highscore()
        self.score = 0
        self.update_scoreboard()


    def game_over(self):
        """
        Displays the 'GAME OVER' message at the center of the screen.

        This is called when the player loses the game.
        """
        self.goto(0, 0)
        self.write('GAME OVER', align='center', font=('Courier', 20, 'normal'))
        self.goto(0, 270)


