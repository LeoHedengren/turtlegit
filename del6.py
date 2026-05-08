import turtle
import random as rand

antal = int(input("Hur många figurer?"))

def trianglar(antal):
    t = turtle.Turtle()
    t.width(7)
    t.speed(100)
    for i in range(antal):
        t.pendown()
        for i in range(3):
            t.color(rand.choice(["blue","cyan", "magenta", "yellow", "green", "red", "black", "white"]))
            t.forward(30)
            t.right(120)
        t.penup()
        t.left(56)
        t.forward(178)

trianglar(antal)