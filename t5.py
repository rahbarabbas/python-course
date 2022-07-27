from turtle import *
fillcolor('red')
pencolor('blue')
speed('slowest')
pensize(3)
for i in range(10,0,-1):
    begin_fill()
    circle(i*10)
    lt(25)
    end_fill()
mainloop()