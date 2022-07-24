from turtle import *

speed('slowest')
pencolor('blue')
bgcolor('green')

side=6
size=100
for i in range(side):
    fd(size)
    lt(360/side)

mainloop()

