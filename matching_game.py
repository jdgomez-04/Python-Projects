import random
from turtle import *

x_val = [0,75,150,225,0,75,150,225,0,75,150,225]
y_val = [0,0,0,0,75,75,75,75,150,150,150,150]
correct = 0
chosen = []

def playmemory():
    
    reset()
    createspace()
    store()
    
    while correct != 6:
        flipcard()
        matchcheck()
    
    endgame()
    done()
    

def createspace():
    play = input('Play? Y/N: ')
    print('Cards are in order 1-12 from bottom to top and left to right.')
    if play == 'Y':
        speed(0)
        screen = Screen()
        setworldcoordinates(-50, -50, 325, 250)
        screen.bgcolor("grey")
        screen.title('Memory Game')
        for i in range(len(x_val)):
            x = x_val[i]
            y = y_val[i]
            Square(x, y, 'white', 'green')
        
        
        
def Square(x, y, col1, col2):
    setheading(0)
    up()
    goto(x, y)
    down()
    color(col1, col2)
    begin_fill()
    for count in range(4):
        forward(50)
        left(90)
    end_fill()
    
    
def shapes(x,y):
    
    setheading(0)
    up()

    if stored[guess-1] == 1:  
        goto(x+10, y+10)
        down()
        color('white', 'yellow')
        begin_fill()
        for count in range(4):
            forward(30)
            left(90)
        
    elif stored[guess-1] == 2:
        goto(x+25, y+10)
        down()
        color('white', 'yellow')
        begin_fill()
        circle(15)
        
    elif stored[guess-1] == 3:
        goto(x+10, y+13)
        down()
        color('white', 'yellow')
        begin_fill()
        for count in range(3):
            forward(30)
            left(120)
            
    elif stored[guess-1] == 4:
        goto(x+15, y+7)
        down()
        color('white', 'yellow')
        begin_fill()
        for count in range(6):
            forward(20)
            left(60)
            
            
    elif stored[guess-1] == 5:
        goto(x+26, y+33)
        down()
        color('white', 'yellow')
        begin_fill()
        setheading(20)
        for count in range(5):
            forward(10)
            right(120)
            forward(10)
            right(72 - 120)
            
    elif stored[guess-1] == 6:
        goto(x+10, y+17)
        down()
        color('white', 'yellow')
        begin_fill()
        for count in range(2):
            forward(30)
            left(90)
            forward(15)
            left(90)
            
    end_fill()
    
    
    
# def createcards():
    
def randomize():
    cards = [1,1,2,2,3,3,4,4,5,5,6,6]
    random.shuffle(cards)
    return cards

def store():
    global stored
    stored = randomize()
    #print(stored)
   

# def arrange():
    
# def displaycard():
    
def selectcard():
    global guess
    guess = int(input("Choose a card to flip 1-12: "))
    while guess in chosen or guess > 12 or guess < 1:
        if guess in chosen or guess > 12 or guess < 1:
            guess = int(input("Choose a new card: "))
    
# def removecard():
    
def flipcard():
    selectcard()
    global first, second
    first = guess
    x = x_val[guess-1]
    y = y_val[guess-1]
    shapes(x, y)
    selectcard()
    second = guess
    x = x_val[guess-1]
    y = y_val[guess-1]
    shapes(x, y)
    
def matchcheck():
    global correct, chosenY
    if stored[first-1] == stored[second-1]:  
        speed(3)
        x = x_val[first-1]
        y = y_val[first-1]
        Square(x, y, 'grey', 'grey')
        x = x_val[second-1]
        y = y_val[second-1]
        Square(x, y, 'grey', 'grey')
        chosen.append(first)
        chosen.append(second)
        #print(chosen)
        print('Those match!')
        correct += 1
        
    elif stored[first-1] != stored[second-1]:  
        speed(3)
        x = x_val[first-1]
        y = y_val[first-1]
        Square(x, y, 'white', 'green')
        x = x_val[second-1]
        y = y_val[second-1]
        Square(x, y, 'white', 'green')
        print("Those don't match.")
    speed(0)
        
# def reflip():
    
def endgame():
    print('Congratulations, You Win!!!')
    
playmemory()