import turtle

def draw_squar(turtle1):
    for i in range(0,4):
        turtle1.forward(200)
        turtle1.right(90)
def draw_shap():
    window = turtle.Screen()
    window.bgcolor("green")
    amr = turtle.Turtle()
    amr.shape("turtle")
    amr.color("red")
    draw_squar(amr)
    cat=turtle.Turtle()
    cat.shape("triangle")
    cat.color("yellow")
    for i in range (0,3):
        amr.left(120)
        amr.forward(200)
    angi=turtle.Turtle()
    angi.shape("arrow")
    angi.color("blue")
    angi.circle(100)
    window.exitonclick()
draw_shap()