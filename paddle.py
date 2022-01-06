from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, x_cord):
        # enables use of the turtle class, inheritance
        super().__init__()
        self.penup()
        self.color("white")
        self.shape(name="square")
        self.goto(x_cord, 0)
        self.shapesize(stretch_wid=5, stretch_len=1)

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
