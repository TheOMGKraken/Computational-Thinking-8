import time
import sys
import random



rng = 0
calc = 0
code = "yay"
codes = []
var = 0
mainvar = 0
tyme = 0
zombie = "zombie"

while len(code) != 0:
    code = input("input codes here ")
    codes.append(f"{code}")

if "ntb" in codes:
    zombie = "bee"

mainvar = input("do you like chose your own adventures?")
if mainvar != "yes" and mainvar != "y" and mainvar != "yeah" and mainvar != "yep" and not "skip" in codes:
    print("well thats too bad")
    time.sleep(7)
if not "skip" in codes:
    print("in this cyoa you will be asked a variety of questions")
    time.sleep(2)
    print("for every question, input 1 or 2")
    time.sleep(2)
    print("understand?")
    time.sleep(0.3)
    print("good")
    time.sleep(1)
    print("if you are asked a yes or no question, 1 is no and 2 is yes")
    time.sleep(3)
    print("if you are asked a non yes or no question, 1 is the first option and 2 is the second option")
    time.sleep(3)
mainvar = 0
print("lets get started!")
time.sleep(3)
while var != 1:
    if tyme < 1:
        print(f"you are in the 5th floor of the middle school and you hear that there is a {zombie} in the 4th floor of the upper school!")
    elif tyme < 4:
        print("you are now in the atrium")
        time.sleep(1)
    elif tyme >= 4:
        print(f"unfortunately, you took too long, and now there are {zombie}s on your floor")
        time.sleep(2)
        print("all the classrooms are barricaded")
        time.sleep(2)
        print(f"you get killed by a {zombie}")
        time.sleep(2)
        rng = random.randint(1, 30)
        if rng > 5:
            raise SystemExit("you died, in a slow way")
        else:
            print("...")
            time.sleep(2)
            raise SystemExit("skip")
    time.sleep(3)
    mainvar = input("do you go to 1: the stairs or 2: try to barricade a classroom? ")
    if mainvar != "1" and mainvar != "2":
        print("die")
        raise SystemError("you didn't chose 1 or 2")
    if mainvar == "1":
        if tyme == 2:
            print(f"the stairs are pretty full of {zombie}s")
            time.sleep(2)
            print("you walk back")
            time.sleep(1)
            tyme += 1
            continue
        elif tyme == 3:
            print(f"the stairs are absolutely packed with {zombie}s")
            time.sleep(1)
            print("you run back")
            time.sleep(0.5)
            tyme += 1
            continue
        print("the stairs are packed full of people")
        time.sleep(2)
        mainvar = 0
        mainvar = input("do you try 1: jumping down the stairs or 2: do you return to the atrium? ")
        if mainvar != "1" and mainvar != "2":
            print("die")
            raise SystemExit("you didn't chose 1 or 2")
        if mainvar == "1":
            print("you try jumping down the stairs")
            time.sleep(2)
            print("... wait, you thought this would work?")
            time.sleep(2)
            print(f"you break your legs on the landing and get trampled to death by a hoard of people running from a {zombie} at the bottom")
            time.sleep(5)
            raise SystemExit("you died, in a stupid way")
        if mainvar == "2":
            mainvar = 0
            tyme += 1
            continue
    if mainvar == "2":
        mainvar = 0
        mainvar = input("which classroom are you going to barricade yourself in? 50# ")
        if mainvar != "1" and mainvar != "2" and mainvar != "3" and mainvar != "4" and mainvar !=  "5":
            print(f"class {mainvar} isn't a class")
            time.sleep(3)
            print("die")
            time.sleep(3)
            raise SystemExit("idiot")
        elif mainvar == "1":
            print("you barricade yourself in the english room")
            time.sleep(2)
            print("unfortunately, you had a essay due that day")
            time.sleep(2)
            rng = random.randint(1, 30)
            if > 5:
                raise SystemExit("you died, in a sad way")
            else:
                time.sleep(2)
                print("...")
                time.sleep(2)
                raise SystemExit("ntb")
        elif mainvar == "2":
            print("you barricade yourself in the history room")
            time.sleep(2)
            print("you wait there for a while")
            mainvar = input("do you read a book? ")
            if mainvar != "1" and mainvar != "2":
                print("die")
                raise SystemExit("you didn't chose 1 or 2")
            if mainvar == "1":
                calc = 20-tyme*5
                time.sleep(calc)
            if mainvar == "2":
                time.sleep(1)
            mainvar = 0
            while 1 == 1:
                mainvar = input(f"{zombie}s are trying to break through! do you 1 try to reinforce the room or 2 try to jump out of the window ")
                if mainvar != "1" and mainvar != "2":
                    print("die")
                    raise SystemExit("you didn't chose 1 or 2")
                if mainvar == "1":
                    print("you can barely hold them in")
                    time.sleep(1)
                    tyme += 1
                    continue
                if mainvar == "2":
                    if tyme >= 4:
                        print("you try to jump out the window")
                        time.sleep(1)
                        print(f"but the {zombie}s get to you first and kills you")
                    else:
                        print("you jump out the window!")
                        time.sleep(2)
                        print("as you fall, you see everything")
                        time.sleep(3)
                        print("your whole life lead up to this")
                        time.sleep(3)
                        print("as you get near the ground, you close your eyes")
                        if not "lucky" in codes:
                            rng = random.randint(1,30)
                            if rng <= 4:
                                print("you landed in a bush! you escaped!")
                                time.sleep(4)
                                rng = random.randint(1, 30)
                                if rng > 7:
                                    raise SystemExit("you lived, in a lucky way")
                                else:
                                    print("...")
                                    time.sleep(2)
                                    raise SystemExit("lucky")
                            else:
                                print("you hit the ground")
                                time.sleep(1)
                                raise SystemExit("you died, in a splaty way")
                        else:
                            print("you landed in a bush! you escaped!")
                            time.sleep(4)
                            raise SystemExit("you lived, in a lucky way")
        elif mainvar == "3":
            print("you  the")
            




