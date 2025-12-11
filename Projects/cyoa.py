import time
import sys

codes = 0
var = 0
mainvar = 0
tyme = 0
zombie = 0

codes = input("input codes here ")
if codes == "ntb":
    zombie = "bee"
if codes != "ntb":
    zombie = "zombie"
mainvar = input("do you like chose your own adventures?")
if mainvar != "yes" and mainvar != "y" and mainvar != "yeah" and mainvar != "yep" and codes != "skip":
    print("well thats too bad")
    time.sleep(7)
if codes != "skip":
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
        raise SystemExit("you died, in a slow way")
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
        if mainvar == "1":
            print("you barricade yourself in the english room")
            time.sleep(2)
            print("unfortunately, you had a essay due that day")
            time.sleep(2)
            raise SystemExit("you died, in a sad way")
