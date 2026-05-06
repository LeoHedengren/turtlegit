import turtle

def rita_kvadrat(sida):
    t = turtle.Turtle()
    for i in range(8):
        for i in range(4):
            t.forward(sida)
            t.right(90)
        t.penup()
        t.left(45)
        t.forward(45)
        t.pendown()

rita_kvadrat(30)


