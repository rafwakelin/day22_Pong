from turtle import Screen, Turtle
from items import Paddle, Ball, Score

# Creates the screen
screen = Screen()
screen.setup(width=1050, height=650)
screen.bgcolor("black")
screen.title("Pong!")

# Draws the center line on the screen
screen.tracer(0)
line = Turtle()
line.hideturtle()
line.goto(0, 280)
line.pencolor("white")
line.pensize(5)
line.setheading(270)
for _ in range(28):
    line.pendown()
    line.forward(10)
    line.penup()
    line.forward(10)

line.penup()
line.setheading(0)
line.goto(-490, 290)
line.pendown()
line.goto(480, 290)

line.penup()
line.setheading(0)
line.goto(-490, -280)
line.pendown()
line.goto(480, -280)

line.penup()
line.setheading(270)
line.goto(480, 290)
line.pendown()
line.goto(480, -280)

line.penup()
line.setheading(270)
line.goto(-490, 290)
line.pendown()
line.goto(-490, -280)

line.penup()
line.shape("circle")
line.goto(0, 0)
line.shapesize(2)
line.color("white")
line.showturtle()

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
