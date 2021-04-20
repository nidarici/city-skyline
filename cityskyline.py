import turtle


# to set the layout
def layout():
    pointer.begin_fill()
    pointer.color("black", "black")
    pointer.forward(400)
    pointer.left(90)
    pointer.forward(400)
    pointer.left(90)
    pointer.forward(400)
    pointer.left(90)
    pointer.forward(400)
    pointer.left(90)
    pointer.end_fill()


# function to draw the layout of the building
def buildings():
    pointer.begin_fill()
    pointer.color("brown", "brown")
    pointer.left(90)
    pointer.forward(100)
    pointer.right(90)
    pointer.forward(50)
    pointer.left(90)
    pointer.forward(50)
    pointer.right(90)
    pointer.forward(50)
    pointer.left(90)
    pointer.forward(180)
    pointer.right(90)
    pointer.forward(100)
    pointer.right(90)
    pointer.forward(145)
    pointer.left(90)
    pointer.forward(50)
    pointer.left(90)
    pointer.forward(70)
    pointer.right(90)
    pointer.forward(70)
    pointer.right(90)
    pointer.forward(60)
    pointer.left(90)
    pointer.forward(30)
    pointer.right(90)
    pointer.forward(50)
    pointer.left(90)
    pointer.forward(50)
    pointer.right(90)
    pointer.forward(145)
    pointer.right(90)
    pointer.forward(400)
    pointer.end_fill()


# function to draw the window
def window():
    pointer.begin_fill()
    pointer.color("white", "white")
    pointer.right(90)
    pointer.forward(10)
    pointer.right(90)
    pointer.forward(10)
    pointer.right(90)
    pointer.forward(10)
    pointer.right(90)
    pointer.forward(10)
    pointer.end_fill()


# function to draw the windows on the building
def windows():
    pointer.up()
    pointer.setposition(-140, -100)
    pointer.down()
    window()

    pointer.up()
    pointer.setposition(-100, 50)
    pointer.down()
    window()

    pointer.up()
    pointer.setposition(-100, 80)
    pointer.down()
    window()

    pointer.up()
    pointer.setposition(-40, 10)
    pointer.down()
    window()

    pointer.up()
    pointer.setposition(-40, -140)
    pointer.down()
    window()

    pointer.up()
    pointer.setposition(35, 10)
    pointer.down()
    window()


# function to draw the star
def star():
    pointer.begin_fill()
    pointer.color("white", "white")
    for i in range(1):
        pointer.forward(2)
        pointer.right(144)
        pointer.end_fill()


# function to draw the stars on the layout
def stars():
    pointer.up()
    pointer.setposition(150, 150)
    pointer.down()
    star()

    pointer.up()
    pointer.setposition(80, 125)
    pointer.down()
    star()

    pointer.up()
    pointer.setposition(110, 50)
    pointer.down()
    star()

    pointer.up()
    pointer.setposition(-135, 145)
    pointer.down()
    star()

    pointer.up()
    pointer.setposition(-140, 40)
    pointer.down()
    star()

    pointer.up()
    pointer.setposition(-180, -80)
    pointer.down()
    star()


pointer = turtle.Turtle()
pointer.pensize(3)
pointer.up()
pointer.setposition(-220, -220)
pointer.down()

layout()
buildings()
windows()
stars()

pointer.up()
pointer.setposition(-220, -220)
pointer.down()
pointer.begin_fill()
pointer.color("brown", "brown")
pointer.end_fill()
pointer.left(180)

turtle.hideturtle()
