import itertools
from collections import defaultdict
import random
import time

print("====================================")
print("Proccessing...")

#initializing vowels and consonants
vowel = list("aeiou")
consonant = list("bcdfghjklmnpqrstvwxyz")

start = time.time()

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
file = open('dictionary2.txt','r')
f = file.readlines()
for word in f:
	word=word.strip()
	words[''.join(sorted(word))].append(word)

# searching for the longest anagram, get the vowels and consonants and check against the words in dictionary
def generate_longest_word():
    outputlist = []
    inputWord = vowels_consonants(vowel, consonant)     #assign generated vowels and consonants to variable inputWord 
    print("Randomly Generated letters are: ", inputWord)
    length_of_word = len(inputWord)
    #sort the vowels and consonants
    inputWord = sorted(inputWord) 
    while length_of_word > 0:
        # generate possible combinations of anagrams based on the length_of_word
        #itertools combinations will maintain the sort order of the letters
        for wordcombination in itertools.combinations(inputWord, length_of_word):  
            result = ''.join(wordcombination)
            if result in words:
            #returns list that contains all possible generated anagrams that match any of the engilsh words in the dictionary 
                outputlist= words[result]
                return outputlist

        length_of_word = length_of_word - 1
        
found = False
#this function will sort the list of anagrams in ascending order and prints out the longest word from the sorted list
def print_longestWords():
    list = generate_longest_word()
    #check to see if the matched_word list is not empty
    if(list is not None):
        sortedwords = sorted(list, key=len) #this builds a new sorted list of anagrams from an iterable.
        print("Total Number of Anagrams: ",len(list))
        print("Longest Word: ",sortedwords[-1])
        found = True
        
    else:
        print("No Longest Word Found...Please try again")
    
print_longestWords()

end = time.time()

print("Processing Finished...")
print("Time taken... %s seconds " % (end - start))     