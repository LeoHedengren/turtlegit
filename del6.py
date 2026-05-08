import turtle

antal = int(input("Hur många figurer?"))

def trianglar(antal):
    t = turtle.Turtle()
    t.color("blue")
    t.width(7)
    t.speed(100)
    for i in range(antal):
        t.pendown()
        for i in range(3):
            t.forward(30)
            t.right(120)
        t.penup()
        t.left(56)
        t.forward(178)

trianglar(antal)