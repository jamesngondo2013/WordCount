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
vowel = list("aeiou")
consonant = list("bcdfghjklmnpqrstvwxyz")

# method that generates vowels and consonants
def vowels_consonants(vow, cons):
    vowels = [letter for letter in vow if letter in vow]
    consonants = [c for c in cons if c in cons]
    randConsonant = random.sample(consonants, 4)
    randVowel = random.sample(vowels, 5)
	
    newstring = randConsonant + randVowel
    vowelsconsonantsword = "".join(newstring)
    return vowelsconsonantsword
    
# read from file and and populate the dictionary
words = defaultdict(list)
file = open('dictionary.txt','r')
f = file.readlines()
for word in f:
	word=word.strip()
	words[''.join(sorted(word))].append(word)

# searching for the longest anagram, get the vowels and consonants and check against the words in dictionary
def generate_longest_word(vows_cons, words):
    length_of_word = len(vows_cons)
    #sort the vowels and consonants
    vows_cons = sorted(vows_cons) 
    while length_of_word > 0:
        # generate possible combinations of anagrams based on the length_of_word
        #itertools combinations will maintain the sort order of the letters
        for wordcombination in itertools.combinations(vows_cons, length_of_word):  
            result = ''.join(wordcombination)
            if result in words:
                return words[result]
        length_of_word -= 1
    

