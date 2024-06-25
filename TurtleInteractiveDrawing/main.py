import turtle

drawing_board = turtle.Screen()
drawing_board.bgcolor('light blue')
drawing_board.title('DRAWING BOARD')

turtle_instance = turtle.Turtle()


def turtle_forward():
    turtle_instance.forward(80)


def rotate_angle_left():
    turtle_instance.setheading(turtle_instance.heading() + 10)
    # turtle_instance.left(10)


def rotate_angle_right():
    turtle_instance.setheading(turtle_instance.heading() - 10)
    # turtle_instance.right(10)


def clear_screen():
    turtle_instance.clear()


def turtle_return_home():
    turtle_pen_up()
    turtle_instance.home()
    turtle_pen_down()


def turtle_pen_up():
    turtle_instance.penup()


def turtle_pen_down():
    turtle_instance.pendown()


drawing_board.listen()
drawing_board.onkey(key="space", fun=turtle_forward)
drawing_board.onkey(key="Down", fun=rotate_angle_right)
drawing_board.onkey(key="Up", fun=rotate_angle_left)
drawing_board.onkey(key="c", fun=clear_screen)
drawing_board.onkey(key="C", fun=clear_screen)
drawing_board.onkey(key="h", fun=turtle_return_home)
drawing_board.onkey(key="H", fun=turtle_return_home)
drawing_board.onkey(key="w", fun=turtle_pen_up)
drawing_board.onkey(key="W", fun=turtle_pen_up)
drawing_board.onkey(key="q", fun=turtle_pen_down)
drawing_board.onkey(key="Q", fun=turtle_pen_down)

turtle.mainloop()