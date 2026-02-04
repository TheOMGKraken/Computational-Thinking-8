import random
# list  of words: "About", "Alert", "Argue", "Beach", "Above", "Alike", "Arise", "Began", "Abuse", "Alive", "Array", "Begin", "Actor", "Allow", "Aside", "Begun", "Acute", "Alone", "Asset", "Being", "Admit", "Along", "Audio", "Below", "Adopt", "Alter", "Audit", "Bench", "Adult", "Among", "Avoid", "Billy", "After", "Anger", "Award", "Birth", "Again", "Angle", "Aware", "Black", "Agent", "Angry", "Badly", "Blame", "Agree", "Apart", "Baker", "Blind", "Ahead", "Apple", "Bases", "Block", "Alarm", "Apply", "Basic", "Blood", "Album", "Arena", "Basis", "Board", "Boost", "Buyer", "China", "Cover", "Booth", "Cable", "Chose", "Craft", "Bound", "Calif", "Civil", "Crash", "Brain", "Carry", "Claim", "Cream", "Brand", "Catch", "Class", "Crime", "Bread", "Cause", "Clean", "Cross", "Break", "Chain", "Clear", "Crowd", "Breed", "Chair", "Click", "Crown", "Brief", "Chart", "Clock", "Curve", "Bring", "Chase", "Close", "Cycle", "Broad", "Cheap", "Coach", "Daily", "Broke", "Check", "Coast", "Dance", "Brown", "Chest", "Could", "Dated", "Build", "Chief", "Count", "Dealt", "Built", "Child", "Court", "Death", "Debut", "Entry", "Forth", "Group", "Delay", "Equal", "Forty", "Grown", "Depth", "Error", "Forum", "Guard", "Doing", "Event", "Found", "Guess", "Doubt", "Every", "Frame", "Guest", "Dozen", "Exact", "Frank", "Guide", "Draft", "Exist", "Fraud", "Happy", "Drama", "Extra", "Fresh", "Harry", "Drawn", "Faith", "Front", "Heart", "Dream", "False", "Fruit", "Heavy", "Dress", "Fault", "Fully", "Hence", "Drill", "Fibre", "Funny", "Night", "Drink", "Field", "Giant", "Horse", "Drive", "Fifth", "Given", "Hotel", "Drove", "Fifty", "Glass", "House", "Dying", "Fight", "Globe", "Human", "Eager", "Final", "Going", "Ideal", "Early", "First", "Grace", "Image", "Earth", "Fixed", "Grade", "Index", "Eight", "Flash", "Grand", "Inner", "Elite", "Fleet", "Grant", "Input", "Empty", "Floor", "Grass", "Issue", "Enemy", "Fluid", "Great", "Irony", "Enjoy", "Focus", "Green", "Juice", "Enter", "Force", "Gross", "Joint", "Judge", "Metal", "Media", "Newly", "Known", "Local", "Might", "Noise", "Label", "Logic", "Minor", "North", "Large", "Loose", "Minus", "Noted", "Laser", "Lower", "Mixed", "Novel", "Later", "Lucky", "Model", "Nurse", "Laugh", "Lunch", "Money", "Occur", "Layer", "Lying", "Month", "Ocean", "Learn", "Magic", "Moral", "Offer", "Lease", "Major", "Motor", "Often", "Least", "Maker", "Mount", "Order", "Leave", "March", "Mouse", "Other", "Legal", "Music", "Mouth", "Ought", "Level", "Match", "Movie", "Paint", "Light", "Mayor", "Needs", "Paper", "Limit", "Meant", "Never", "Party", "Peace", "Power", "Radio", "Round", "Panel", "Press", "Raise", "Route", "Phase", "Price", "Range", "Royal", "Phone", "Pride", "Rapid", "Rural", "Photo", "Prime", "Ratio", "Scale", "Piece", "Print", "Reach", "Scene", "Pilot", "Prior", "Ready", "Scope", "Pitch", "Prize", "Refer", "Score", "Place", "Proof", "Right", "Sense", "Plain", "Proud", "Rival", "Serve", "Plane", "Prove", "River", "Seven", "Plant", "Queen", "Quick", "Shall", "Plate", "Sixth", "Stand", "Shape", "Point", "Quiet", "Roman", "Share", "Pound", "Quite", "Rough", "Sharp", "Sheet", "Spare", "Style", "Times", "Shelf", "Speak", "Sugar", "Tired", "Shell", "Speed", "Suite", "Title", "Shift", "Spend", "Super", "Today", "Shirt", "Spent", "Sweet", "Topic", "Shock", "Split", "Table", "Total", "Shoot", "Spoke", "Taken", "Touch", "Short", "Sport", "Taste", "Tough", "Shown", "Staff", "Taxes", "Tower", "Sight", "Stage", "Teach", "Track", "Since", "Stake", "Teeth", "Trade", "Sixty", "Start", "Texas", "Treat", "Sized", "State", "Thank", "Trend", "Skill", "Steam", "Theft", "Trial", "Sleep", "Steel", "Their", "Tried", "Slide", "Stick", "Theme", "Tries", "Small", "Still", "There", "Truck", "Smart", "Stock", "These", "Truly", "Smile", "Stone", "Thick", "Trust", "Smith", "Stood", "Thing", "Truth", "Smoke", "Store", "Think", "Twice", "Solid", "Storm", "Third", "Under", "Solve", "Story", "Those", "Undue", "Sorry", "Strip", "Three", "Union", "Sound", "Stuck", "Threw", "Unity", "South", "Study", "Throw", "Until", "Space", "Stuff", "Tight", "Upper", "Upset", "Whole", "Waste", "Wound", "Urban", "Whose", "Watch", "Write", "Usage", "Woman", "Water", "Wrong", "Usual", "Train", "Wheel", "Wrote", "Valid", "World", "Where", "Yield", "Value", "Worry", "Which", "Young", "Video", "Worse", "While", "Youth", "Virus", "Worst", "White", "Worth", "Visit", "Would", "Vital", "Voice"
# Pick word at random

