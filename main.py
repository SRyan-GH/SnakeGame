from turtle import Screen
from snake import Snake
from food import Food
import time
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake')
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

def play_game(play):
    """
    Main game loop for the snake game.

    This function continuously updates the snake's position, checks for collisions
    (with walls, food, or itself), and listens for user input to move the snake.

    Args:
        play (bool): A boolean that controls whether the game continues.
    """
    while play:
        snake.move()
        screen.update()
        time.sleep(0.1)

        # game ends if wall collision
        if snake.segments[0].xcor() >= 300 or snake.segments[0].xcor() <= -300:
            scoreboard.game_over()
            screen.update()
            time.sleep(1.5)
            scoreboard.reset_scoreboard()
            snake.reset_snake()
        elif snake.segments[0].ycor() >= 300 or snake.segments[0].ycor() <= -300:
            scoreboard.game_over()
            screen.update()
            time.sleep(1.5)
            scoreboard.reset_scoreboard()
            snake.reset_snake()

        # food collision
        if snake.segments[0].distance(food) <= 10:
            food.refresh()
            scoreboard.increase_score()
            snake.add_segment()

        # segment collision
        for segment in snake.segments[1:]:
            if snake.segments[0].distance(segment) < 10:
                scoreboard.game_over()
                screen.update()
                time.sleep(1.5)
                scoreboard.reset_scoreboard()
                snake.reset_snake()

        # key events
        screen.listen()
        screen.onkey(key='Up',fun=snake.move_up)
        screen.onkey(key='Down', fun=snake.move_down)
        screen.onkey(key='Left', fun=snake.move_left)
        screen.onkey(key='Right', fun=snake.move_right)


playing = True
play_game(playing)

screen.exitonclick()