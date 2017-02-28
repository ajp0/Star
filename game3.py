#Designed by Alex Palumbo

import turtle
wn = turtle.Screen()                    #initiates window
wn.setup(width=450, height=490)         #set up window
wn.bgpic("tttbg.gif")                   #background picture
wn.title("Tic Tac Toe - Alex Palumbo")  #window title
           #listens for screen click event
    
dT=turtle.Turtle()
dT.hideturtle()
dO=turtle.Turtle()
dO.hideturtle()
dX=turtle.Turtle()
dX.hideturtle()
rT=turtle.Turtle()
rT.hideturtle()
tl=tm=tr=ml=mm=mr=bl=bm=br=0
turn=1
w=1


def drawX(x,y):
    dX.speed(0)
    dX.color('black')
    dX.width(3)
    dX.penup()
    dX.goto(x,y)
    dX.pendown()
    dX.setheading(-45)
    dX.forward(75)
    dX.setheading(135)
    dX.forward(150)
    dX.penup()
    dX.goto(x,y)
    dX.pendown()
    dX.setheading(45)
    dX.forward(75)
    dX.setheading(225)
    dX.forward(150)
    
def drawO(x,y):
    dO.speed(0)
    dO.color('black')
    dO.width(3)
    dO.penup()
    dO.goto(x,y)
    dO.setheading(270)
    dO.forward(58) #goes down 64 because circle does not draw from center
    dO.setheading(0)
    dO.pendown()
    dO.circle(55) #circe radius

def text(n):
    dT.speed(0)
    dT.hideturtle()
    dT.clear()
    dT.color('black')
    dT.penup()
    dT.goto(0,-225)
    if n==1:
        dT.write("Player One's Turn", False, align="center", font=("Arial", 14, "normal"))
    elif n==2:
        dT.write("Player Two's Turn", False, align="center", font=("Arial", 14, "normal"))
    elif n==3:
        dT.write("Player One Wins", False, align="center", font=("Arial", 14, "normal"))
    elif n==4:
        dT.write("Player Two Wins", False, align="center", font=("Arial", 14, "normal"))
    else:
        dT.write("Tie", False, align="center", font=("Arial", 14, "normal"))
        
text(1)

def checkCoords(x,y):
    global w
    if w==1:
        topLeft = x>-400 and x<-67 and y>67 and y<200   #checks the coords to see what square was clicked
        topMiddle = x<67 and x>-67 and y>67 and y<200
        topRight = x>67 and x<200 and y>67 and y<200
        middleLeft = x>-200 and x<-67 and y>-67 and y<67
        middleMiddle = x<67 and x>-67 and y<67 and y>-67
        middleRight = x>67 and x<200 and y<67 and y>-67
        bottomLeft = x>-200 and x<-67 and y>-200 and y<-67
        bottomMiddle = x<67 and x>-67 and y>-200 and y<-67
        bottomRight = x>67 and x<200 and y>-200 and y<-67
        count=0
        for click in [topLeft, topMiddle, topRight, middleLeft, middleMiddle, middleRight, bottomLeft, bottomMiddle, bottomRight]:
            count=count+1   #1-9
            if click:      #send 1-9 to turn function depending on what box was clicked. print(count) for test
                  changeSquareProperty(count)
    else:
        endCheck(x,y)
              
