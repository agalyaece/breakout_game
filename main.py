import time
import turtle as t
from paddle import Paddle
from ball import Ball
from bricks import Bricks
from scoreboard import Scoreboard
from ui import UI


screen = t.Screen()
screen.setup(width=1200, height=600)
screen.bgcolor("black")
screen.title("The Breakout Game")
screen.tracer(0)

ui = UI()
ui.header()
score = Scoreboard(lives=2)

paddle = Paddle()
ball = Ball()
bricks = Bricks()

game_is_on = True
game_paused = False
def pause_game():
    global game_paused
    if game_paused:
        game_paused=False
    else:
        game_paused = True
    

screen.listen()
screen.onkey(fun=paddle.move_left, key="Left")
screen.onkey(fun=paddle.move_right, key="Right")
screen.onkey(fun=pause_game, key="space")

def check_collisions_with_wall():
    global ball, score, game_is_on, ui
    if ball.xcor() > 580 or ball.xcor() < -570:
        ball.bounce(x_bounce=True, y_bounce=False)
        return
    if ball.ycor() > 280:
        ball.bounce(x_bounce=False, y_bounce=True)
        return
    if ball.ycor() < -270:
        ball.reset_ball()
        score.decrease_lives()
        if score.lives == 0:
            score.reset_score()
            game_is_on=False
            ui.game_over(win=False)
            return
        ui.change_color()
        return


def check_collisions_with_paddle():
    global ball, paddle

    paddle_x = paddle.xcor()
    ball_x = ball.xcor()

    if ball.distance(paddle) < 110 and ball.ycor()<-250:
        if paddle_x>0:
            if ball_x>paddle_x:
                ball.bounce(x_bounce=True, y_bounce=True)
                return
            else:
                ball.bounce(x_bounce=False, y_bounce=True)
                return
        elif paddle_x<0:
            if ball_x<paddle_x:
                ball.bounce(x_bounce=True, y_bounce=True)
                return
            else:
                ball.bounce(x_bounce=False,y_bounce=True)
                return
        else:
            if ball_x> paddle_x:
                ball.bounce(x_bounce=True, y_bounce=True)
                return
            elif ball_x < paddle_x:
                ball.bounce(x_bounce=True, y_bounce=True)
                return
            else:
                ball.bounce(x_bounce=False, y_bounce=True)
                return


def check_collisions_with_bricks():
    global bricks, ball, score
    for brick in bricks.bricks:
        if ball.distance(brick) < 40:
            score.increase_score()
            brick.quantity -= 1
            if brick.quantity == 0:
                brick.clear()
                brick.goto(3000, 3000)
                bricks.bricks.remove(brick)
            if ball.xcor() < brick.left_wall:
                ball.bounce(x_bounce=True, y_bounce=False)
            elif ball.xcor() > brick.right_wall:
                ball.bounce(x_bounce=True, y_bounce=True)
            elif ball.ycor() > brick.upper_wall:
                ball.bounce(x_bounce=False, y_bounce=True)
            elif ball.ycor() < brick.bottom_wall:
                ball.bounce(x_bounce=False, y_bounce=True)


while game_is_on:
    if not pause_game():
        screen.update()
        time.sleep(0.1)
        ball.move()
        check_collisions_with_wall()
        check_collisions_with_paddle()
        check_collisions_with_bricks()
        if len(bricks.bricks) == 0:
            ui.game_over(win=True)
            break

    else:
        ui.paused_status()

t.mainloop()
