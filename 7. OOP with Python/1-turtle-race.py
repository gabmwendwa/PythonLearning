import os
from turtle import Turtle
from random import randint
# Ninja Turtles

# Danotello 
Danotello = Turtle()

Danotello.color('purple')
Danotello.shape('turtle')

Danotello.penup()
Danotello.goto(-160, 100)
Danotello.pendown()

# Raphael
Raphael = Turtle()

Raphael.color('red')
Raphael.shape('turtle')

Raphael.penup()
Raphael.goto(-160, 70)
Raphael.pendown()


# Leonardo
Leonardo = Turtle()

Leonardo.color('blue')
Leonardo.shape('turtle')

Leonardo.penup()
Leonardo.goto(-160, 40)
Leonardo.pendown()

# Michaelangelo
Michaelangelo = Turtle()

Michaelangelo.color('orange')
Michaelangelo.shape('turtle')

Michaelangelo.penup()
Michaelangelo.goto(-160, 10)
Michaelangelo.pendown()

for movement in range(100):
	Danotello.forward(randint(1,5))
	Raphael.forward(randint(1,5))
	Leonardo.forward(randint(1,5))
	Michaelangelo.forward(randint(1,5))
 
os.system("pause")

