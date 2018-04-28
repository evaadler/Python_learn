import turtle

def draw_square():
    window = turtle.Screen()
    window.bgcolor("red")

    brad = turtle.Turtle()


    for i in range(1, 5):
        brad.forward(100)
        brad.right(90)

    brad.circle(10)

    window.exitonclick()

draw_square()