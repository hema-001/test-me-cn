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

Newly added on 1/29/2023 by Ibrahim M. I. Ismail:
- added english translation of the words

Newly added on 2/1/2023 by Ibrahim M. I. Ismail:
- added a feature to show the wrong answers at the end of the execution

Newly added on 2/2/2023 by Ibrahim M. I. Ismail:
- added a feature to show the time it took to complete the quiz

Newly added on 2/12/2023 by Ibrahim M. I. Ismail:
- optimized the script, now using dictionries instead of lists

Newly added on 2/26/2023 by Ibrahim M. I. Ismail:
- added a feature to allow users to limit the number of characters to be tested with
"""
import csv
import random
import time
import sys

def load_csv_file(filename):
    """Loads the CSV file and returns a list of characters, pinyin, and English meanings."""
    with open(filename, newline='', encoding='utf-8') as f:
        reader = csv.reader(f)
        return [(row[0], row[1], row[2]) for row in reader]

def quiz(characters, num_chars):
    """Runs a quiz using the specified list of characters."""
    score = 0
    wrong_answers = []
    total_chars = num_chars
    current_char = 0
    # initialize the timer

    for char, pinyin, eng in characters[:num_chars]:
        start_time = time.time()
        input_str = input(f"\nHit enter to get a character, or type 'quit' to stop.\n")
        if input_str == 'quit':
            break
        
        current_char += 1
        
        print(f"What is the pinyin for the following character?")
        print(f"{char}")
        print(f"\n{current_char}/{total_chars}")
        input(f"Hit enter to get the answer.")
        print(f"\nThe right answer is: {pinyin}, in English: {eng}")
        answer = input(f"\nDid you get it right?, 'Yes' or 'No':")

        if answer.lower() not in {"yes", "no"}:
            print("Invalid input. Please enter 'Yes' or 'No'.")
            continue

        if answer.lower() == 'yes':
            score += 1
        else:
            wrong_answers.append(f"{char},{pinyin},{eng}")
    
    end_time = time.time()
    total_time = end_time - start_time

    final_score = score / num_chars
    # print the final time in minutes and seconds
    print(f"\nYou took {int(total_time / 60)} minutes and {float(total_time % 60)} seconds to complete the quiz.")
    print(f"\nYour final score is {int(final_score * 100)}%")
    print(f"You got {score} characters correct out of {num_chars}")

    if wrong_answers:
        print("\nYou got the following wrong:")
        for wrong_answer in wrong_answers:
            print(wrong_answer)

if __name__ == '__main__':
    # get run arguments
    args = sys.argv[1:]
    if len(args) != 1:
        print("Usage: python char_quiz.py <number of chars>")
        exit()
    print(f"Loading {args[0]} characters...")
    try:
        characters = load_csv_file("characters.txt")
    except FileNotFoundError:
        print("Error: File not found")
        exit()
    except csv.Error:
        print("Error: Invalid CSV file")
        exit()

    random.shuffle(characters)
    quiz(characters, int(args[0]))
