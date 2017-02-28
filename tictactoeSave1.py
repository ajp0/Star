#Designed and devleoped by Alex Palumbo
#Tic Tac Toe
#Start - 2/22/2017

import turtle
#set up screen
turtle.setup(450,470)
wn = turtle.Screen()
myPen = turtle.Turtle()
myPen.hideturtle()
myPen.speed(0)
def drawForm():     #draws the tic tac tow board
    myPen.penup()
    myPen.goto(-67,-200)
    myPen.pendown()
    myPen.goto(-67,200)
    myPen.penup()
    myPen.goto(67,200)
    myPen.pendown()
    myPen.goto(67,-200)
    myPen.penup()
    myPen.goto(-200,67)
    myPen.pendown()
    myPen.goto(200,67)
    myPen.penup()
    myPen.goto(-200,-67)
    myPen.pendown()
    myPen.goto(200,-67)
drawForm()
def text():
    myPen.penup()
    myPen.goto(0,-225)
    myPen.write("Player one's turn ", False, align="center", font=("Arial", 14, "normal"))
text()

def drawX(x,y):     #draws the X move
    myPen.width(3)
    myPen.penup()
    myPen.goto(x,y)
    myPen.pendown()
    myPen.setheading(-45)
    myPen.forward(90)
    myPen.setheading(135)
    myPen.forward(180)
    myPen.penup()
    myPen.goto(x,y)
    myPen.pendown()
    myPen.setheading(45)
    myPen.forward(90)
    myPen.setheading(225)
    myPen.forward(180)
    
def drawO(x,y):     #draws the O move
    myPen.width(3)
    myPen.penup()
    myPen.goto(x,y)
    myPen.setheading(270)
    myPen.forward(64) #goes down 64 because circle does not draw from center
    myPen.setheading(0)
    myPen.pendown()
    myPen.circle(64) #circel radius

def reset():
    x=0
    
turn=0

def checkCoords(x,y):
    if(x>-400 and x<-67 and y>67 and y<200): #top left, center =
        drawO(0,133)
    elif(x<67 and x>-67 and y>67 and y<200): #top middle, center =
        drawO(0,133)
    elif(x>67 and x<200 and y>67 and y<200): #top right, center =
        drawO(0,133)
    elif(x>-200 and x<-67 and y>-67 and y<67): #middle left, center =
        drawO(0,133)
    elif (x<67 and x>-67 and y<67 and y>-67): #middle middle, center =
        drawO(0,133)
    elif (x>67 and x<200 and y<67 and y>-67): #middle right, center =
        drawO(0,133)
    elif (x>-200 and x<-67 and y>-200 and y<-67): #bottom left, center =
        drawO(0,133)
    elif (x<67 and x>-67 and y>-200 and y<-67): #bottom middle, center =
        drawO(0,133)
    elif (x>67 and x<200 and y>-200 and y<-67): #bottom right, center =
        drawX(0,0)

def testCoords(x,y):
    print x, y  #use to check coords of screen
    
wn.onscreenclick(checkCoords) #will stay active, "always listening"

"""
make function to tell whos turn it is and send that with a variable when checking coords
change whos turn it is in the text
"""
    
