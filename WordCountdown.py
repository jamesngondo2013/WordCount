import itertools
from collections import defaultdict
import random
from bs4 import BeautifulSoup
import urllib.request

NUM_LETTERS = 5
file = open('dictionary.txt', 'w+') # file that will store all the English words we get form website

print("====================================")
print("File name created: ",file.name)
print("Proccessing...")

#Gettting English words from the website using web scraping tools
#We read all the english words and only write to file words with a length of greater than five 
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

vow = list("aeiou")
cons = list("bcdfghjklmnpqrstvwxyz")


vowels = [letter for letter in vow if letter in vow]

consonants = [c for c in cons if c in cons]


randConsonant = random.sample(consonants, 4)
randVowel = random.sample(vowels, 5)
	
newstring = randConsonant + randVowel
vowelsconsonantsword = "".join(newstring)
print(vowelsconsonantsword)

def anagramGenerator(dictword,inputword):  
    for letter in dictword:  
        if letter in inputword:  
            inputword=inputword.replace(letter, '', 1)  
        else:  
            return False  
    return True

#inputWord = vowelsconsonantsword
inputWord=input('Enter anagram:')  
f = open('wordsList.txt', 'r')  
for line in f:  
    line=line.strip()
    if anagramGenerator(line,inputWord): 
        print(line)
f.close()