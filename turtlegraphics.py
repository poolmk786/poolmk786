"""ITECH1400 - FOUNDATIONS OF PROGRAMMING.
Assignment 01: Ceaser Ciphers and Turtle Graphics"""
#Importing Turtle Library
import turtle
#giving my name as a variable to be displayed on the title
name = "VENKATESH"
#Title
turtle.title("Turtle writing my Name: "+ name)
#Creating background colour
window = turtle.Screen()
window.bgcolor('light blue')
#First Letter- 'V'
letterV = turtle.Turtle()
letterV.goto(-375,0)
letterV.pensize(4)
letterV.left(45)
letterV.forward(100)
letterV.backward(100)
letterV.right(270)
letterV.forward(100)
letterV.hideturtle()
#Letter E
Eletter = turtle.Turtle()
Eletter.goto(-300,0)
Eletter.pensize(4)
Eletter.forward(70)
Eletter.backward(70)
Eletter.left(90)
Eletter.forward(70)
Eletter.right(90)
Eletter.forward(70)
Eletter.backward(70)
Eletter.right(90)
Eletter.forward(35)
Eletter.left(90)
Eletter.forward(70)
Eletter.hideturtle()
#Letter N
NLetter = turtle.Turtle()
NLetter.goto(-220,0)
NLetter.pensize(4)
NLetter.left(90)
NLetter.forward(70)
NLetter.right(135)
NLetter.forward(100)
NLetter.left(135)
NLetter.forward(70)
NLetter.hideturtle()
#LetterK
KLetter = turtle.Turtle()
KLetter.goto(-135,0)
KLetter.pensize(4)
KLetter.left(90)
KLetter.forward(70)
KLetter.backward(35)
KLetter.right(45)
KLetter.forward(50)
KLetter.backward(50)
KLetter.right(90)
KLetter.forward(50)
KLetter.hideturtle()
#LetterA
ALetter = turtle.Turtle()
ALetter.goto(-95,0)
ALetter.pensize(4)
ALetter.left(45)
ALetter.forward(100)
ALetter.right(90)
ALetter.forward(100)
ALetter.backward(50)
ALetter.right(135)
ALetter.forward(73)
ALetter.hideturtle()
#LetterT
TLetter = turtle.Turtle()
TLetter.goto(62.5,0)
TLetter.pensize(4)
TLetter.left(90)
TLetter.forward(70)
TLetter.left(90)
TLetter.forward(50)
TLetter.backward(100)
TLetter.hideturtle()
#LetterE, again
Eletter1 = turtle.Turtle()
Eletter1.goto(125,0)
Eletter1.pensize(4)
Eletter1.forward(70)
Eletter1.backward(70)
Eletter1.left(90)
Eletter1.forward(70)
Eletter1.right(90)
Eletter1.forward(70)
Eletter1.backward(70)
Eletter1.right(90)
Eletter1.forward(35)
Eletter1.left(90)
Eletter1.forward(70)
Eletter1.hideturtle()
#LetterS
SLetter = turtle.Turtle()
SLetter.goto(210,0)
SLetter.pensize(4)
SLetter.forward(70)
SLetter.left(90)
SLetter.forward(35)
SLetter.left(90)
SLetter.forward(70)
SLetter.right(90)
SLetter.forward(35)
SLetter.right(90)
SLetter.forward(70)
SLetter.hideturtle()
#LetterH
HLetter = turtle.Turtle()
HLetter.goto(290,0)
HLetter.pensize(4)
HLetter.left(90)
HLetter.forward(70)
HLetter.backward(35)
HLetter.right(90)
HLetter.forward(70)
HLetter.left(90)
HLetter.forward(35)
HLetter.backward(70)
HLetter.hideturtle()
#Underline
Underline = turtle.Turtle()
Underline.goto(0, -15)
Underline.pensize(2)
Underline.forward(400)
Underline.backward(800)
Underline.hideturtle()

#Creating Exit on clicking the screen.
turtle.Screen().exitonclick()
