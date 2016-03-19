### Student Name - James Ngondo
#### Student Number - G00304277

# Python Countdown Letter Game Solver

## Introduction
This script is meant to solve a Countdown letter game. Countdown is a long-running British TV game show that involves word and number puzzles. More details on [Wikipedia](https://en.wikipedia.org/wiki/Countdown_(game_show)#Letters_round). This game requires that the user attemps to make the longest word possible from nine randomly generated letters, comprising five vowels and four consonants.

## About the Scripts
This document outlines three different scripts that I have used for the Countdown Letter Game Solver. Each script will be analyzed in detail later in the following section as I will be explaining what each version of the script does. 

## Tools and Libraries
Developed using Python 3.0.1 Release.
An [English dictionary](http://www-01.sil.org/linguistics/wordlists/english/wordlist/wordsEn.txt) file known as dictionary.txt with one word per line and approximately 120,000 words is used in this script. The script will check if the dictionary text file exist. If not, it will attempt to create one. The script also uses some of Python's standard libraries such as:
####* [Beautiful Soup](http://www.crummy.com/software/BeautifulSoup/bs4/doc/)
Beautiful Soup is a Python library for pulling data out of HTML and XML files. It works with your favorite parser to provide idiomatic ways of navigating, searching, and modifying the parse tree. It commonly saves programmers hours or days of work. Beautiful Soup supports the HTML parser included in Python’s standard library, but it also supports a number of third-party Python parsers.
Installation procedure for Beautiful Soup can be found [here](http://www.crummy.com/software/BeautifulSoup/bs4/doc/).

####* [urllib.request](https://docs.python.org/3/library/urllib.request.html#module-urllib.request)
The urllib.request module defines functions and classes which help in opening URLs (mostly HTTP) in a complex world — basic and digest authentication, redirections, cookies and more.
####* Itertools
####* Defaultdict

## Versions of the Script
The Countdown Letter Game Solver script is been divided into three - with each script demonstrating the way it runs (processing, efficiency and the output results). Each script has been timed in order to check its efficiency depending on certain input factors. 

### Version 1 - Script With Web Scraping
This version uses a web scraping algorithm. 
Web scraping is the practice of using a computer algorithm that sifts through a web page and gather the data that is needed in a format most useful to the user while at the same time preserving the structure of the data.

#### a) Preprocessing
The algorithm starts with preprocessing where it it has to initially create an english word dictionary text file. This is where web scraping comes in. The algorithm has to sift through a web page and gather data.
```python
import itertools
from collections import defaultdict
import random
from bs4 import BeautifulSoup
import urllib.request
import time
```
#### b) Efficiency
#### c) Results

### 2. Script using an existing English Word Dictionary
#### a) Preprocessing
#### b) Efficiency
#### c) Results

### 3. Scrip with Graphical User Interface (GUI)
#### a) Preprocessing
#### b) Efficiency
#### c) Results

## References

