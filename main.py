#
#	main.py
#	Pairs - Ultimate Edition 
#
#	Created by sgav191 on 3/12/2021.
#

import turtle
import random
screen = turtle.Screen()
drawer = turtle.Turtle()
screen.title("Pairs")
screen.bgcolor("#00aeff")

hidden = [True]*16
state = None
numbers = list(range(1,9))*2
random.shuffle(numbers)

def Numbering(x, y):
	return int((x + 100) // 50 + ((y + 100) // 50) * 4)

def screenclick(xcor,ycor):
	global state
	print (xcor)
	print (ycor)
	numclick = Numbering(xcor,ycor)
	print (numclick)
	oldstate = state
	if oldstate == None:
		state = numclick
		print ("No Match")
	else:
		print ("Numbers match")
		state = None

def coordinatesx(num):
	xcor = (num % 4) * 50 - 100
	return xcor

def coordinatesy(num):
	ycor = (num // 4) * 50 - 100
	return ycor
def drawsquare(xcor,ycor):
	drawer.penup()
	drawer.goto(xcor,ycor)
	drawer.color("#ff0000")
	drawer.begin_fill()
	drawer.pendown()
	for num in range(4):
		drawer.forward(45)
		drawer.left(90)
	drawer.end_fill()
def draw():
	for num in range(16):
		xcor = coordinatesx(num)
		ycor = coordinatesy(num)
		drawsquare(xcor,ycor)
print (numbers)
screen.onscreenclick(screenclick)
draw()
turtle.done()
