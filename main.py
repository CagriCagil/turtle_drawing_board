import turtle


while True:
    try:
        lenght = int(input("Enter how many pixels you want to move forward"))
        break
    except:
        print("please enter a number value")

while True:
    try:
        angle = int(input("enter rotation angle"))
        break
    except:
        print("please enter a number value")

while True:
    try:
        radius = int(input("Enter radius information to draw a circle"))
        break
    except:
        print("please enter a number value")


turtle_screen = turtle.Screen()
turtle_screen.bgcolor("#EBE8B3")
turtle_screen.title("drawing board")

turtle_instance = turtle.Turtle()
turtle_instance.color("#C21D1A")
turtle_instance.speed(0)

def turtle_forward():
    turtle_instance.forward(lenght)

def turtle_angle_right():
    turtle_instance.right(angle)
def turtle_angle_left():
    turtle_instance.left(angle)

def clean_screen():
    turtle_instance.clear()

def return_home():
    turtle_instance.home()

def turtle_pen_up():
    turtle_instance.penup()

def turtle_pen_down():
    turtle_instance.pendown()

def turtle_circle():
    turtle_instance.circle(radius)

turtle_screen.listen()
turtle_screen.onkey(fun=turtle_forward, key="w")
turtle_screen.onkey(fun=turtle_angle_right, key="Right")  # "Down" yerine "Right" kullanıldı.
turtle_screen.onkey(fun=turtle_angle_left, key="Left")  # "Up" yerine "Left" kullanıldı.
turtle_screen.onkey(fun=clean_screen, key ="c" )
turtle_screen.onkey(fun=return_home, key="h")
turtle_screen.onkey(fun=turtle_pen_up, key="u")
turtle_screen.onkey(fun=turtle_pen_down, key="d")
turtle_screen.onkey(fun=turtle_circle, key="x")


turtle_screen.mainloop()