from turtle import *

#we want to paint a house

#step 1:   draw a square
shape("turtle")
speed(30) 
width(7) 
color("purple")
forward(200) 
left(90)
 
forward(200) 
left(90)

forward(200) 
left(90) 

forward(200) 
left(90) 
#end of square 

#drawing a door

forward(70)
color("yellow")
begin_fill() 
left(90) 
forward(120)    #height of the door
right(90)
forward(60) 
right(90)
forward(120)
end_fill() 
penup() 
goto(200, 200) 
pendown()

color("red") 
begin_fill()
right(150) 
forward(200) 
left(120) 
forward(200) 
end_fill()

#drawing  windows

color("blue") 
begin_fill()
penup()
left(50)
forward(40)
pendown() 
left(70) 
forward(40)
right(90)
forward(60)
right(90)
forward(40) 
right(90)
forward(60)
end_fill()    #one window finished

#drawing second window

color("blue")
begin_fill()
penup()
right(90)
forward(130)
pendown()
forward(40)
right(90)
forward(60)
right(90)
forward(40)
right(90)
forward(60)
end_fill() 

exitonclick() 

#The house is done  