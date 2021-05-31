import turtle
wn = turtle.Screen()
wn.title("pong by 68,64")
wn.tracer(0)
wn.setup(width=800, height=600)
wn.bgcolor("black")
wn.listen()


# paddles

class paddles(turtle.Turtle):
    def __init__(self, xpos):
        super().__init__(shape="square")
        self.up()
        self.shapesize(3, 1)
        self.color("white")
        self.xpos = xpos
        self.goto(xpos, 0)

    def move_up(self):
        if self.ycor() < 280:
            self.goto(self.xcor(), self.ycor()+40)

    def move_down(self):
        if self.ycor() > -280:
            self.goto(self.xcor(), self.ycor()-40)


class ball(turtle.Turtle):
    def __init__(self, paddle1, paddle2, score):
        super().__init__(shape="circle")
        self.up()
        self.color("white")
        self.dx, self.dy = 0.1, 0.1
        self.paddle1 = paddles
        self.paddle2 = paddles
        self.score = score
        self.score1 = 0
        self.score2 = 0

    def Move(self):
        self.goto(self.xcor()+self.dx, self.ycor()+self.dy)

        # scoreplayer1
        if self.xcor() > 400:
            self.goto(0, 0)
            self.dx *= -1
            self.score1 += 1
            if self.score1 > 1 and self.score1 < 7:
                self.dx *= 1.5
            self.score.clear()
            self.score.write(
                f"player 1 : {self.score1}  player 2 : {self.score2}", align="center",)

        # scoreplayer2
        if self.xcor() < -400:
            self.goto(0, 0)
            self.dx *= -1
            self.score2 += 1
            if self.score2 > 1 and self.score2 < 7:
                self.dx *= 1.5
            self.score.clear()
            self.score.write(
                f"player 1 : {self.score1}  player 2 : {self.score2}", align="center",)

        if self.ycor() > 290 or self.ycor() < -290:
            self.dy *= -1

    def bounce_paddle(self):

        # Paddle2
        if self.xcor()-10 <= paddle2.xcor()-10 and self.xcor()+10 >= paddle2.xcor()-10 and self.dx > 0:
            if self.ycor()+10 >= paddle2.ycor()-40 and self.ycor()-10 <= paddle2.ycor()+40:
                self.dx *= -1

        # Paddle1 - ball towards paddle (dx negative or < 0),
        # between left (xcor()+10) side and middle (xcor()) of paddle,
        # between top (ycor()+50) and bottom (ycor()-50)
        if self.xcor()-10 <= paddle1.xcor()+10 and self.dx < 0:
            if self.ycor()-10 <= paddle1.ycor()+40 and self.ycor()+10 >= paddle1.ycor()-40:
                self.dx *= -1


class Scoreboard(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.up()
        self.hideturtle()
        self.color("white")
        self.goto(0, 250)
        self.write("player 1 : 0  player 2 : 0", align="center")


score = Scoreboard()
paddle1 = paddles(-350)
paddle2 = paddles(350)
ball = ball(paddle1, paddle2, score)

wn.onkeypress(paddle1.move_up, "w")
wn.onkeypress(paddle1.move_down, "s")
wn.onkeypress(paddle2.move_up, "Up")
wn.onkeypress(paddle2.move_down, "Down")


# main
while True:
    wn.update()
    ball.Move()
    ball.bounce_paddle()