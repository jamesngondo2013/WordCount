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
file = open('dictionary.txt','r')
f = file.readlines()
for word in f:
	word=word.strip()
	words[''.join(sorted(word))].append(word)

# searching for the longest anagram, get the vowels and consonants and check against the words in dictionary
def generate_longest_word():
    inputWord = vowels_consonants(vowel, consonant)
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
                return words[result]
        length_of_word = length_of_word - 1
    

#assign generated vowels and consonants to variable inputWord 
	
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

end = time.time()

print("Processing Finished...")
print("Time taken... %s seconds " % (end - start))     