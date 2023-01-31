"""
This app returns a random Chines words from a file of 
characters that I learned, to test my learning progress.

How to Use:

Just fill the "characters.txt" file with the Chinese characters you wish
to test yourself with, the file format is comma separated values (i.e., CSV)
each line should have only one Chinese character and its corresponding pinyin and english
translation spearated by comma.

characters.txt format example:
大,da,big
车,che,car
打电话,dadianhua,make a phone call

and so on.



Newly added on 1/15/2023 by Ibrahim M. I. Ismail:
- added correct answer feature; you should see the correct
  pinyin of the character after your answer
- added one more message at the end of the execution to 
  to show how many characters you got right out of the 
  total characters in file.

Newly added on 1/29/2023 by Ibrahim M. I. Ismail:
- added english translation of the words
"""
import random

def loadFile(f):
    ls = []
    with open(f, "r", encoding="utf8") as file:
        for line in file:
            ls.append(line.strip())
    return ls

def getCharFromList(ls):
    word = ls[0]
    ls.remove(ls[0])
    return word

def separateLines(ls):
    char = []
    pinyin = []
    eng = []
    for line in ls:
        char.append(line.split(",")[0].strip())
        pinyin.append(line.split(",")[1].strip())
        eng.append(line.split(",")[2].strip())
    return (char, pinyin, eng)

if __name__ == '__main__':
    ls = loadFile("characters.txt")
    random.shuffle(ls)
    char, pin_yin, eng = separateLines(ls)
    user_input = ""
    score = 0
    char_count = len(char)
    while user_input != "quit" and len(char) != 0:
        user_input = input("\nHit enter to get a character, or enter \'quit\' to stop.\n")
        print(getCharFromList(char))
        answer = input("\nDid you get it right?, \'Yes\' or \'No\':")
        print("\nThe right answer is: {}, in English: {}".format(getCharFromList(pin_yin), getCharFromList(eng)))
        if answer.lower() == "yes":
            score += 1
    final_score = score/char_count
    print("Your final score is {}%".format(int(final_score*100)))
    print("You got {} characters correct out of {}".format(score, char_count))
