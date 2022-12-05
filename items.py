from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 80, "normal")


# Paddles
class Paddle(Turtle):
    """Creates the paddles, takes as input a tuple of z and y locations and puts the paddles on these locations"""
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(position)

    def up(self):
        """Listens to keyboard entry and moves paddles up"""
        new_y = self.ycor() + 30
        self.goto(self.xcor(), new_y)

    def down(self):
        """Listens to keyboard entry and moves paddles down"""
        new_y = self.ycor() - 30
        self.goto(self.xcor(), new_y)


# Ball
class Ball(Turtle):
    """Creates the ball and puts it in the center of the court"""
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.goto(0, 0)
        self.xmove = 3.5
        self.ymove = 3.5
        self.move_speed = 0.1

    def move(self):
        """Moves the ball to a new location"""
        new_x = self.xcor() + self.xmove
        new_y = self.ycor() + self.ymove
        self.goto(new_x, new_y)

    def bounce_y_axis(self):
        """Bounces back when hits the wall"""
        self.ymove *= -1

    def bounce_x_axis(self):
        """Bounces back when hits the paddle"""
        self.xmove *= -1

    def reset_position(self):
        self.goto(0, 0)
        self.xmove *= -1


# Score
class Score(Turtle):
    def __init__(self, score_position):
        """Creates a score board"""
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.setposition(score_position)
        self.write(arg=f"{self.score}", align=ALIGNMENT, font=FONT)

    def new_score(self):
        """Once the paddle misses scoreboard gets updated"""
        self.score += 1
        self.clear()
        self.write(arg=f"{self.score}", align=ALIGNMENT, font=FONT)


# Screen
def set_screen():
    line = Turtle()
    line.hideturtle()
    line.goto(0, 280)
    line.pencolor("white")
    line.pensize(2)
    line.setheading(270)
    for _ in range(28):
        line.pendown()
        line.forward(10)
        line.penup()
        line.forward(10)

    line.pensize(4)
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
    line.shapesize(4)
    line.showturtle()