def changeSquareProperty(square):
    global tl
    global tm
    global tr
    global ml
    global mm
    global mr
    global bl
    global bm
    global br
    global turn
    if square==1:
        if tl==0:
            if turn==1:
                tl=1
                drawX(-134,134)
                turn=2
                text(2)
                checkWin()
            else:
                tl=2
                drawO(-134,134)
                turn=1
                text(1)
                checkWin()
    elif square==2:
        if tm==0:
            if turn==1:
                tm=1
                drawX(0,134)
                turn=2
                text(2)
                checkWin()
            else:
                tm=2
                drawO(0,134)
                turn=1
                text(1)
                checkWin()
    elif square==3:
        if tr==0:
            if turn==1:
                tr=1
                drawX(134,134)
                turn=2
                text(2)
                checkWin()
            else:
                tr=2
                drawO(134,134)
                turn=1
                text(1)
                checkWin()
    elif square==4:
        if ml==0:
            if turn==1:
                ml=1
                drawX(-134,0)
                turn=2
                text(2)
                checkWin()
            else:
                ml=2
                drawO(-134,0)
                turn=1
                text(1)
                checkWin()
    elif square==5:
        if mm==0:
            if turn==1:
                mm=1
                drawX(0,0)
                turn=2
                text(2)
                checkWin()
            else:
                mm=2
                drawO(0,0)
                turn=1
                text(1)
                checkWin()
    elif square==6:
        if mr==0:
            if turn==1:
                mr=1
                drawX(134,0)
                turn=2
                text(2)
                checkWin()
            else:
                mr=2
                drawO(134,0)
                turn=1
                text(1)
                checkWin()
    elif square==7:
        if bl==0:
            if turn==1:
                bl=1
                drawX(-134,-134)
                turn=2
                text(2)
                checkWin()
            else:
                bl=2
                drawO(-134,-134)
                turn=1
                text(1)
                checkWin()
    elif square==8:
        if bm==0:
            if turn==1:
                bm=1
                drawX(0,-134)
                turn=2
                text(2)
                checkWin()
            else:
                bm=2
                drawO(0,-134)
                turn=1
                text(1)
                checkWin()
    elif square==9:
        if br==0:
            if turn==1:
                br=1
                drawX(134,-134)
                turn=2
                text(2)
                checkWin()
            else:
                br=2
                drawO(134,-134)
                turn=1
                text(1)
                checkWin()

def checkWin():
    if((tl==1 and tm==1 and tr==1) or (ml==1 and mm==1 and mr==1) or (bl==1 and bm==1 and br==1) or (tl==1 and mm==1 and br==1) or (tr==1 and mm==1 and bl==1) or (tl==1 and ml==1 and bl==1) or(tm==1 and mm==1 and bm==1) or (tr==1 and mr==1 and br==1)):
        text(3)
        restart()
    elif((tl==2 and tm==2 and tr==2) or (ml==2 and mm==2 and mr==2) or (bl==2 and bm==2 and br==2) or (tl==2 and mm==2 and br==2) or (tr==2 and mm==2 and bl==2) or (tl==2 and ml==2 and bl==2) or(tm==2 and mm==2 and bm==2) or (tr==2 and mr==2 and br==2)):        
        text(4) 
        restart()
    elif(tl!=0 and tm!=0 and tr!=0 and ml!=0 and mm!=0 and mr!=0 and bl!=0 and bm!=0 and br!=0): #check to see if board is full
        text(5)
        restart()

def restart():
    global w
    w=2
    rT.penup()
    rT.speed(0)
    rT.goto(-130,210)
    rT.color('red')
    rT.write("Restart?", False, align="center", font=("Arial", 14, "normal"))

def endCheck(x,y):
    if x>-167 and x<-95 and y<231 and y>208:
        end()
            
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
    global turn
    global w
    dT.clear()
    dX.clear()
    dO.clear()
    rT.clear()
    text(1)
    tl=tm=tr=ml=mm=mr=bl=bm=br=0
    turn=1
    w=1
    
wn.onscreenclick(checkCoords)
import Tkinter
Tkinter.mainloop()
"""
turtles:
    player turn text
    Os
    xs
    tie/win text
    restart button
methods:
    check who wins
    change turns (text and x/o)
    draw O and X
    draw text 'use parameters'
    clear everything
    game done (show restart button)
    check click coords
    maybe: listen
vatiables:
    tl (0,1,2)
    -
    br
    turn
listen for screen click

outline:
click->check coords->change tl-br value to 1 or 2-> check win-> change turn 'text and piece'-> restart
    
"""
