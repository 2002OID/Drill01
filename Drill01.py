import turtle

def move_w():
    turtle.setheading(90)
    turtle.forward(50)

def move_a():
    turtle.setheading(180)
    turtle.forward(50)

def move_s():
    turtle.setheading(-90)
    turtle.forward(50)

def move_d():
    turtle.setheading(0)
    turtle.forward(50)

def reseting():
    turtle.reset()

turtle.onkey(move_w,'w')
turtle.onkey(move_a,'a')
turtle.onkey(move_s,'s')
turtle.onkey(move_d,'d')

turtle.onkey(reseting,'Escape')

tertle.listen()
