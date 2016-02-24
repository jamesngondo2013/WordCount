import random

vow = list("aeiou")
cons = list("bcdfghjklmnpqrstvwxyz")

vowels = [letter for letter in vow if letter in vow]

consonants = [c for c in cons if c in cons]
print(consonants)
print(vowels)

randConsonant = random.sample(consonants, 4)
randVowel = random.sample(vowels, 5)
	
newstring = randConsonant + randVowel
vowelsconsonantsword = "".join(newstring)
print(vowelsconsonantsword)

def anagramGenerator(dictword,checkedword):  
    for letter in dictword:  
        if letter in checkedword:  
            checkedword=checkedword.replace(letter, '', 1)  
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