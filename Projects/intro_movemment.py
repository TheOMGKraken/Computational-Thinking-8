import time, turtle, random
from utils import *
# Section 1: Setup
set_background("castle")
s1 = create_sprite("farmer",0,-200)
s2 = create_sprite("srarmer", 0, 200)

s1y = 0
s1x = 0
s1uv = 0
md = 0

s2x = 0
s2y = 0


s1.color("red")


# Section 2: define controls
def move_up():
    global s1x, s1y, s1uv
    s1uv = 5

        
def move_down():
    global s1x, s1y, s1uv
    s1uv -= 15

    
def startmove_left():
    global s1x, s1y, md
    md = -1

def endmove_left():
    global s1x, s1y, md
    if md == -1:
        md = 0
    
def startmove_right():
    global s1x, s1y, md
    md = 1

def endmove_right():
    global s1x, s1y, md
    if md == 1:
        md = 0

def startdraw():
    s1.pendown()

def endraw():
    s1.penup()

def pencolor(color):
    s1.pencolor(f"{color}")


def penclear():
    s1.clear()


def up():
    global s2y, s2x
    s2y += 10
    s2x += 0

def down():
    global s2y, s2x
    s2y += -10
    s2x += 0

def left():
    global s2y, s2x
    s2y += 0
    s2x += -10

def right():
    global s2y, s2x
    s2y += 0
    s2x += 10

window.onkeypress(move_up, "w")
window.onkeypress(move_down, "s")
window.onkeypress(startmove_left, "a")
window.onkeyrelease(endmove_left, "a")
window.onkeypress(startmove_right, "d")
window.onkeyrelease(endmove_right, "d")
window.onkeypress(startdraw, "c")
window.onkeyrelease(endraw, "c")
window.onkeypress(lambda: pencolor("red") , "r")
window.onkeypress(lambda: pencolor("green"), "g")
window.onkeypress(penclear, "p")
window.onkeypress(up, "Up")
window.onkeypress(down, "Down")
window.onkeypress(left, "Left")
window.onkeypress(right, "Right")

# Section 3: define other controls
def hide():
    s1.hideturtle()
def show():
    s1.showturtle()

window.onkeypress(hide, "h")
window.onkeyrelease(show, "h")


# Section 4: game loop
window.listen()
for i in range(1000000000):

    if s1y <= -100 and s1uv <= 0:
        s1uv = 0
    else:
        s1uv -= 0.1

    s1y += s1uv

    s1x += md*1

    s1.goto(s1x, s1y)
    s2.goto(s2x, s2y)

    time.sleep(0.01)
    window.update()