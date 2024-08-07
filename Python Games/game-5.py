import turtle
import os

# Set up the screen
window = turtle.Screen()
window.title("Brick Breaker Game")
window.bgcolor("black")
window.setup(width=800, height=600)
window.tracer(0)

# Score
score = 0

# Paddle
paddle = turtle.Turtle()
paddle.speed(1)
paddle.shape("square")
paddle.color("white")
paddle.shapesize(stretch_wid=1, stretch_len=5)
paddle.penup()
paddle.goto(0, -250)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("red")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.3  # Increased speed
ball.dy = -0.3  # Increased speed

# Bricks
bricks = []

for i in range(6):
    for j in range(7):
        brick = turtle.Turtle()
        brick.speed(1)
        brick.shape("square")
        brick.color("blue")
        brick.shapesize(stretch_wid=1, stretch_len=2)
        brick.penup()
        brick.goto(-290 + j * 100, 250 - i * 30)
        bricks.append(brick)

# Pen
pen = turtle.Turtle()
pen.speed(1)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0", align="center", font=("Courier", 24, "normal"))

# Function to move the paddle left and right
def paddle_left():
    x = paddle.xcor()
    x -= 20
    if x < -350:
        x = -350
    paddle.setx(x)

def paddle_right():
    x = paddle.xcor()
    x += 20
    if x > 350:
        x = 350
    paddle.setx(x)

# Keyboard bindings
window.listen()
window.onkeypress(paddle_left, "Left")
window.onkeypress(paddle_right, "Right")

# Main game loop
while True:
    window.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking
    if ball.xcor() > 390:
        ball.setx(390)
        ball.dx *= -1

    if ball.xcor() < -390:
        ball.setx(-390)
        ball.dx *= -1

    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.goto(0, 0)
        ball.dy *= -1
        score -= 1
        pen.clear()
        pen.write("Score: {}".format(score), align="center", font=("Courier", 24, "normal"))

    # Paddle and ball collisions
    if (ball.xcor() > paddle.xcor() - 50 and ball.xcor() < paddle.xcor() + 50) and (ball.ycor() < paddle.ycor() + 10 and ball.ycor() > paddle.ycor() - 10):
        ball.sety(-240)
        ball.dy *= -1

    # Ball and brick collisions
    for brick in bricks:
        if (ball.xcor() > brick.xcor() - 50 and ball.xcor() < brick.xcor() + 50) and (ball.ycor() > brick.ycor() - 10 and ball.ycor() < brick.ycor() + 10):
            ball.dy *= -1
            brick.goto(1000, 1000)  # Move the brick off screen
            bricks.remove(brick)
            score += 1
            pen.clear()
            pen.write("Score: {}".format(score), align="center", font=("Courier", 24, "normal"))
            break
