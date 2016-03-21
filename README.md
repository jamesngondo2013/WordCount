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
Installation procedure for Beautiful Soup can be found [here](http://www.crummy.com/software/BeautifulSoup/bs4/doc/).

####* [urllib.request](https://docs.python.org/3/library/urllib.request.html#module-urllib.request)
The urllib.request module defines functions and classes which help in opening URLs (mostly HTTP) in a complex world — basic and digest authentication, redirections, cookies and more.
####* [Itertools](https://docs.python.org/3/library/itertools.html)
Itertools comes packaged with Python and it provides a set of functions for working with iterable data sets. In the end, these are functions that will increase performance and avoid side effects with larger data sets.
####* [Defaultdict](https://www.accelebrate.com/blog/using-defaultdict-python/)
A defaultdict is a Python dictionary which provides a default value for keys, so that keys which have no value(s) can be explicitly defined and accessed without errors. That simply means you do not need to check whether a key is present or not.

###* [Time]

###* [Random]


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

Finally, the below script gets all the generates anagrams based on the input vowels and consonants and initially check to see if the matched_word list is not empty, then get all the longest words and prints them out. If the matched_word is empty, we get then assume that we were not able to generate any english anagram from the inputWord (Vowels and Consonants).
```python
matched_word = generate_longest_word()

#check to see if the matched_word list is not empty, get all the longest words and print them out
found = False

if(matched_word):
    for word in matched_word:
        if(word in matched_word):
            print("Longest Generated Word is: ",word)
            found = True
            
else:
    print("Sorry, Can not create word...Try Again")  
```

#### b) Efficiency
The algorithm has been timed. It is more efficient in terms of time/ speed. Since this algorithm uses web scraping, therefore, 	the speed varies depending on internet connection as it sifts through the web page to get data (English dictioanry words). If the 		internet connection is slow, then the algorithm itself is a bit slow. The first time the algorithm runs, it will create a 	dictionary file (dictionary.txt) and populate it with english words. Then it will start reading in the dictionary file (preprocessing) and add to Python's standard dictionary. Generating anagrams from vowels and consonants and checking against Python's standard dictionary with key value pairs is faster since defaultdict has excellent runtime performance characteristics. The whole process may take approximately 0.756014347076416 seconds.


#### c) Results
The screenshot below indicates the output results after running the algorithm several times. 
![alt tag](http://url/to/img.png)

### 2. Script using an existing English Word Dictionary
#### a) Preprocessing
#### b) Efficiency
#### c) Results

### 3. Scrip with Graphical User Interface (GUI)
#### a) Preprocessing
#### b) Efficiency
#### c) Results

## References

