from turtle import Turtle


MOVE_DISTANCE = 10
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.goto(0, -240)
        self.x_move_dist = MOVE_DISTANCE
        self.y_move_dist = MOVE_DISTANCE


    def move(self):
        new_x = self.xcor()+self.x_move_dist
        new_y = self.ycor()+self.y_move_dist

        self.goto(new_x, new_y)

    def bounce(self, x_bounce, y_bounce):
        if x_bounce:
            self.x_move_dist *= -1
        if y_bounce:
            self.y_move_dist *= -1

    def reset_ball(self):
        self.goto(0, -240)
        self.y_move_dist = 10

