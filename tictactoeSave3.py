#Designed and devleoped by Alex Palumbo
#Name - Tic Tac Toe
#Start - 2/22/2017

import sys
import os
import turtle
turtle.setup(width=450, height=470)	#set up window
wn = turtle.Screen()                    #initiates window
wn.title("Tic Tac Toe - Alex Palumbo")  #window title
myPen = turtle.Turtle()                 #assign name to main turtle
myPen.hideturtle()
myPen.speed(0)
def drawForm():     #draws the tic tac tow board
    myPen.width(1)
    myPen.color('black')
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

def title():        #top title
    myPen.color('black')
    myPen.penup()
    myPen.goto(0,205)
    myPen.write("Tic Tac Toe", False, align="center", font=("Arial", 14, "normal"))
title()

def delText():#covers text with white box
    myPen.penup()
    myPen.goto(-100,-201)
    myPen.setheading(0)
    myPen.begin_fill()
    myPen.forward(200)
    myPen.right(90)
    myPen.forward(25)
    myPen.right(90)
    myPen.forward(200)
    myPen.right(90)
    myPen.forward(25)
    myPen.color('white')
    myPen.end_fill()

def text1():        #player 1
    delText()
    myPen.color('black')
    myPen.penup()
    myPen.goto(0,-225)
    myPen.write("Player one's turn ", False, align="center", font=("Arial", 14, "normal"))
text1()
    
def text2():      #player 2
    delText()
    myPen.color('black')
    myPen.penup()
    myPen.goto(0,-225)
    myPen.write("Player two's turn ", False, align="center", font=("Arial", 14, "normal"))
        

def drawX(x,y):     #draws the X move
    myPen.color('black')
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
    myPen.color('black')
    myPen.width(3)
    myPen.penup()
    myPen.goto(x,y)
    myPen.setheading(270)
    myPen.forward(64) #goes down 64 because circle does not draw from center
    myPen.setheading(0)
    myPen.pendown()
    myPen.circle(64) #circe radius
#------------------------------------------------------------------------------------------------------------------------------
def boxR():#covers text with white box
    myPen.penup()
    myPen.goto(-100,-230)
    myPen.setheading(0)
    myPen.begin_fill()
    myPen.forward(200)
    myPen.right(90)
    myPen.forward(30)
    myPen.right(90)
    myPen.forward(200)
    myPen.right(90)
    myPen.forward(30)
    myPen.color('white')
    myPen.end_fill()
    boxRText()
def boxRText():
    myPen.color('red')
    myPen.penup()
    myPen.goto(0,-257)
    myPen.write("Play Again?", False, align="center", font=("Arial", 16, "normal"))
boxR()
#------------------------------------------------------------------------------------------------------------------------------
    
tl=0
tm=0
tr=0
ml=0
mm=0
mr=0
bl=0
bm=0
br=0

def checkCoords(x,y,turn):#check coords to see which box was clicked, then draw an O or X depending on turn
    global tl
    global tm
    global tr
    global ml
    global mm
    global mr
    global bl
    global bm
    global br
    global turn1
    if(x>-400 and x<-67 and y>67 and y<200): #top left, center = -134,134
        if tl==0:
            if turn==1:
                drawX(-134,134)
                tl=1
                text2()
                checkWin()
            else:
                drawO(-134,134)
                tl=2
                text1()
                checkWin()
        else:
            if turn==1:
                turn1=2
            else:
                turn1=1

    elif(x<67 and x>-67 and y>67 and y<200): #top middle, center = 0,134
        if tm==0:
            if turn==1:
                drawX(0,134)
                tm=1
                text2()
                checkWin()
            else:
                drawO(0,134)
                tm=2
                text1()
                checkWin()
        else:
            if turn==1:
                turn1=2
            else:
                turn1=1
            
    elif(x>67 and x<200 and y>67 and y<200): #top right, center = 134,134
        if tr==0:
            if turn==1:
                drawX(134,134)
                tr=1
                text2()
                checkWin()
            else:
                drawO(134,134)
                tr=2
                text1()
                checkWin()
        else:
            if turn==1:
                turn1=2
            else:
                turn1=1
            
    elif(x>-200 and x<-67 and y>-67 and y<67): #middle left, center = -134,0
        if ml==0:
            if turn==1:
                drawX(-134,0)
                ml=1
                text2()
                checkWin()
            else:
                drawO(-134,0)
                ml=2
                text1()
                checkWin()
        else:
            if turn==1:
                turn1=2
            else:
                turn1=1
            
    elif (x<67 and x>-67 and y<67 and y>-67): #middle middle, center = 0,0
        if mm==0:
            if turn==1:
                drawX(0,0)
                mm=1
                text2()
                checkWin()
            else:
                drawO(0,0)
                mm=2
                text1()
                checkWin()
        else:
            if turn==1:
                turn1=2
            else:
                turn1=1

    elif (x>67 and x<200 and y<67 and y>-67): #middle right, center = 134,0
        if mr==0:
            if turn==1:
                drawX(134,0)
                mr=1
                text2()
                checkWin()
            else:
                drawO(134,0)
                mr=2
                text1()
                checkWin()
        else:
            if turn==1:
                turn1=2
            else:
                turn1=1
	    
    elif (x>-200 and x<-67 and y>-200 and y<-67): #bottom left, center = -134,-134
        if bl==0:
            if turn==1:
                drawX(-134,-134)
                bl=1
                text2()
                checkWin()
            else:
                drawO(-134,-134)
                bl=2
                text1()
                checkWin()
        else:
            if turn==1:
                turn1=2
            else:
                turn1=1
	    
    elif (x<67 and x>-67 and y>-200 and y<-67): #bottom middle, center = 0,-134
        if bm==0:
            if turn==1:
                drawX(0,-134)
                bm=1
                text2()
                checkWin()
            else:
                drawO(0,-134)
                bm=2
                text1()
                checkWin()
        else:
            if turn==1:
                turn1=2
            else:
                turn1=1
	    
    elif (x>67 and x<200 and y>-200 and y<-67): #bottom right, center = 134,-134
        if br==0:
            if turn==1:
                drawX(134,-134)
                br=1
                text2()
                checkWin()
            else:
                drawO(134,-134)
                br=2
                text1()
                checkWin()
                
        else:
            if turn==1:
                turn1=2
            else:
                turn1=1
            
