'''
name: Naser Al Madi
file: pong.py
data: 9/20/2020
course: CS151 fall
description: simple implementation of the game Pong using python 3 turtles.
'''

import turtle


class Paddle:
    def __init__(self, position):
        ''' initializes a paddle with a position '''
        self.x_position = position["x"]
        self.y_position = position["y"]
        self.turt = make_turtle("square", "white", {"width": 5, "length": 1}, {"x": self.x_position, "y": self.y_position})


    def up(self):
        y = self.turt.ycor()
        y += 20
        self.turt.sety(y)
        self.y_position = y


    def down(self):
        y = self.turt.ycor()
        y -= 20
        self.turt.sety(y)
        self.y_position = y


    def xcor(self):
        ''' returns turtle x_cord '''
        return self.turt.xcor()

    
    def ycor(self):
        ''' returns turtle y_cord '''
        return self.turt.ycor()


def make_turtle(shape, color, stretch_param, position):
    ''' creates a turtle and sets initial position '''
    turt = turtle.Turtle()
    turt.speed(0)
    turt.shape(shape)
    turt.color(color)
    turt.shapesize(stretch_param["width"], stretch_param["length"]) 
    turt.penup()
    turt.goto(position["x"], position["y"])
    return turt


class Ball:
    def __init__(self):
        ''' intializes a ball with default direction and position '''
        self.turt = make_turtle("square", "white", {"width": 1, "length": 1}, {"x": 0, "y": 0})
        self.ball_dx = 0.0925
        self.ball_dy = 0.0925
        self.x_position = 0
        self.y_position = 0


    def move(self):
        ''' moves the ball in x and y directions '''
        self.turt.setx(self.turt.xcor() + self.ball_dx)
        self.turt.sety(self.turt.ycor() + self.ball_dy)

        self.x_position = self.turt.xcor()
        self.y_position = self.turt.ycor()
        self.check_top_bottom()

        
    def check_top_bottom(self):
        if self.turt.ycor() > 290:
            self.turt.sety(290)
            self.ball_dy *= -1

        elif self.turt.ycor() < -290:
            self.turt.sety(-290)
            self.ball_dy *= -1

    def xcor(self):
        ''' returns turtle x_cord '''
        return self.turt.xcor()

    
    def ycor(self):
        ''' returns turtle y_cord '''
        return self.turt.ycor()


    def goto(self, x_pos, y_pos):
        ''' moves ball to new x, y positions '''
        self.turt.goto(x_pos, y_pos)
        self.x_position = x_pos
        self.y_position = y_pos


    def setx(self, x_cor):
        ''' sets the ball x position '''
        self.turt.setx(x_cor)
        self.x_position = x_cor


    def sety(self, y_cor):
        ''' sets the ball y position '''
        self.turt.sety(y_cor)
        self.x_position = y_cor    


class Game:
    def __init__(self):
        self.window = None
        self.ball = None
        self.paddle_1 = None
        self.paddle_2 = None
        self.score_player1 = 0
        self.score_player2 = 0
        self.pen = None
        self.turt = None


    def make_window(self, window_title, bgcolor, dimensions):
        '''this function creates a screen object and returns it'''
        window = turtle.getscreen()
        window.title(window_title)
        window.bgcolor(bgcolor)
        window.setup(dimensions["width"], dimensions["height"])
        window.tracer(0)
        self.window = window


    def initialize(self):
        self.make_window("Pong - A CS151 Reproduction!", "black", {"width":800, "height":600})
        self.paddle_1 = Paddle({"x":-350, "y":0})
        self.paddle_2 = Paddle({"x":350, "y":0})
        self.ball = Ball()
        self.pen = make_turtle("square", "white", {"width":1, "length":1}, {"x":0, "y":260})
        self.pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))
        self.pen.hideturtle()


    def keyboard_bindings(self):
        self.window.listen()
        self.window.onkeypress(self.paddle_1.up, "w")
        self.window.onkeypress(self.paddle_1.down, "s")
        self.window.onkeypress(self.paddle_2.up, "Up")
        self.window.onkeypress(self.paddle_2.down, "Down")


    def border_checking(self):
        if self.ball.xcor() > 350:
            self.score_player1 += 1
            self.pen.clear()
            self.pen.write("Player A: "+ str(self.score_player1) + "  Player B: "+ str(self.score_player2), align="center", font=("Courier", 24, "normal"))
            self.ball.goto(0, 0)
            self.ball.ball_dx *= -1

        elif self.ball.xcor() < -350:
            self.score_player2 += 1
            self.pen.clear()
            self.pen.write("Player A: "+ str(self.score_player1) + "  Player B: "+ str(self.score_player2), align="center", font=("Courier", 24, "normal"))
            self.ball.goto(0, 0)
            self.ball.ball_dx *= -1


    def check_collision(self):
        if self.ball.xcor() < -340 and self.ball.xcor() > -350 and self.ball.ycor() < self.paddle_1.ycor() + 50 and self.ball.ycor() > self.paddle_1.ycor() - 50:
            self.ball.setx(-340)
            self.ball.ball_dx *= -1.5
        
        elif self.ball.xcor() > 340 and self.ball.xcor() < 350 and self.ball.ycor() < self.paddle_2.ycor() + 50 and self.ball.ycor() > self.paddle_2.ycor() - 50:
            self.ball.setx(340)
            self.ball.ball_dx *= -1.5


    def play(self):
        self.window.update()
        self.ball.move()
        self.border_checking()
        self.check_collision()
            

def main():
    ''' the main function where the game events take place '''
    pong_game = Game()
    pong_game.initialize()
    pong_game.keyboard_bindings()

    while True:
        pong_game.play()


if __name__ == "__main__":
	main()