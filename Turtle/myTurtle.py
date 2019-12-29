from turtle import *

import turtle

sc = turtle.Screen()
foo =  turtle.Turtle()

#render speed
# turtle.tracer(0,0) #instant
turtle.tracer(1,1) #normal
# turtle.tracer(3,3) #fast


bgcolor('black')
pendown()

clrs_1 = ['#ff0000','#ff8000','#ffc400','#ccff00','#33ff00','#00ff95']

def draw(xcor,ycor):
        foo.clear()
        foo.reset()
        foo.hideturtle()
        for i in range(5):
                width(5)
                rt(90)
                fd(100+(i/100))
                pencolor(clrs_1[ i % 6])

sc.onclick(draw)
# sc.onscreenclick(draw)
sc.onkey(sc.bye, 'q')

sc.listen()
sc.mainloop()


