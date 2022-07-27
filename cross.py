from turtle import *
fillcolor('red')
bgcolor('green')
pensize(30)
pencolor('black')
begin_fill()
for i in range (4):
    fd(100)
    lt(90)
    fd(100)
    lt(90)
    fd(100)
    rt(90)
end_fill()

mainloop()