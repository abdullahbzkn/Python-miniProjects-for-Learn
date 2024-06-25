import turtle
from random import randint
drawing_board = turtle.Screen()
drawing_board.bgcolor("Black")
drawing_board.title("Python Turtle")

turtle_instance = turtle.Turtle()
'''
Ngen
def leftgo(ngen):
    for i in range(ngen):
        angle = 360 / ngen
        turtle_instance.forward(80)
        turtle_instance.left(angle)
inp = int(input("Çizdirmek istediğiniz şeklin kenar sayısını giriniz : "))
leftgo(inp)
turtle.done()
'''
'''
Star
for i in range(5):
    turtle_instance.forward(200)
    turtle_instance.right(144)
turtle.done()
'''
'''
mikroişlemci çizdir laksjfksdfjdf
x = 100
for i in range(50):
    turtle_instance.forward(x)
    turtle_instance.right(90)
    x-=5
turtle.done()
'''
'''
renkler = ["blue","brown","white","pink","yellow","light green","purple"]

x = 120

while x>0:
    y = randint(0,6)
    turtle_instance.forward(x)
    turtle_instance.right(90)
    turtle_instance.color(renkler[y])
    x-=5

turtle.done()
'''

renkler = ["blue","brown","white","pink","yellow","light green","purple","orange"]
turtle_instance.color("white")
turtle.speed("fastest")
for i in range(10):
    y = randint(0,7)
    turtle_instance.color(renkler[y])
    # rand lib kullanmadan da yapılabilir
    # turtle_instance.color(renkler[y%8])
    # y+=1
    turtle_instance.circle(10*i)
    turtle_instance.circle(-10*i)
    turtle_instance.left(i)
turtle.done()