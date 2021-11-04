#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# WarComplete.py
import random
suits = ['clubs', 'diamonds', 'hearts', 'spades']
faces = ['two', 'three', 'four', 'five', 'six',
         'seven', 'eight', 'nine', 'ten', 'jack',
         'queen', 'king', 'ace']
keepGoing = True
hands = 0
ties = 0
my_score = 0
your_score = 0
while keepGoing and (hands < 26):
    hands += 1
    my_face = random.choice(faces)
    my_suit = random.choice(suits)
    your_face = random.choice(faces)
    your_suit = random.choice(suits)
    print ("I have the", my_face, "of", my_suit)
    print ("You have the", your_face, "of", your_suit)
    if faces.index(my_face) > faces.index(your_face):
        print ("I win!")
        my_score += 1 + ties
        ties = 0
    elif faces.index(your_face) > faces.index(my_face):
        print ("You win!")
        your_score += 1 + ties
        ties = 0
    else:
        print ("It's a tie!")
        ties += 1
    print ("Score: Computer",my_score, ", You",your_score)
    answer = input("Hit [Enter] to keep going, any other keys to exit: ")
    keepGoing = (answer == "")
print("Game Over")
if my_score > your_score:
    print ("I win the game!")
elif your_score > my_score:
    print ("You win the game!")
else:
    print ("It was a tie game!")


# In[ ]:


#Kaleidoscope2.py
import random
import turtle
t = turtle.Pen()
t.speed(0)
turtle.bgcolor('black')
colors=['red', 'yellow', 'blue', 'green',
        'orange', 'purple', 'white', 'gray']

for n in range(50):
    # generate spirals of random sizes/colors at random locations on the screen
    t.pencolor(random.choice(colors))   # pick a random color from colors[]
    size = random.randint(10,40)        # random size spiral from 10 to 40
    sides = random.randint(3,9)        # random number of sides in spiral
    thick = random.randint(1,6)         # random thickness of the lines
    t.width(thick)
    angle = t.heading() #remember the angle we're starting at
    
    # generate a random (x,y) location on the screen
    x = random.randrange(size,turtle.window_width()//2)
    y = random.randrange(size,turtle.window_height()//2)
    # first spiral
    t.penup()
    t.setpos(x,y)
    t.pendown()
    for m in range(size):
        t.forward(m*2)
        t.left(360/sides + 2)
    # second spiral
    t.penup()
    t.setpos(-x,y)
    t.pendown()
    t.setheading(180-angle)
    for m in range(size):
        t.forward(m*2)
        t.right(360/sides + 2)    
    # third spiral
    t.penup()
    t.setpos(-x,-y)
    t.pendown()
    t.setheading(angle-180)
    for m in range(size):
        t.forward(m*2)
        t.left(360/sides + 2)
    # fourth spiral
    t.penup()
    t.setpos(x,-y)
    t.pendown()
    t.setheading(360-angle)
    for m in range(size):
        t.forward(m*2)
        t.right(360/sides + 2)


# In[ ]:


#rock, paper, scissors
import random
choices = ["scissors", "rock", "paper"]
person = input("Do you choose rock, paper, or scissors? (q to quit) ")
while person != "q":
    person = person.lower()
    computer = random.choice(choices)
    print("You choose " +person+ ", and the computer chose, " +computer+".")
    if person == computer:
        print("Its a tie!")
    elif person =="rock":
        if computer =="scissors":
            print("You win!")
        else:
            print("You lost :(")
    elif person =="paper":
        if computer =="rock":
            print("You won!")
        else:
            print("You lost:/")
    elif person =="scissors":
        if computer =="paper":
            print("You Won")
        else:
            print("You lost -_-")
    else: 
        print("I think there was some sort of error")
    print()
    person = input("Do you choose rock, paper, or scissors? (q to quit) ")                                                      


# In[ ]:


#click smilly face
import turtle
import random 

t = turtle.Pen()
turtle.bgcolor("black")
t.speed(0)
turtle.hideturtle()

def spiral(x,y):  #function for the smilly face
    t.penup()
    t.setpos(x,y)
    t.pendown()
    #Head
    t.pencolor("yellow")
    t.fillcolor("yellow")
    t.begin_fill()
    t.circle(50)
    t.end_fill()
    #Left eye
    t.setpos(x-20,y +60)
    t.fillcolor("blue")
    t.begin_fill()
    t.circle(10)
    t.end_fill()
    #Right eye
    t.setpos(x+20,y +60)
    t.fillcolor("blue")
    t.begin_fill()
    t.circle(10)
    t.end_fill()
    #Mouth
    t.setpos(x-30, y+40)
    t.pencolor("black")
    t.width(10)
    t.goto(x-10, y+20)
    t.goto(x+10, y+20)
    t.goto(x+30, y+40)
    t.width(1)

turtle.onscreenclick(spiral)


# In[ ]:




