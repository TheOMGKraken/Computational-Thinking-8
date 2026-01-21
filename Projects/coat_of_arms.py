# Section 1 - Your code
from utils import *
import random
import time

rng1 = 0
rng2 = 0

set_background("Stars")

set_background("underwater")

s11 = random.randint(-200, 200)
s12 = random.randint(-200, 200)
s1 = create_sprite("GermanyFlag", s11, s12)
s21 = random.randint(-200, 200)
s22 = random.randint(-200, 200)
s2 = create_sprite("SadGuy", s21, s22)
s31 = random.randint(-200, 200)
s32 = random.randint(-200, 200)
s3 = create_sprite("SoccerBall", s31, s32)

text = create_sprite("EMPTY", -100,-50)
text.color("black")
text.write("3!", font = ("Arial", 40, "normal"))
window.update()
time.sleep(1)
text.write("2!", font = ("Arial", 40, "normal"))
window.update()
time.sleep(1)
text.write("1!", font = ("Arial", 40, "normal"))
window.update()
time.sleep(1)
text.write("!", font = ("Arial", 40, "normal"))
window.update()
time.sleep(1)
# message1.write("𒅒𒈔𒅒𒇫𒄆©  𓁹 ✞𒀱✞ 𓁹  ©𒅒𒇫𒄆𒅒𒈔 ",font = ("Arial", 20, "normal"))

message1.hideturtle()

window.update()

s1sd = 1
s1vd = 1

while 1 == 1:
    time.sleep(0.1)
    
#   s1sd means s1 side direction
    if s11 >= 300:
        s1sd = -1
    elif s11 <= -300:
        s1sd = 1
#   s1vd means s1 vertical direction
    if s12 >= 250:
        s1vd = -1
    elif s12 <= -250:
        s1vd = 1
    
    s11 += 5 * s1sd
    s12 += 5 * s1vd


    s1 = create_sprite("GermanyFlag", s11, s12)
    s2 = create_sprite("SadGuy", s21, s22)
    s3 = create_sprite("SoccerBall", s31, s32)


    window.update






######################################################################


# Section 2 - Keeping the window open (DON'T CHANGE!!)
window.update()
turtle.exitonclick()