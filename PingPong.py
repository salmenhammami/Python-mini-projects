import turtle

wind=turtle.Screen()
wind.title("ping-pong")
wind.bgcolor("black")
wind.setup(width=800,height=600)
wind.tracer(0)

bar1=turtle.Turtle()
bar1.speed(0)
bar1.shape("square")
bar1.color("blue")
bar1.penup()
bar1.goto(-380,0)
bar1.shapesize(stretch_wid=5,stretch_len=1)

bar2=turtle.Turtle()
bar2.speed(0)
bar2.shape("square")
bar2.color("red")
bar2.penup()
bar2.goto(380,0)
bar2.shapesize(stretch_wid=5,stretch_len=1)

ball=turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0,0)

ball.dx=0.3
ball.dy=0.3

score1=0
score2=0
score=turtle.Turtle()
score.speed(0)
score.color("white")
score.penup()
score.hideturtle()
score.goto(0,260)
score.write("player 1 : 0   player 2: 0",align="center",font=("courier",24,"normal "))

def bar1_up():
    y=bar1.ycor()
    y+=20
    bar1.sety(y)

def bar1_down():
    y=bar1.ycor()
    y-=20
    bar1.sety(y)

def bar2_up():
    y=bar2.ycor()
    y+=20
    bar2.sety(y)

def bar2_down():
    y=bar2.ycor()
    y-=20
    bar2.sety(y)

wind.listen()
wind.onkeypress(bar1_up,"z")
wind.onkeypress(bar1_down,"s")
wind.onkeypress(bar2_up,"Up")
wind.onkeypress(bar2_down,"Down")

while True:
    wind.update()
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)
    
    if ball.ycor()>290:
        ball.sety(290)
        ball.dy*=-1

    if ball.ycor()<-290:
        ball.sety(-290)
        ball.dy*=-1
    
    if ball.xcor()>390:
        ball.goto(0,0)
        ball.dx*=-1
        score1+=1
        score.clear()
        score.write("player 1 : {}   player 2: {}".format(score1,score2),align="center",font=("courier",24,"normal "))

    if ball.xcor()<-390:
        ball.goto(0,0)
        ball.dx*=-1
        score2+=1
        score.clear()
        score.write("player 1 : {}   player 2: {}".format(score1,score2),align="center",font=("courier",24,"normal "))
    
    if (ball.xcor()<-370 and ball.xcor()>-380) and (ball.ycor()<bar1.ycor()+40 and ball.ycor()>bar1.ycor()-40):
        ball.setx(-370)
        ball.dx*=-1

    if (ball.xcor()>370 and ball.xcor()<380) and (ball.ycor()<bar2.ycor()+40 and ball.ycor()>bar2.ycor()-40):
        ball.setx(340)
        ball.dx*=-1
