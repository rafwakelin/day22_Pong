from turtle import Screen
from items import Paddle, Ball, Score, set_screen

# Creates the screen
screen = Screen()
screen.setup(width=1050, height=650)
screen.bgcolor("black")
screen.title("Pong!")

# Draws the court on the screen
screen.tracer(0)
set_screen()

# Creates the players paddles, the ball, and scoreboard
r_paddle = Paddle((450, 0))
l_paddle = Paddle((-450, 0))
ball = Ball()
r_score = Score((100, 200))
l_score = Score((-100, 200))

# Listens to the keyboard entries to control the players paddles
screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")

# Unfreezes the animations after the screen is created
game_is_on = True
while game_is_on:
    screen.update()

    # Gets the ball to move on the screen
    ball.move()

    # Detect collision with the wall
    if ball.ycor() > 270 or ball.ycor() < -270:
        ball.bounce_y_axis()

    # Detect collision with the right paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 420:
        ball.bounce_x_axis()

    # Detect collision with the left paddle
    if ball.distance(l_paddle) < 40 and ball.xcor() < -420:
        ball.bounce_x_axis()

    # Keeps track of score and resets the ball
    if ball.xcor() > 520:
        l_score.new_score()
        ball.reset_position()

    if ball.xcor() < -520:
        r_score.new_score()
        ball.reset_position()

screen.exitonclick()
