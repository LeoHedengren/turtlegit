import turtle

antal = int(input("Hur många figurer?"))

def trianglar(antal):
    t = turtle.Turtle()
    t.color("blue")
    for i in range(antal):
        t.pendown()
        for i in range(3):
            t.forward(30)
            t.right(60)
        t.penup()
        t.left(30)
        t.forward(25)

trianglar(antal)