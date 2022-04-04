from turtle import *

bgcolor('black')
speed(0)
hideturtle()
for i in range(600):
    color('#FF0000') #8000FF
    circle(i*1.7)
    color('#FF7F00') #46FFF4
    circle(i*1.5)
    color('#FFFF00') #FF00F7
    circle(i*1.3)
    color('#00FF00') #FF00F7
    circle(i*1.1)
    color('#0000FF') #FF00F7
    circle(i*0.9)
    color('#4B0082') #FF00F7
    circle(i*0.7)
    color('#9400D3') #FF00F7
    circle(i*0.5)
    right(10)
    forward(10)
done()