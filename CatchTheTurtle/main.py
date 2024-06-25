import turtle
import random

screen = turtle.Screen()
screen.bgcolor('#6c7929')
screen.title('- Catch The Turtle Game -')

score_turtle = turtle.Turtle()
countdown_turtle = turtle.Turtle()

topy = screen.window_height() / 2
topx = turtle.window_width() / 2

grid_size = 10
score = 0
game_over = False
FONT = ('Arial', 15, 'bold')
turtle_list = list()

txt = "Score: {}".format(score)


def setup_score_turtle():
    score_turtle.color("blue")
    score_turtle.hideturtle()
    y = topy * 0.90
    x = topx * -0.86
    score_turtle.penup()
    score_turtle.setpos(x,y)
    score_turtle.pendown()
    score_turtle.write(txt, move=False, align='center', font=FONT)


def make_turtle(x,y):
    t = turtle.Turtle()

    def handle_click(x,y):
        global score
        score+=1
        score_turtle.clear()
        score_turtle.write(arg="Score: {}".format(score), move=False, align='center', font=FONT)

    t.onclick(handle_click)
    t.penup()
    t.shape("turtle")
    t.shapesize(2,2)
    t.color("dark green")
    t.goto(grid_size*x, grid_size*y)
    turtle_list.append(t)


x_coordinates = [-20, -10, 0, 10, 20]
y_coordinates = [-20, -10, 0, 10]


def setup_turtles():
    for i in x_coordinates:
        for j in y_coordinates:
            make_turtle(i,j)


def hide_turtles():
    for t in turtle_list:
        t.hideturtle()


def show_turtles_randomly():
    if not game_over:
        hide_turtles()
        random.choice(turtle_list).showturtle()
        screen.ontimer(show_turtles_randomly, 450)


def countdown(time):
    global game_over
    countdown_turtle.hideturtle()
    countdown_turtle.color("blue")
    y = topy * 0.90
    x = topx * 0.80
    countdown_turtle.penup()
    countdown_turtle.setpos(x, y)
    countdown_turtle.pendown()
    countdown_turtle.clear()
    if time > 0:
        countdown_turtle.clear()
        countdown_turtle.write(arg="Time: {}".format(time), move=False, align='center', font=FONT)
        screen.ontimer(lambda: countdown(time - 1), 1000)
    else:
        game_over = True
        countdown_turtle.clear()
        hide_turtles()
        countdown_turtle.write(arg="Game Over !", move=False, align='center', font=FONT)


turtle.tracer(0)        # animation turtle geçişlerini yoksayar ve direkt oluşmasını sağlar

setup_score_turtle()
setup_turtles()
hide_turtles()
show_turtles_randomly()
countdown(10)

turtle.tracer(1)

turtle.mainloop()