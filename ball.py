from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("white")
        self.movement_value_x = 10
        self.movement_value_y = 10
        self.move_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.movement_value_x
        new_y = self.ycor() + self.movement_value_y
        self.goto(new_x, new_y)

    def bounce(self):
        self.movement_value_y = -self.movement_value_y

    def paddle_bounce(self):
        self.movement_value_x = -self.movement_value_x
        self.move_speed *= 0.5

    def ball_reset(self, winner):
        self.move_speed = 0.1

        self.goto(0, 0)

        if winner == "right":
            self.movement_value_y = -10
            self.movement_value_x = -10

        if winner == "left":
            self.movement_value_x = 10
            self.movement_value_y = 10



