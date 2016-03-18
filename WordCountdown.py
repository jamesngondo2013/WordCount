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

#initializing vowels and consonants
vow = list("aeiou")
cons = list("bcdfghjklmnpqrstvwxyz")

# method that generates vowels and consonants
def vowels_consonants(vow, cons):
    vowels = [letter for letter in vow if letter in vow]
    consonants = [c for c in cons if c in cons]
    randConsonant = random.sample(consonants, 4)
    randVowel = random.sample(vowels, 5)
	
    newstring = randConsonant + randVowel
    vowelsconsonantsword = "".join(newstring)
    return vowelsconsonantsword

    
#assign generated vowels and consonants to variable inputWord 
inputWord = vowels_consonants(vowel, consonant)

print("Randomly Generated letters are: ", inputWord)