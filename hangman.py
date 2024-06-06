#hangman game in python 
#Made by Dhruv :))
import random
wordbank = []
tries = "X X X X X X X X X X"
with open('hangwords.txt','r') as wordfile:
    for line in wordfile:      
        for worde in line.split():
            wordbank.append(worde +" ")
word = (random.choice(wordbank))
#word = "level"
charcount = len(word)-1
tri = ("Tries: ")
lose = ("You lost!")
win = ("You win!")
ndashes = (str("_"*charcount))
dashes = (str("_"*charcount))
print(f"Word length: {charcount}")
for i in range(0,50):
    dashes=ndashes
    print(f'\033[28;1m{dashes}\033[0m') #necessary
    usergs = input()
    #print(word.count(usergs)) make this into a double letter detection
    # occurcount = word.count(usergs)
    # if occurcount>1:
    #     print("WARNING: MULTIPLE LETTERS")
    #     letpos = (word.find(usergs))
    #     qwer = dashes[letpos]
    #     ndashes = list(dashes)
    #     ndashes[letpos] = usergs

    if usergs == "exit":
        exit()
    if len(usergs) != 1 and usergs != "instant":
        print("One character at a time!")
        exit()
    letpos = (word.find(usergs))
    if usergs in word:
        qwer = dashes[letpos]
        ndashes = list(dashes)
        ndashes[letpos] = usergs
    elif usergs not in word:
        tries = tries[:-2]
    occurcount = word.count(usergs)
    # while occurcount>1:
    #     print("WARNING: MULTIPLE LETTERS")
    #     letpos2 = (word.find(usergs,letpos+1))
    #     qwer = dashes[letpos2]
    #     ndashes = list(dashes)
    #     ndashes[letpos] = usergs
    #     occurcount -= 1
    print(f'\033[31;1m{tri}{tries}\033[0m') #necessary

    if "_" not in ndashes or usergs == "instant":
        print(f'\033[36;1m{win}\033[0m')
        print(f"Correct word: {word}")
        exit()
    if len(tries) == 0:
        print(f'\033[33;1m{lose}\033[0m')
        print(f"Correct word: {word}")
        exit()