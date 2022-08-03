from turtle import *

size=100
side=6
speed('fastest')
pensize(3)

for i in range(side):
    pencolor('red')
    forward(size)
    for i in range(side):
        dot(20)
        pencolor('green')
        forward(size//2)
        pencolor('black')
        #write(i,font=('Arial',14,'normal'),align='left')
        left(360/side)
    left(360/side)
mainloop()