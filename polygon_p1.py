from turtle import *

speed('slowest')
pencolor('red')
pensize(50)
bgcolor('black')

side=6
size=100
fillcolor('green')
begin_fill()
for i in range(side):
    fd(size)
    lt(360/side)
end_fill()
mainloop()

