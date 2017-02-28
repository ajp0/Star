#Designed and devleoped by Alex Palumbo
#Name - Tic Tac Toe
#Start - 2/22/2017

import sys
import os
import turtle
turtle.setup(width=450, height=470)	#set up window
wn = turtle.Screen()
wn.title("Tic Tac Toe - Alex Palumbo")
myPen = turtle.Turtle()
myPen.hideturtle()
myPen.speed(0)
def drawForm():     #draws the tic tac tow board
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

def title():
    myPen.color('black')
    myPen.penup()
    myPen.goto(0,205)
    myPen.write("Tic Tac Toe", False, align="center", font=("Arial", 14, "normal"))
title()

def text1():
    myPen.color('black')
    myPen.penup()
    myPen.goto(0,-225)
    myPen.write("Player one's turn ", False, align="center", font=("Arial", 14, "normal"))
text1()
    
def text2():
    myPen.color('black')
    myPen.penup()
    myPen.goto(0,-225)
    myPen.write("Player two's turn ", False, align="center", font=("Arial", 14, "normal"))
    
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
    myPen.circle(64) #circel radius

def reset():
    x=0
    
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
                checkWin()
                delText()   #put this in for all
                text2()     #and this
            else:
                drawO(-134,134)
                tl=2
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
                checkWin()
            else:
                drawO(0,134)
                tm=2
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
                checkWin()
            else:
                drawO(134,134)
                tr=2
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
                checkWin()
            else:
                drawO(-134,0)
                ml=2
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
                checkWin()
            else:
                drawO(0,0)
                mm=2
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
                checkWin()
            else:
                drawO(134,0)
                mr=2
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
                checkWin()
            else:
                drawO(-134,-134)
                bl=2
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
                checkWin()
            else:
                drawO(0,-134)
                bm=2
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
                checkWin()
            else:
                drawO(134,-134)
                br=2
                checkWin()
        else:
            if turn==1:
                turn1=2
            else:
                turn1=1
    #call function to see if a player won
    #call function to change 'player turn' text
            
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

wn.onscreenclick(whosturn) #will stay active, "always listening"

def checkWin():
    myPen.color('black')
    if((tl==1 and tm==1 and tr==1) or (ml==1 and mm==1 and mr==1) or (bl==1 and bm==1 and br==1) or (tl==1 and mm==1 and br==1) or (tr==1 and mm==1 and bl==1) or (tl==1 and ml==1 and bl==1) or(tm==1 and mm==1 and bm==1) or (tl==1 and ml==1 and bl==1)):
        myPen.penup()
        myPen.goto(0,205)
        myPen.write("Player one wins ", False, align="center", font=("Arial", 14, "normal"))
    elif((tl==2 and tm==2 and tr==2) or (ml==2 and mm==2 and mr==2) or (bl==2 and bm==2 and br==2) or (tl==2 and mm==2 and br==2) or (tr==2 and mm==2 and bl==2) or (tl==2 and ml==2 and bl==2) or(tm==2 and mm==2 and bm==2) or (tl==2 and ml==2 and bl==2)):        
        myPen.penup()
        myPen.goto(0,205)
        myPen.write("Player two wins ", False, align="center", font=("Arial", 14, "normal"))
    elif(tl!=0 and tm!=0 and tr!=0 and ml!=0 and mm!=0 and mr!=0 and bl!=0 and bm!=0 and br!=0): #check to see if board is full
        myPen.penup()
        myPen.goto(0,205)
        myPen.write("Tie", False, align="center", font=("Arial", 14, "normal"))



def end():
    x=0

"""
change whos turn it is in the text

if they click on a full space it wont skip there turn

reset command
"""




















    
