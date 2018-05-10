import turtle
def draw_squar(turtle1):
    for i in range(0,4):
        turtle1.forward(100)
        turtle1.right(90)
def draw_shap():
    window = turtle.Screen()
    window.bgcolor("green")
    amr = turtle.Turtle()
    amr.shape("turtle")
    amr.color("red")
    amr.speed(90)

    for i in range (0,361,5):
        amr.setheading(i)
        draw_squar(amr)
    amr.right(90)
    amr.color("orange")
    amr.pensize(2)
    amr.forward(250)

    window.exitonclick()
draw_shap()