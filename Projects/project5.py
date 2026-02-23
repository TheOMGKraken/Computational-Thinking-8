import time, turtle, random
from utils import *
# Section 1: Setup

# goal is to reach the end (when attacks stop coming)

floorbrick = create_sprite("brick", 0, -260)
s1 = create_sprite("Farmer", 0,-200)
narrator = create_sprite("EMPTY", -200 , 200)

looop = True
dontcheckthis = 0

gravity = 0.1
dangers = []
onground = True
I = 0
s1y = 0
s1x = 0
s1uv = 0
md = 0
event = 0

s2x = 0
s2y = 0


s1.color("red")


# Section 2: define controls
def move_up():
    global s1x, s1y, s1uv, onground
    if onground == True:
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

def doyoubeliveingravity():
    global gravity
    gravity = 0

def madeinheaven():
    global gravity
    gravity = 0.1

window.onkeypress(move_up, "w")
window.onkeypress(move_down, "s")
window.onkeypress(startmove_left, "a")
window.onkeyrelease(endmove_left, "a")
window.onkeypress(startmove_right, "d")
window.onkeyrelease(endmove_right, "d")
window.onkeypress(doyoubeliveingravity, "p")
window.onkeyrelease(madeinheaven, "p")

# Section 3: define other controls
def hide():
    s1.hideturtle()
def show():
    s1.showturtle()

window.onkeypress(hide, "h")
window.onkeyrelease(show, "h")


# Section 4: game loop
window.listen()
while looop == True:

    onground = False

    narrator.clear()
    I += 1

    if I <= 500:
        narrator.write("welcome to THE GAME", font = ("Arial", 30, "normal"))
    elif I < 1000:
        narrator.write("this game is very hard", font = ("Arial", 30, "normal"))
    elif I < 1050:
        narrator.write("press w to jump and a and d to move sideways", font = ("Arial", 20, "normal"))
    elif I < 1051:
        spikewall = create_sprite("spikewall", 0, 500)
        dangers.append(spikewall)
    elif I < 1300:
        narrator.write("hey btw you can double jump", font = ("Arial", 30, "normal"))
        dontcheckthis = 1
    elif I < 1400:
        dontcheckthis = 1
    elif I < 1401:
        lazer = create_sprite("Lazer", 100, 0)
        dangers.append(lazer)
    elif I < 1600:
        dontcheckthis = 1
    elif I < 1601:
        lazer = create_sprite("Lazer", -100, 0)
        dangers.append(lazer)

    

    for spikewall in dangers:
        swy = spikewall.ycor()
        swx = spikewall.xcor()
        if swy > -50:
            swy -= 50
        else:
            swy = -50
        
        spikewall.goto(swx, swy)

        if s1x > swx - 130 and s1x < swx + 130 and s1y < swy and s1y > swy - 20 and s1y > swy - 40:
            print("died to spikewall")
            looop = False
        if s1x > swx - 130 and s1x < swx + 130 and s1y > swy + -10 and s1y < swy + 10:
            onground = True
            s1y = swy + 10

    for lazer in dangers:
        ly = lazer.ycor()
        lx = lazer. xcor()

        if s1x > lx - 50 and s1x < lx + 50 and s1y > ly - 2000 and s1y < ly + 2000:
            print("died to lazer")
            looop = False
        
        ly -= 100
        lazer.goto(lx, ly)

    if s1x > -130 and s1x < 130 and s1y < -100 and s1y > -120:
        s1y = -100
        onground = True
    

    if s1y < -300:
        looop = False

    # player movement (no touchy)
    if 1 == 1:
        if onground == True:
            if s1uv <= 0:
                s1uv = 0
        else:
            s1uv -= gravity

        s1y += s1uv

        s1x += md*3

        s1.goto(s1x, s1y)

    time.sleep(0.01)
    window.update()