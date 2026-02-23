import turtle, time, random, math
from utils import *

# goal of the game is to get as many onions as possible (like cookie clicker)

# Section 1 - setup
# TODO - set a background using set_background()
set_background("Farm")
# TODO - create at least two variables and set their starting value. ex: cookies = 0

rng = 0
onions = 0
Monions = 0
Gonions = 0
marmalade = 0
farmercost = 10
farmers = 0
shronionfarmercost = 100
shronionfarmers = 0
I = 0

# OPTIONAL: use this invisible alien to say a message

message_sprite = create_sprite("EMPTY", -200,200)
message_sprite.hideturtle()
farmersaysprite = create_sprite("EMPTY", -250, -170)
shronionsaysprite = create_sprite("EMPTY", 150, -10)
marmaladesaysprite = create_sprite("EMPTY", -250, -10)
shronionfarmersaysprite = create_sprite("EMPTY", 10, -170)

onionsprite = create_sprite("Onion", 0, 0)
shronionsprite = create_sprite("Shronion", 200, 0)
marmaladesprite = create_sprite("marmalade", -200, 0)
farmersprite = create_sprite("farmer", -200, -200)
shronionfarmersprite = create_sprite("srarmer", 150, -200)

# Section 2 - controls
# TODO - define an action. ex: def my_control()



def onM1click(x, y):
    #e
    global onions, Monions, Gonions, marmalade, farmercost, farmers, shronionfarmers, shronionfarmercost

    if x >= -50 and x <= 50 and y >= -50 and y <= 50 :

        
        
        rng = random.randint(1, 10000)

        if rng != 1:
            onions += (marmalade + 1) * 1
        else:
            Gonions += 1
            

    elif x >= 150 and x <= 250 and y >= -50 and y <= 50:
        if onions >= 100:
            onions -= 100
            Monions += 1

    elif x >= -220 and x <= -180 and y >= -20 and y <= 20:
        if Monions >= 10:
            Monions -= 10
            marmalade += 1
    
    elif x >= -250 and x <= -150 and y <= -70:
        if onions >= farmercost:
            onions -= farmercost
            farmers += 1
            farmercost *= 1.1
            farmercost = int(farmercost)
    
    elif x >= 50 and x <= 150 and y <= -70:
        if Monions >= shronionfarmercost:
            Monions -= shronionfarmercost
            shronionfarmers += 1
            shronionfarmercost *= 1.1
            shronionfarmercost = int(shronionfarmercost)





def onEclick():
    global onions, Monions, onionmarmalade

    if onions >= 100:
            onions -= 100
            Monions += 1

    
    
# TODO - choose a key to do the action. ex: window.onkeypress(my_control, "space")

window.onclick(onM1click)
window.onkeypress(onEclick, "e")

# TODO - make a second control





# Section 3 - game loop
window.listen()
while 1 == 1:
    
    I += 1

    if I % 25 == 0:
        for x in range(farmers):
            rng = random.randint(1,2)
            if rng == 1:
                onions += 0.5

        for x in range(shronionfarmers):
            rng = random.randint(1,2)
            if rng == 1:
                Monions += 0.5
        
    onions = math.ceil(onions)
    Monions = math.ceil(Monions)

        

    # TODO - put any automatic actions here


    # OPTIONAL - use the message sprite to say a message
    message_sprite.clear()
    if Gonions == 0:
        message_sprite.write(f"{onions} onions {Monions} shronions")
    else:
        message_sprite.write(f"{onions} onions {Gonions} golden onions {Monions} Shronions")

    farmersaysprite.clear()
    farmersaysprite.color("white")
    farmersaysprite.write(f"cost: {farmercost} onions", font = ("Arial", 10, "normal"))


    shronionfarmersaysprite.clear()
    shronionfarmersaysprite.color("white")
    shronionfarmersaysprite.write(f"cost: {shronionfarmercost} Shronions", font = ("Arial", 10, "normal"))


    shronionsaysprite.clear()
    shronionsaysprite.color("black")
    shronionsaysprite.write(f"cost: 100 onions", font = ("Arial", 10, "normal"))


    marmaladesaysprite.clear()
    marmaladesaysprite.color("black")
    marmaladesaysprite.write(f"cost: 10 Shronions", font = ("Arial", 10, "normal"))

    time.sleep(0.01)
    window.update()