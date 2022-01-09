# Simple Pong in python
# By @juan_glitch
# Based on the tutorial: https://www.youtube.com/watch?v=C6jJg9Zan7w&t

import os
import turtle

# Game Objects

class paddle(turtle.Turtle):
    def __init__(self, color, gotoX, gotoY, shapeW, shapeL):
        super().__init__()
        self.color(color)
        self.speed(0)
        self.shape('square')
        self.shapesize(stretch_wid=shapeW, stretch_len=shapeL)
        self.penup()
        self.goto(gotoX, gotoY)

    def moveUp(self, pixels = 20):
        y = self.ycor()
        y += pixels
        self.sety(y)

    def moveDown(self, pixels = 20):
        y = self.ycor()
        y -= pixels
        self.sety(y)

    def checkCollision(self, ball):
        if (ball.xcor() > 340) and (ball.ycor() < self.ycor() + 50) and (ball.ycor() > self.ycor() - 50):
            ball.setx(340)
            ball.dx *= -1
            os.system("aplay bounce.wav&")

        if (ball.xcor() < -340) and (ball.ycor() < self.ycor() + 50) and (ball.ycor() > self.ycor() - 50):
            ball.setx(-340)
            ball.dx *= -1
            os.system("aplay bounce.wav&")

class Ball(turtle.Turtle):
    def __init__(self, color, size, speed = .2):
        super().__init__()
        self.color(color)
        self.speed(1)
        self.shape('circle')
        self.shapesize(stretch_wid=size, stretch_len=size)
        self.penup()
        self.goto(0, 0)
        # Movement in x and y directions (pixel/frame)
        self.dx = speed
        self.dy = speed

        # Scoring start
        self.score_a = 0
        self.score_b = 0

    def move(self):
        self.goto(self.xcor() + self.dx, self.ycor() + self.dy)
        # Border checking
        if ball.ycor() > 290:
            ball.sety(290)
            # Reverse the y direction
            ball.dy *= -1
        
        if ball.ycor() < -290:
            ball.sety(-290)
            # Reverse the y direction
            ball.dy *= -1

        if ball.xcor() > 390:
            ball.goto(0, 0)
            ball.dx *= -1
            self.score_a += 1

        if ball.xcor() < -390:
            ball.goto(0, 0)
            ball.dx *= -1
            self.score_b += 1
           
    def update(self):
        self.move()

class Score(turtle.Turtle):
    def __init__(self, color, gotoX = 0, gotoY = 270, size = 20):
        super().__init__()
        self.color(color)
        self.speed(0)

        # Initialize scores
        self.score_a = 0
        self.score_b = 0
        # Not to see the line of the turtle object
        # self.hideturtle()
        self.penup() 
        self.goto(gotoX, gotoY)
        self.write(f'Player A: 0  Player B: 0', align='center', font=('Courier', size, 'normal'))

        self.scoreA = 0
        self.scoreB = 0

    def update(self, ball):
        self.clear()
        self.write(f'Player A: {ball.score_a}  Player B: {ball.score_b}', align='center', font=('Courier', size, 'normal'))
      

if __name__ == '__main__':

    # Create a screen
    wn = turtle.Screen()
    wn.title("Pong")
    wn.bgcolor("black")
    wn.setup(width=800, height=600)
    wn.tracer(0)
    
    #  Objects in the game
    paddle_a = paddle('white', -350, 0, 5, 1)
    paddle_b = paddle('yellow', 350, 0, 5, 1)
    score = Score('red', 0, 260, 20)
    ball = Ball('white',1.5)

    #  Key bindings
    wn.listen()
    wn.onkeypress(paddle_a.moveUp, 'w')
    wn.onkeypress(paddle_a.moveDown, 's')
    wn.onkeypress(paddle_b.moveUp, 'Up')
    wn.onkeypress(paddle_b.moveDown, 'Down')

    # Main game loop
    while True:
        wn.update()
        # # Move the ball
        ball.update()

        # Collision checking
        paddle_a.checkCollision(ball)
        paddle_b.checkCollision(ball)

        #  Check if the ball hit the border
        score.update(ball)

    