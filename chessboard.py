import turtle
chessboard = turtle.Turtle()
chessboard.speed(8) 
for i in range(14): 
    chessboard.forward(800) 
    chessboard.right(90) 
a = 0 
b = 0 

for i in range(14): 
    if(b == 0):
        a=1
    else:
        a=0
    for j in range(14): 
        chessboard.penup()
        chessboard.goto(j*100, i*100*(-1))
        chessboard.pendown()
        if(a==0):
            chessboard.fillcolor('black')
            a=1
            box_size = 20
        else:
            chessboard.fillcolor('white')
            a=0
            box_size = 20
        chessboard.begin_fill()
        for k in range(4):
            chessboard.forward(100)
            chessboard.right(90)
        chessboard.end_fill()
    if(b==0):
        b=1
    else:
        b=0
  
import turtle
chessboard = turtle.Turtle()
chessboard.speed(8) 
for i in range(4): 
    chessboard.forward(800) 
    chessboard.right(90) 
a = 0 
b = 0 
for i in range(8):
    if(b == 0):
        a=1
    else:
        a=0
    for j in range(8): 
        chessboard.penup()
        chessboard.goto(j*100, i*100*(-1))
        chessboard.pendown()
        if(a==0):
            chessboard.fillcolor('black')
            a=1
        else:
            chessboard.fillcolor('white')
            a=0
        chessboard.begin_fill()
        for k in range(4):
            chessboard.forward(100)
            chessboard.right(90)
        chessboard.end_fill()
    if(b==0):
        b=1
    else:
        b=0