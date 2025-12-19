# Section 1 - Your code
from utils import *
import random

rng1 = 0
rng2 = 0

set_background("Stars")


for i, 1 in 4:
    rng1 = random.randint(-200, 200)
    rng2 = random.randint(-200, 200)
    s1 = create_sprite("baag", rng1, rng2)

message1 = create_sprite("alien", -325,0)
message1.color("red")
message1.write("𒅒𒈔𒅒𒇫𒄆  𓁹 ✞𒀱✞ 𓁹  𒅒𒇫𒄆𒅒𒈔 ",font = ("Arial", 20, "normal"))
message1.hideturtle()


######################################################################


# Section 2 - Keeping the window open (DON'T CHANGE!!)
window.update()
turtle.exitonclick()