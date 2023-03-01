# TestMeCn
This app returns a random Chinese word from a file of characters that I learned, to test my learning progress.

## Requirements
- Python 3.x
- csv module
## Installation
1. Clone this repository or download char_quiz.py and characters.txt files.
2. Install Python 3.x if it's not already installed.
3. Open a command prompt and navigate to the directory where the files are located.
4. Run pip install csv to install the csv module.
## Usage
Open the characters.txt file and fill it with the Chinese characters you wish to test yourself with.
Each line should have only one Chinese character and its corresponding pinyin and English translation separated by comma in the following format:

```
大,da,big
车,che,car
打电话,dadianhua,make a phone call  
```

To run the quiz, open a command prompt and navigate to the directory where the files are located.
Run the following command: 
```
python char_quiz.py <HSK level: e.g. 1|2|3|.., or '0' for all chars in file> <number of characters> 
```
Where `<HSK level>` specifies the words to be tested with to be within a given HSK-level. For example, HSK-1 has 150 words, HSK-2 has 300 words and so on. 
And `<number of characters>` is the number of characters you wish to be tested with. For example, 
```
python char_quiz.py 1 10 
```
will test you on 10 random characters from HSK level 1 (HSK-1) fetched from the csv file.  
Follow the prompts to complete the quiz.  
At the end of the quiz, the app will show you how many characters you got right out of the total characters in the file, the time it took to complete the quiz, and the characters that you got wrong.

## Change log
### 3/1/2023
- Added a feature to allow users to specify the HSK level of the characters to be tested with
### 2/26/2023
- Added a feature to allow users to limit the number of characters to be tested with.
### 2/12/2023
- Optimized the script, now using dictionaries instead of lists.
### 2/2/2023
- Added a feature to show the time it took to complete the quiz.
### 2/1/2023
- Added a feature to show the wrong answers at the end of the execution.
### 1/29/2023
- Added English translation of the words.
### 1/15/2023
- Added correct answer feature; you should see the correct pinyin of the character after your answer.
- Added one more message at the end of the execution to show how many characters you got right out of the total characters in the file.