turn1=2
def whosturn(x,y):
    x=x
    y=y
    global turn1
    if turn1==1:
        turn1=2
    else:
        turn1=1
    checkCoords(x,y,turn1)

run="yes"

def gogo(x,y):
    if run=="yes":
        whosturn(x,y)
    else:
        checkReset(x,y)
            
wn.onscreenclick(gogo) #will stay active, "always listening"


def checkWin():
    if((tl==1 and tm==1 and tr==1) or (ml==1 and mm==1 and mr==1) or (bl==1 and bm==1 and br==1) or (tl==1 and mm==1 and br==1) or (tr==1 and mm==1 and bl==1) or (tl==1 and ml==1 and bl==1) or(tm==1 and mm==1 and bm==1) or (tr==1 and mr==1 and br==1)):
        delText()
        myPen.color('black')
        myPen.penup()
        myPen.goto(0,-225)
        myPen.write("Player One Wins!", False, align="center", font=("Arial", 14, "normal"))  
        end()
    elif((tl==2 and tm==2 and tr==2) or (ml==2 and mm==2 and mr==2) or (bl==2 and bm==2 and br==2) or (tl==2 and mm==2 and br==2) or (tr==2 and mm==2 and bl==2) or (tl==2 and ml==2 and bl==2) or(tm==2 and mm==2 and bm==2) or (tr==2 and mr==2 and br==2)):        
        delText()
        myPen.color('black')
        myPen.penup()
        myPen.goto(0,-225)
        myPen.write("Player Two Wins!", False, align="center", font=("Arial", 14, "normal"))  
        end()
    elif(tl!=0 and tm!=0 and tr!=0 and ml!=0 and mm!=0 and mr!=0 and bl!=0 and bm!=0 and br!=0): #check to see if board is full
        delText()
        myPen.color('black')
        myPen.penup()
        myPen.goto(0,-225)
        myPen.write("Tie", False, align="center", font=("Arial", 14, "normal"))  
        end()
def checkReset(x,y):
    if(x>-100 and x<100 and y<-230 and y>-260):
        reset()

        
"""
    myPen.goto(-100,-230)
    myPen.setheading(0)
    myPen.begin_fill()
    myPen.forward(200)
    myPen.right(90)
    myPen.forward(30)
    myPen.right(90)
    myPen.forward(200)
    myPen.right(90)
    myPen.forward(30)
"""
def end():
    global tl
    global tm
    global tr
    global ml
    global mm
    global mr
    global bl
    global bm
    global br
    global turn1
    global run
    run="no"
    wn.bgcolor("#f4f8ff")
    turn1=2
    tl=0
    tm=0
    tr=0
    ml=0
    mm=0
    mr=0
    bl=0
    bm=0
    br=0
    turtle.setup(width=450, height=535)

def reset():
    global run
    myPen.clear()
    turtle.setup(width=450, height=470)
    wn.bgcolor("white")
    drawForm()
    text1()
    title()
    boxR()
    run="yes"
"""
TO DO//






"""




















    
