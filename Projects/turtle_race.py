import turtle, time, random
from utils import *
import random



# Section 1 - Variables
# TODO - add starting values for all the variables
rng1min = 2
rng2min = 2
rng3min = 0
rng4min = 2

youwon = False
pwinner = ""

x1 = -200
y1 = 150
x2 = -200
y2 = 50
x3 = -250
y3 = -50
x4 = -200
y4 = -150


# Section 2 - Setup
# # TODO - use your own background, and set your four turtles to images of your choice
set_background("Track")
t1 = create_sprite("Orange_Horse",x1,y1)
t2 = create_sprite("White_Horse",x2,y2)
t3 = create_sprite("Disabled_Horse",x3,y3)
t4 = create_sprite("Black_Horse",x4,y4)


# # Section 3 - Racing
# # TODO - set how much each variable changes by and increase the number of repeats to at least 30
# # TODO - explain here which sprites are faster or slower

rng1 = random.randint(10, 70)
rng2 = random.randint(20, 70)
rng3 = random.randint(10, 20)
rng4 = random.randint(30, 60)

rng1 /= 10
rng2 /= 10
rng3 /= 10
rng4 /= 10

pwinner = input("Place your bets! Who do you think will win?(orange, white, gray, or black) ")

text1 = create_sprite("EMPTY", -150, 200)
text1.color("black")
text1.write("3!", font = ("Arial", 40, "normal"))
window.update()
time.sleep(1)
text1.goto(-50, 200)
text1.write("2!", font = ("Arial", 40, "normal"))
window.update()
time.sleep(1)
text1.goto(50, 200)
text1.write("1!", font = ("Arial", 40, "normal"))
window.update()
time.sleep(1)
text1.goto(150, 200)
text1.write("GO!", font = ("Arial", 40, "normal"))
window.update()
time.sleep(1)
text1.goto(150, 200)

for i in range(30):
    x1 += rng1
    x2 += rng2
    x3 += rng3
    x4 += rng4

    t1.goto(x1, y1)
    t2.goto(x2, y2)
    t3.goto(x3, y3)
    t4.goto(x4, y4)

    window.update()
    time.sleep(0.1)

# speed change loop
while 1 == 1:
    if x1 >= 200 or x2 >= 200 or x3 >= 200 or x4 >= 200:
        break

    print(rng1)
    rngl = (rng1 - 2) * 10
    rngl = int(rngl)
    print(rngl)
    rngh = (rng1 + 2) * 10
    rngh = int(rngh)
    rng1 = random.randint(rngl, rngh)

    rngl = (rng2 - 2) * 10
    rngl = int(rngl)
    print(rngl)
    rngh = (rng2 + 2) * 10
    rngh = int(rngh)
    rng1 = random.randint(rngl, rngh)

    rngl = (rng3 - 2) * 10
    rngl = int(rngl)
    print(rngl)
    rngh = (rng3 + 2) * 10
    rngh = int(rngh)
    rng1 = random.randint(rngl, rngh)

    rngl = (rng4 - 2) * 10
    rngl = int(rngl)
    print(rngl)
    rngh = (rng4 + 2) * 10
    rngh = int(rngh)
    rng1 = random.randint(rngl, rngh)

    rng1 /= 10
    rng2 /= 10
    rng3 /= 10
    rng4 /= 10

    for i in range(30):
        if rng1 <= rng1min:
            rng1 = rng1min
        x1 += rng1
        if rng2 <= rng2min:
            rng2 = rng2min
        x2 += rng2
        if rng3 <= rng3min:
            rng3 = rng3min
        x3 += rng3
        if rng4 <= rng4min:
            rng4 = rng4min
        x4 += rng4

        t1.goto(x1, y1)
        t2.goto(x2, y2)
        t3.goto(x3, y3)
        t4.goto(x4, y4)

        window.update()
        time.sleep(0.1)










if x3 >= x1 and x3 >= x2 and x3 >= x4:
    print("The Gray Horse won!")
    winner = 3
elif x1 >= x2 and x1 >= x3 and x1 >= x4:
    print("The Orange Horse won!")
    winner = 1
elif x2 >= x1 and x2 >= x3 and x2 >= x4:
    print("The White Horse won!")
    winner = 2
elif x4 >= x2 and x4 >= x3 and x1 >= x4:
    print("The Black Horse won!")
    winner = 4

if winner == 1:
        if pwinner == "orange" or pwinner == "Orange":
            youwon = True
if winner == 2:
        if pwinner == "white" or pwinner == "White":
            youwon = True
if winner == 3:
        if pwinner == "gray" or pwinner == "Gray":
            youwon = True
if winner == 4:
        if pwinner == "Black" or pwinner == "Black":
            youwon = True

if youwon == True:
    if winner == 3:
        print("...")
        time.sleep(2)
        print("...")
        time.sleep(2)
        print("...")
        time.sleep(2)
        print("how the hell did you win ts")
        time.sleep(5)
        # godly win
        print("GW")
    time.sleep(2)
    print("You Won!!!")
     

turtle.exitonclick()

