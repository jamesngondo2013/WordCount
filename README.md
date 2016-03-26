### Student Name - James Ngondo
#### Student Number - G00304277

# Python Countdown Letter Game Solver

## Introduction
This script is meant to solve a Countdown letter game. Countdown is a long-running British TV game show that involves word and number puzzles. More details on [Wikipedia](https://en.wikipedia.org/wiki/Countdown_(game_show)#Letters_round). This game requires that the user attemps to make the longest word possible from nine randomly generated letters, comprising five vowels and four consonants.

## About the Scripts
This document outlines three different scripts that I have used for the Countdown Letter Game Solver. Each script will be analyzed in detail later in the following section as I will be explaining what each version of the script does. 

## Tools and Libraries
The scripts are developed using Python 3.0.1 Release.
An [English dictionary](http://www-01.sil.org/linguistics/wordlists/english/wordlist/wordsEn.txt) file known as dictionary.txt with one word per line and approximately 120,000 words is used in this script. The script will check if the dictionary text file exist. If not, it will attempt to create one. The script also uses some of Python's standard libraries such as:
####* [Beautiful Soup](http://www.crummy.com/software/BeautifulSoup/bs4/doc/)
Beautiful Soup is a Python library for pulling data out of HTML and XML files. It works with your favorite parser to provide idiomatic ways of navigating, searching, and modifying the parse tree. It commonly saves programmers hours or days of work. Beautiful Soup supports the HTML parser included in Python’s standard library, but it also supports a number of third-party Python parsers.
BeautifulSoup4 installs fine with python3. But make sure that your version of pip is for python3.
        cli -> pip install beautifulsoup4
        cli ->pip -V
        
Full installation procedure for Beautiful Soup can be found [here](http://www.crummy.com/software/BeautifulSoup/bs4/doc/).


####* [urllib.request](https://docs.python.org/3/library/urllib.request.html#module-urllib.request)
The urllib.request module defines functions and classes which help in opening URLs (mostly HTTP) in a complex world — basic and digest authentication, redirections, cookies and more.
####* [Itertools](https://docs.python.org/3/library/itertools.html)
Itertools comes packaged with Python and it provides a set of functions for working with iterable data sets. In the end, these are functions that will increase performance and avoid side effects with larger data sets.
####* [Defaultdict](https://www.accelebrate.com/blog/using-defaultdict-python/)
A defaultdict is a Python dictionary which provides a default value for keys, so that keys which have no value(s) can be explicitly defined and accessed without errors. That simply means you do not need to check whether a key is present or not.

####* [tkinter](https://docs.python.org/3.0/library/tkinter.html)
Tkinter is the standard GUI library for Python. Python when combined with Tkinter provides a fast
and easy way to create GUI applications. Tkinter provides a powerful object-oriented interface to
the Tk GUI toolkit.

####* [Time](http://pythoncentral.io/measure-time-in-python-time-time-vs-time-clock/)
Python's time module provides various time-related functions. time.time() returns the time in seconds since the epoch, i.e., the point where the time starts. If the program is expected to run in a system that also runs lots of other programs at the same time, using time.time() makes sense.

####* [Random](http://effbot.org/librarybook/random.htm)
 The random module is another library of functions that can extend the basic features of python. This can be used to pick a random element from a list, pick a random card from a deck etc.


## Versions of the Script
The Countdown Letter Game Solver script is been divided into three - with each script demonstrating the way it runs (processing, efficiency and the output results). Each script has been timed in order to check its efficiency depending on certain input factors. 

### Version 1 - Script With Web Scraping
This version uses a web scraping algorithm. 
Web scraping is the practice of using a computer algorithm that sifts through a web page and gather the data that is needed in a format most useful to the user while at the same time preserving the structure of the data.

#### a) Preprocessing
The algorithm starts with preprocessing where it it has to initially create an english word dictionary text file. This is where web scraping comes in. The algorithm has to sift through a web page and gather the data we need.
The code snippet below shows some of Python's libraries that I have used.
```python
import itertools
from collections import defaultdict
import random
from bs4 import BeautifulSoup
import urllib.request
import time
```
This code snippet below creates a file called dictionary.txt if it does not exist or override the existing one when the script is run.
The def getEnglish_Words(...) function will perfom web scraping, getting all the english words from a given [website](http://www-01.sil.org/linguistics/wordlists/english/wordlist/wordsEn.txt). In order to reduce the search space for my algorithm, and come up with the longest english word possible, I have decided to eliminate from the english word dictionary all the words that have the length of less than five... which simply means that only words that have the length greater than five are extracted and then written to a text file - dictionary.txt. 
```python
NUM_LETTERS = 5
file = open('dictionary.txt', 'w+')
print("File name created: ",file.name)
print("Proccessing...")

def getEnglish_Words(link):
    page = urllib.request.urlopen(link)
    soup = BeautifulSoup(page.read(),"html.parser")
    data = soup.string
    for word in data.split():
        if len(word) > NUM_LETTERS:
            
            file.write(word)
            file.write('\n')
            #print((word))
                       
    file.close()           
url = "http://www-01.sil.org/linguistics/wordlists/english/wordlist/wordsEn.txt"
words = getEnglish_Words(url)
```
The section of the code below, is a function that randomly generates and return all the nine letters that I need to generate a longest possible english word of nine characters. This includes five vowels and four consonants.

```python
vowel = list("aeiou")
consonant = list("bcdfghjklmnpqrstvwxyz")

start = time.time()

def vowels_consonants(vow, cons):
    vowels = [letter for letter in vow if letter in vow]
    consonants = [c for c in cons if c in cons]
    randConsonant = random.sample(consonants, 4)
    randVowel = random.sample(vowels, 5)
	
    newstring = randConsonant + randVowel
    vowelsconsonantsword = "".join(newstring)
    return vowelsconsonantsword
```

The script below reads english words from text file, remove all the white spaces, sort and join all the individual charachers and add them to a Python default dictionary - words. As explained above, you can that the dictionary is has no keys. Defaultdict automatically creates an empty list, and the list.append will then help to append the values to the list. Using defaultdict proves to be faster than performing similar poerations using dict.set_default method of Python.
```python
words = defaultdict(list)
file = open('dictionary.txt','r')
f = file.readlines()
for word in f:
	word=word.strip()
	words[''.join(sorted(word))].append(word)
```	

The part of script below is a function that searches for the longest anagram. It gets the randomly generated vowels and consonants and sorts them. The function uses the itertools.combination library (as explained above) to produce a sequence of combinations of items taken from the inputWord - this returns an iterator containing all the possible combinations of the given sequence of the given length. The itertools.combinatios does not include items that are duplicates of other items in a different order. The function eventually returns list that contains all possible generated anagrams.
```python
def generate_longest_word():
	inputWord = vowels_consonants(vowel, consonant)
            .
            .
            .
       
        for wordcombination in itertools.combinations(inputWord, length_of_word):  
            result = ''.join(wordcombination)
            if result in words:
                return words[result]
        length_of_word = length_of_word - 1
            .
            .
            .
```

Finally, the below script gets the list of generated anagrams that was returned from the above function - generate_longest_word(). This function will initially check to see if the list is not empty, then sort the list in ascending order - builds a new sorted list of anagrams from an iterable. and prints them out. If the list is empty, we then assume that we were not able to generate any english anagram from the inputWord (Vowels and Consonants).
```python
 list = generate_longest_word()
    if(list is not None):
        sortedwords = sorted(list, key=len) 
        print("Total Number of Anagrams: ",len(list))
        print("Longest Word: ",sortedwords[-1])
        found = True
        
    else:
        print("No Longest Word Found...Please try again")
    
print_longestWords()
```

This script is being used to time the algorithms. It helps us evaluate the efficiency of the algorthm that is being run.
```python
start = time.time()
	.
	.
	.
end = time.time()
print("Time taken... %s seconds " % (end - start)) 

```

#### b) Efficiency
The algorithm has been timed. It is more efficient in terms of time/ speed. Since this algorithm uses web scraping, therefore, 	the speed varies depending on internet connection as it sifts through the web page to get data (English dictioanry words). If the 		internet connection is slow, then the algorithm itself is a bit slow. The first time the algorithm runs, it will create a 	dictionary file (dictionary.txt) and populate it with english words. Then it will start reading in the dictionary file (preprocessing) and add to Python's standard dictionary. Generating anagrams from vowels and consonants and checking against Python's standard dictionary with key value pairs is faster since defaultdict has excellent runtime performance characteristics. The whole process may take approximately 3.5 seconds.

#### c) Results
The screenshot below indicates the output results after running the algorithm several times. 
![alt text](https://github.com/jamesngondo2013/WordCount/blob/master/results.PNG)

### 2. Script using an existing English Word Dictionary
This algorthm is quite similar to the one above except that it uses an existing dictionary other than web scraping. 
#### a) Preprocessing
During preprocessing, the algorithm also generates random letters that are used to generate the matching anagrams. It reads the dictionary file - (txt) and add all the words to Python's standard dictionary. The proceces of generating anagrams from vowels and consonants and checking against Python's standard dictionary with key value pairs is faster since defaultdict has excellent runtime performance characteristics. The algorithm will generate one or more english words of similar lenght and prints only the longest word as output result. 
#### b) Efficiency
Generating anagrams from vowels and consonants and checking against Python's standard dictionary with key value pairs is faster since defaultdict has excellent runtime performance characteristics. The whole process may take approximately 0.6 seconds.
#### c) Results
Below is a screenshot showing the output results and also the efficiency of the algorithm as it runs several times.
![alt text](https://github.com/jamesngondo2013/WordCount/blob/master/results_V2.PNG)

### 3. Scrip with Graphical User Interface (GUI)
This algorthm is quite similar to the one above except that it uses an existing dictionary other than web scraping and also has a Graphical User Interface that allows the user to input their own letters other than randomly generated letters. The GUI provides two text boxes. One text box is for the user to input the letters of their choice (vowels and consonants). the other text box displays the output results after the user has clicked on the Submit button. Ther user can click on the Reset button to clear the text boxes and re-enter new input. There's also a Quit button that exits the program. This design lets the user interact with the application.
#### a) Preprocessing
During preprocessing, the algorithm also generates random letters that are used to generate the matching anagrams. It reads the dictionary file - (txt) and add all the words to Python's standard dictionary. The proceces of generating anagrams from vowels and consonants and checking against Python's standard dictionary with key value pairs is faster since defaultdict has excellent runtime performance characteristics. The algorithm will generate one or more english words of similar lenght as output result.

Below is a script that shows the Python's standard libraries that we have imported for the algorithm. 
```python
try:
    # for Python2
    from Tkinter import *   ## notice capitalized T in Tkinter 
    import itertools
    from collections import defaultdict
    import random
except ImportError:
    # for Python3
    from tkinter import *  
    from collections import defaultdict
    import itertools
```

This piece of code defines the main class of the application that comprises a constructor that initialises the frame and other widgets such as labels, textboxes and buttons.

```python
class Application(Frame):
    def __init__(self, master): #constructor

        Frame.__init__(self, master)# initialize frame
        self.grid()
        self.create_widgets() 
        
    def create_widgets(self): #create button, text, widgets
    
        self.label= Label(self, text = "")
        self.label.grid(row=0, column=1, columnspan=2, sticky=W)
        
        self.label2= Label(self, text = "Countdown Letter Game Solver",font=("Helvetica", 15),fg="blue")
        self.label2.grid(row=1, column=1, columnspan=2, sticky=W)
        	.	
        	.
        	.
```

This function is called on the Reset button. It clears/ resets the input and display text boxes.
```python
 def reset(self):
        self.vowelsconsonants.delete(0, END)
        self.text.delete(1.0, END)

```

This function is called on the Submit button. It is responsible for reading the text file, store all english words in a defaultdict, get user input ( letters - vowels and consonants), generate possible anagrams and check against the dictionary and the generate the longest word.
```python
def reveal(self):
        words = defaultdict(list)
        outputlst = []
        inputWord = self.vowelsconsonants.get()
   		.
   		.
   		.
```
#### b) Efficiency
In terms of efficiency, the process of generating anagrams from vowels and consonants and checking against Python's standard dictionary with key value pairs is faster since defaultdict has excellent runtime performance characteristics. The whole process may take approximately 0.6 seconds.
#### c) Results
Below are screenshots showing the output results and also the efficiency of the algorithm as it runs several times.
![alt text](https://github.com/jamesngondo2013/WordCount/blob/master/screenshot1.PNG)
![alt text](https://github.com/jamesngondo2013/WordCount/blob/master/screenshot2.PNG)

## References
##### 1. http://code.runnable.com/UqBhah-3yRUKAAAf/anagram-solver-in-python-
##### 2. http://blog.blakehemingway.co.uk/?p=1
##### 3. http://stackoverflow.com/questions/24592036/is-beautiful-soup-available-for-python-3-4-1
##### 4. http://codereview.stackexchange.com/questions/75023/optimizing-an-anagram-solver
##### 5. http://stackoverflow.com/questions/8371887/making-all-possible-combinations-of-a-list-in-python
##### 6. http://stackoverflow.com/questions/16159239/how-can-i-find-the-longest-word-in-a-text-file
##### 7. http://stackoverflow.com/questions/8286554/find-anagrams-for-a-list-of-words
##### 8. https://www.youtube.com/watch?v=XqTKV0Vd0JQ
##### 9. http://www.diveintopython3.net/advanced-iterators.html
##### 10. http://www.howopensource.com/2011/06/generation-of-words-using-the-combination-of-consonants-and-vowels-using-python/
##### 11. http://jakerpomperada.blogspot.ie/2014/06/consonants-and-vowels-counter-in-python.html