RED = '\033[31m'
GREEN = '\033[32m'
BLUE = '\033[34m'

YELLOW = '\033[93m'

RESET = '\033[0m'


# word_list = ["About", "Alert", "Argue", "Beach", "Above", "Alike", "Arise", "Began", "Abuse", "Alive", "Array", "Begin", "Actor", "Allow", "Aside", "Begun", "Acute", "Alone", "Asset", "Being", "Admit", "Along", "Audio", "Below", "Adopt", "Alter", "Audit", "Bench", "Adult", "Among", "Avoid", "Billy", "After", "Anger", "Award", "Birth", "Again", "Angle", "Aware", "Black", "Agent", "Angry", "Badly", "Blame", "Agree", "Apart", "Baker", "Blind", "Ahead", "Apple", "Bases", "Block", "Alarm", "Apply", "Basic", "Blood", "Album", "Arena", "Basis", "Board", "Boost", "Buyer", "China", "Cover", "Booth", "Cable", "Chose", "Craft", "Bound", "Calif", "Civil", "Crash", "Brain", "Carry", "Claim", "Cream", "Brand", "Catch", "Class", "Crime", "Bread", "Cause", "Clean", "Cross", "Break", "Chain", "Clear", "Crowd", "Breed", "Chair", "Click", "Crown", "Brief", "Chart", "Clock", "Curve", "Bring", "Chase", "Close", "Cycle", "Broad", "Cheap", "Coach", "Daily", "Broke", "Check", "Coast", "Dance", "Brown", "Chest", "Could", "Dated", "Build", "Chief", "Count", "Dealt", "Built", "Child", "Court", "Death", "Debut", "Entry", "Forth", "Group", "Delay", "Equal", "Forty", "Grown", "Depth", "Error", "Forum", "Guard", "Doing", "Event", "Found", "Guess", "Doubt", "Every", "Frame", "Guest", "Dozen", "Exact", "Frank", "Guide", "Draft", "Exist", "Fraud", "Happy", "Drama", "Extra", "Fresh", "Harry", "Drawn", "Faith", "Front", "Heart", "Dream", "False", "Fruit", "Heavy", "Dress", "Fault", "Fully", "Hence", "Drill", "Fibre", "Funny", "Night", "Drink", "Field", "Giant", "Horse", "Drive", "Fifth", "Given", "Hotel", "Drove", "Fifty", "Glass", "House", "Dying", "Fight", "Globe", "Human", "Eager", "Final", "Going", "Ideal", "Early", "First", "Grace", "Image", "Earth", "Fixed", "Grade", "Index", "Eight", "Flash", "Grand", "Inner", "Elite", "Fleet", "Grant", "Input", "Empty", "Floor", "Grass", "Issue", "Enemy", "Fluid", "Great", "Irony", "Enjoy", "Focus", "Green", "Juice", "Enter", "Force", "Gross", "Joint", "Judge", "Metal", "Media", "Newly", "Known", "Local", "Might", "Noise", "Label", "Logic", "Minor", "North", "Large", "Loose", "Minus", "Noted", "Laser", "Lower", "Mixed", "Novel", "Later", "Lucky", "Model", "Nurse", "Laugh", "Lunch", "Money", "Occur", "Layer", "Lying", "Month", "Ocean", "Learn", "Magic", "Moral", "Offer", "Lease", "Major", "Motor", "Often", "Least", "Maker", "Mount", "Order", "Leave", "March", "Mouse", "Other", "Legal", "Music", "Mouth", "Ought", "Level", "Match", "Movie", "Paint", "Light", "Mayor", "Needs", "Paper", "Limit", "Meant", "Never", "Party", "Peace", "Power", "Radio", "Round", "Panel", "Press", "Raise", "Route", "Phase", "Price", "Range", "Royal", "Phone", "Pride", "Rapid", "Rural", "Photo", "Prime", "Ratio", "Scale", "Piece", "Print", "Reach", "Scene", "Pilot", "Prior", "Ready", "Scope", "Pitch", "Prize", "Refer", "Score", "Place", "Proof", "Right", "Sense", "Plain", "Proud", "Rival", "Serve", "Plane", "Prove", "River", "Seven", "Plant", "Queen", "Quick", "Shall", "Plate", "Sixth", "Stand", "Shape", "Point", "Quiet", "Roman", "Share", "Pound", "Quite", "Rough", "Sharp", "Sheet", "Spare", "Style", "Times", "Shelf", "Speak", "Sugar", "Tired", "Shell", "Speed", "Suite", "Title", "Shift", "Spend", "Super", "Today", "Shirt", "Spent", "Sweet", "Topic", "Shock", "Split", "Table", "Total", "Shoot", "Spoke", "Taken", "Touch", "Short", "Sport", "Taste", "Tough", "Shown", "Staff", "Taxes", "Tower", "Sight", "Stage", "Teach", "Track", "Since", "Stake", "Teeth", "Trade", "Sixty", "Start", "Texas", "Treat", "Sized", "State", "Thank", "Trend", "Skill", "Steam", "Theft", "Trial", "Sleep", "Steel", "Their", "Tried", "Slide", "Stick", "Theme", "Tries", "Small", "Still", "There", "Truck", "Smart", "Stock", "These", "Truly", "Smile", "Stone", "Thick", "Trust", "Smith", "Stood", "Thing", "Truth", "Smoke", "Store", "Think", "Twice", "Solid", "Storm", "Third", "Under", "Solve", "Story", "Those", "Undue", "Sorry", "Strip", "Three", "Union", "Sound", "Stuck", "Threw", "Unity", "South", "Study", "Throw", "Until", "Space", "Stuff", "Tight", "Upper", "Upset", "Whole", "Waste", "Wound", "Urban", "Whose", "Watch", "Write", "Usage", "Woman", "Water", "Wrong", "Usual", "Train", "Wheel", "Wrote", "Valid", "World", "Where", "Yield", "Value", "Worry", "Which", "Young", "Video", "Worse", "While", "Youth", "Virus", "Worst", "White", "Worth", "Visit", "Would", "Vital", "Voice"]
# hidden_word = random.choice(word_list)

