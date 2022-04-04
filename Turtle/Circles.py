from turtle import *

bgcolor('black')
speed(0)
hideturtle()
for i in range(600):
    color('#FF00F7') #8000FF
    circle(i)
    color('#8000FF') #46FFF4
    circle(i*0.8)
    color('#46FFF4') #FF00F7
    circle(i*0.65)
    right(3)
    forward(3)
done()