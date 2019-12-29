from turtle import *

import turtle
import random

sc = turtle.Screen()
foo = turtle.Turtle()

#render speed
turtle.tracer(0,0) #instant
# turtle.tracer(1,1) #normal
# turtle.tracer(3,3) #fast


bgcolor('black')
turtle.ht()

clrs_1 = ['#ff0000','#ff8000','#ffc400','#ccff00','#33ff00','#00ff95']

def draw(xcor,ycor):
        # turtle.setposition(xcor,ycor)
        turtle.reset()
        turtle.hideturtle()
        turtle.goto(xcor,ycor)
        
        for i in range(300):
                
                width(5)
                fd(10+(i*2))
                rt(91)
                pencolor(clrs_1[ i % 6])
        
sc.onclick(draw)
sc.onkey(sc.bye, 'q')

sc.listen()
sc.mainloop()