hidden_word = []
rng = 0

for j in range(10):
    rng = random.randint(1, 26)

    if rng == 1:
        hidden_word += "a"
    elif rng == 2:
        hidden_word += "b"
    elif rng == 3:
        hidden_word += "c"
    elif rng == 4:
        hidden_word += "d"
    elif rng == 5:
        hidden_word += "e"
    elif rng == 6:
        hidden_word += "f"
    elif rng == 7:
        hidden_word += "g"
    elif rng == 8:
        hidden_word += "h"
    elif rng == 9:
        hidden_word += "i"
    elif rng == 10:
        hidden_word += "j"
    elif rng == 11:
        hidden_word += "k"
    elif rng == 12:
        hidden_word += "l"
    elif rng == 13:
        hidden_word += "m"
    elif rng == 14:
        hidden_word += "n"
    elif rng == 15:
        hidden_word += "o"
    elif rng == 16:
        hidden_word += "p"
    elif rng == 17:
        hidden_word += "q"
    elif rng == 18:
        hidden_word += "r"
    elif rng == 19:
        hidden_word += "s"
    elif rng == 20:
        hidden_word += "t"
    elif rng == 21:
        hidden_word += "u"
    elif rng == 22:
        hidden_word += "v"
    elif rng == 23:
        hidden_word += "w"
    elif rng == 24:
        hidden_word += "x"
    elif rng == 25:
        hidden_word += "y"
    elif rng == 26:
        hidden_word += "z"








print("WORDLE:")

i = 0

# Repeat for 6 guesses
while i < 21:
    # Guess a word
    rg = 20 - i
    print(f"you have {rg} guesses left")
    guess_word = input()

    output1 = ""
    output2 = ""

    # if guess_word in word_list:
    # i += 1
    # else:
    #     print("not a word")
    #     continue

    # First letter (in python, counting starts at 0 not 1)

    if not len(guess_word) == 10:
        print("not 10 letters")
        continue
    else:
        i += 1

    for u in range(10):
        if guess_word[u] == hidden_word[u]:
            output1 += f"{GREEN} {guess_word[u]}{RESET}"
            output2 += "🟩"
        elif guess_word[u] in hidden_word:
            output1 += f"{YELLOW} {guess_word[u]}{RESET}"
            output2 += "🟨"
        else:
            output1 += f"{RESET} {guess_word[u]}{RESET}"
            output2 += "⬛"
    

    # Result
    print(output1)
    print(output2)
    # if guess_word == hidden_word:
    if output2 == "🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩":
        print("You win")
        break

print(f"You used {i} guesses")