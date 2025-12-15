import sys

zero = 0
one = 0
two = 0
asking = 0
answer = 0
codes = []
code = "tomgk"

while len(code) != 0:
    code = input("input codes here ")
    codes.append(f"{code}")

asking = 1
answer = input("what is the square root of two? A. 2 B. 4 C. 1.41 ")
while asking == 1:
    if answer == "a" or answer == "A":
        zero += 1
        asking = 0
        continue
    elif answer == "b" or answer == "B":
        one += 1
        asking = 0
        continue
    elif answer == "c" or answer == "C":
        two += 1
        asking = 0
        continue
    else:
        answer = input("bro chose again: A. 2 B. 4 C. 1.41 ")
        continue

asking = 1
answer = input("what is π (closest answer)? A. 3.14 B. 3.24 C. 3 ")
while asking == 1:
    if answer == "a" or answer == "A":
        two += 1
        asking = 0
        continue
    elif answer == "b" or answer == "B":
        one += 1
        asking = 0
        continue
    elif answer == "c" or answer == "C":
        zero += 1
        asking = 0
        continue
    else:
        answer = input("bro chose again: A. 3.14 B. 3.24 C. 3 ")
        continue

asking = 1
answer = input("how many continents are there? A. 9 B. 7 C. 8 ")
while asking == 1:
    if answer == "a" or answer == "A":
        zero += 1
        asking = 0
        continue
    elif answer == "b" or answer == "B":
        two += 1
        asking = 0
        continue
    elif answer == "c" or answer == "C":
        one += 1
        asking = 0
        continue
    else:
        answer = input("bro chose again: A. 9 B. 7 C. 8 ")
        continue

asking = 1
answer = input("how many people are there (billions)? A. 8 B. 9 C. 6 ")
while asking == 1:
    if answer == "a" or answer == "A":
        two += 1
        asking = 0
        continue
    elif answer == "b" or answer == "B":
        one += 1
        asking = 0
        continue
    elif answer == "c" or answer == "C":
        zero += 1
        asking = 0
        continue
    else:
        answer = input("bro chose again: A. 8 B. 9 C. 6 ")
        continue

asking = 1
answer = input("how many people die per second? A. 1.9 B. 2.6 C. 0.7 ")
while asking == 1:
    if answer == "a" or answer == "A":
        two += 1
        asking = 0
        continue
    elif answer == "b" or answer == "B":
        one += 1
        asking = 0
        continue
    elif answer == "c" or answer == "C":
        zero += 1
        asking = 0
        continue
    else:
        answer = input("bro chose again: A. 1.9 B. 2.6 C. 0.7 ")
        continue

asking = 1
answer = input("how many seconds are in a day? A. 87300 B. 86400 C. 76400 ")
while asking == 1:
    if answer == "a" or answer == "A":
        one += 1
        asking = 0
        continue
    elif answer == "b" or answer == "B":
        two += 1
        asking = 0
        continue
    elif answer == "c" or answer == "C":
        zero += 1
        asking = 0
        continue
    else:
        answer = input("bro chose again: A. 87300 B. 86400 C. 76400 ")
        continue


if "1" in codes and not "2" in codes and not "3" in codes and not "4" in codes and not "5" in codes:
    zero = 6
    two = 0
    one = 0
if not "1" in codes and "2" in codes and not "3" in codes and not "4" in codes and not "5" in codes:
    zero = 2
    two = 2
    one = 2
if not "1" in codes and not "2" in codes and "3" in codes and not "4" in codes and not "5" in codes:
    zero = 0
    two = 0
    one = 6
if not "1" in codes and not "2" in codes and not "3" in codes and "4" in codes and not "5" in codes:
    zero = 3
    two = 3
    one = 0
if not "1" in codes and not "2" in codes and not "3" in codes and not "4" in codes and "5" in codes:
    zero = 0
    two = 6
    one = 0

input(f"your scores were {zero} questions wrong, {one} question semi correct, and {two} questions correct")



if zero > 3:
    input("you got most of the questions incorrect")
elif one == two == zero:
    input("you got 2 correct answers, 2 semi correct answers, and 2 wrong answers. you are the most average person")
elif one > 3 or zero == two != one:
    input("you did average")
elif two > 3:
    input("you got most of the questions correct")





