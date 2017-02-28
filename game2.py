#Designed by Alex Palumbo

import turtle
def main():
    import turtle
    wn = turtle.Screen()                    #initiates window
    wn.setup(width=450, height=490)         #set up window
    wn.bgpic("tttbg.gif")                   #background picture
    wn.title("Tic Tac Toe - Alex Palumbo")  #window title
    text(1)
    wn.onscreenclick(checkCoords)           #listens for screen click event
    
def varAssign():
    dT=turtle.Turtle()
    dO=turtle.Turtle()
    dX=turtle.Turtle()
    tl=tm=tr=ml=mm=mr=bl=bm=br=0
    turn=1


def drawX(x,y):
    dX.color('black')
    dX.width(3)
    dX.penup()
    dX.goto(x,y)
    dX.pendown()
    dX.setheading(-45)
    dX.forward(90)
    dX.setheading(135)
    dX.forward(180)
    dX.penup()
    dX.goto(x,y)
    dX.pendown()
    dX.setheading(45)
    dX.forward(90)
    dX.setheading(225)
    dX.forward(180)
    
def drawO(x,y):
    dO.color('black')
    dO.width(3)
    dO.penup()
    dO.goto(x,y)
    dO.setheading(270)
    dO.forward(64) #goes down 64 because circle does not draw from center
    dO.setheading(0)
    dO.pendown()
    dO.circle(64) #circe radius

def text(n):
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
        
def checkCoords(x,y):
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
              
def changeSquareProperty(square):
    if square==1:
        if tl==0:
            print("got hur")
            if turn==1:
                tl=1
                drawX(-134,134)
                turn=2
                text(2)
                
            else:
                tl=2
                drawO(-134,134)
                turn=1
                text(1)
                checkWin()
    elif square==2:
        print("got hur")

def checkWin():
    if((tl==1 and tm==1 and tr==1) or (ml==1 and mm==1 and mr==1) or (bl==1 and bm==1 and br==1) or (tl==1 and mm==1 and br==1) or (tr==1 and mm==1 and bl==1) or (tl==1 and ml==1 and bl==1) or(tm==1 and mm==1 and bm==1) or (tr==1 and mr==1 and br==1)):
        text(3)
        end()
    elif((tl==2 and tm==2 and tr==2) or (ml==2 and mm==2 and mr==2) or (bl==2 and bm==2 and br==2) or (tl==2 and mm==2 and br==2) or (tr==2 and mm==2 and bl==2) or (tl==2 and ml==2 and bl==2) or(tm==2 and mm==2 and bm==2) or (tr==2 and mr==2 and br==2)):        
        text(4) 
        end()
    elif(tl!=0 and tm!=0 and tr!=0 and ml!=0 and mm!=0 and mr!=0 and bl!=0 and bm!=0 and br!=0): #check to see if board is full
        text(5)
        end()
def end():
    print("done")
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
