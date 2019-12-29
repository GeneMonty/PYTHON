from turtle import *

import turtle
import random

sc = turtle.Screen()
foo = turtle.Turtle()

#render speed
# turtle.tracer(0,0) #instant
# turtle.tracer(1,1) #normal
turtle.tracer(3,3) #fast


bgcolor('black')
turtle.ht()

clrs_1 = ['#ff0000','#ff8000','#ffc400','#ccff00','#33ff00','#00ff95']
clrs_2 = ['#00ffe1','#0095ff','#0037ff','#8400ff','#ff00c3','#ff0062']

def draw(xcor,ycor):
        # turtle.setposition(xcor,ycor)
        turtle.reset()
        turtle.hideturtle()
        turtle.goto(xcor,ycor)
        
        for i in range(80):
                pencolor(clrs_2[ i % 6])
                for i in range(5):
                        width(5)
                        fd(50)#(100+(i/2))
                        rt(61)
                        pencolor(clrs_1[ i % 6])
                        # for i in range(5):
                        #         width(5)
                        #         fd(5)#(100+(i/2))
                        #         rt(45)
                        #         pencolor(clrs_1[ i % 6])
                        # fd(50*i)
                fd(50*i)






sc.onclick(draw)
sc.onkey(sc.bye, 'q')

sc.listen()
sc.mainloop()
# sc.done()


