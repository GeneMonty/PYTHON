#i store functions that draw different shapes
def workbench_0(xcor,ycor):
        turtle.reset()
        turtle.goto(0,0)
        turtle.ht()
        turtle.speed(0)
        for i in range(400):
                pencolor(clrs_3[ i % 4])
                width(5)
                rt(316) #120 inv-tri , 240 tri
                # bk(2*i)
                fd(1+i)
                # rt(61)

def draw(xcor,ycor):
        # turtle.setposition(xcor,ycor)
        turtle.reset()
        turtle.goto(xcor,ycor)
        
        for i in range(80):
                
                for i in range(5):
                        width(1+(i/100))
                        fd(xcor)#(100+(i/2))
                        rt(ycor)#integer 61
                        pencolor(clrs_1[ i % 6])
                        # for i in range(5):
                        #         width(5)
                        #         fd(5)#(100+(i/2))
                        #         rt(45)
                        #         pencolor(clrs_1[ i % 6])
                        # fd(50*i)
                fd(50*i)

def draw2(xcor,ycor):
        turtle.reset()
        turtle.ht()
        # turtle.getscreen().tracer(0,0)
        turtle.goto(0,0)
        # turtle.speed(0)
        for i in range (360):
                pd()
                width(1+(i/(100)))
                pencolor(clrs_1[ i % 6])
                fd(100+i)
                pu()
                backward(101+i)
                rt(5)

def py_cube_0(xcor,ycor):
        
        turtle.reset()
        turtle.ht()
        turtle.goto(0,0)
        turtle.speed(0)
        for i in range(300):
                pencolor(clrs_3[ i % 6])
                width(5)
                rt(60)
                # bk(2*i)
                fd(1+i)

def sqSpiral_1(xcor,ycor):
        turtle.reset()
        turtle.ht()
        turtle.goto(0,0)
        turtle.speed(0)
        for i in range(600):
                pencolor(clrs_1[ i % 6])
                width(1)
                fd(1**i)
                pencolor(clrs_2[ i % 6])
                rt(90)
                fd(2*i)
                pencolor(clrs_1[ i % 6])
                rt(12)
                fd(3*i)

def sqSpiral_3(xcor,ycor):
        turtle.reset()
        turtle.ht()
        turtle.goto(0,0)
        turtle.speed(0)
        for i in range(600):
                pencolor(clrs_1[ i % 6])
                width(1)
                fd(1**i)
                pencolor(clrs_2[ i % 6])
                rt(90)
                fd(2*i)
                pencolor(clrs_1[ i % 6])
                lt(29)
                fd(3*i)

def sqSpiral_4(xcor,ycor):
        turtle.reset()
        turtle.ht()
        turtle.goto(0,0)
        turtle.speed(0)
        for i in range(600):
                pencolor(clrs_1[ i % 6])
                width(1)
                fd(1**i)
                pencolor(clrs_2[ i % 6])
                rt(90)
                fd(2*i)
                for i in range(4):
                        rt(90)
                        fd(10)#+(i/2))
                pencolor(clrs_1[ i % 6])
                lt(29)
                fd(3*i)

def sqPy_0(xcor,ycor):
        turtle.reset()
        turtle.ht()
        turtle.goto(0,0)
        turtle.speed(0)
        for i in range(600):
                pencolor(clrs_1[ i % 6])
                width(1)
                fd(1**i)
                pencolor(clrs_2[ i % 6])
                rt(90)
                fd(2*i)
                # pencolor(clrs_1[ i % 6])
                # lt(29)
                # fd(3*i)
def star_0(xcor,ycor):
        turtle.reset()
        turtle.ht()
        turtle.goto(0,0)
        turtle.speed(0)
        for i in range(600):
                pencolor(clrs_1[ i % 6])
                width(1)
                fd(1**i)
                pencolor(clrs_2[ i % 6])
                rt(90)
                fd(2*i)
                pencolor(clrs_1[ i % 6])
                lt(29)
                fd(3*i)

def triangle_0(xcor,ycor):
        turtle.reset()
        turtle.ht()
        turtle.goto(0,0)
        turtle.speed(0)
        for i in range(500):
                pencolor(clrs_1[ i % 3])
                width(5)
                rt(241) #120 inv-tri , 240 tri
                # bk(2*i)
                fd(1+i)
                # rt(61)
def triangle_1(xcor,ycor):
        turtle.reset()
        turtle.ht()
        turtle.goto(0,0)
        turtle.speed(0)
        for i in range(500):
                pencolor(clrs_1[ i % 3])
                width(5)
                rt(240) #120 inv-tri , 240 tri
                # bk(2*i)
                fd(1+i)
                # rt(61)

def octaSpiral_0(xcor,ycor):
        turtle.reset()
        turtle.goto(0,0)
        turtle.ht()
        turtle.speed(0)
        for i in range(400):
                pencolor(clrs_3[ i % 4])
                width(5)
                rt(316) #120 inv-tri , 240 tri
                # bk(2*i)
                fd(1+i)
                # rt(61)