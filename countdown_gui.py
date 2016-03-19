try:
    # for Python2
    from Tkinter import *   ## notice capitalized T in Tkinter 
    import itertools
    from collections import defaultdict
    import random
except ImportError:
    # for Python3
    from tkinter import *   ## notice here too
    from collections import defaultdict
    import itertools
    


#https://www.youtube.com/watch?v=ic3__PoSq-4

class Application(Frame):
    def __init__(self, master): #constructor

        Frame.__init__(self, master)# initialize frame
        self.grid()
        self.create_widgets()
        
    def create_widgets(self): #create button, text, widgets
    
        #self.labelframe = LabelFrame(root, text="This is a LabelFrame")
        #self.labelframe.pack(fill="both", expand="yes")
        
        self.instruction = Label(self, text = "Enter Vowels(5) and Consonants(4)")
        self.instruction.grid(row = 4, column =0, columnspan =2, sticky =W)
        
        self.vowelsconsonants = Entry(self)
        self.vowelsconsonants.grid(row =4, column = 1, sticky = W)
        
        
        
        #textbox that displays the message
        self.text = Text(self, width =70, height = 20, wrap = WORD)
        self.text.grid(row =6, column =0, columnspan = 2, sticky = W)
        
        self.submit_button = Button(self, text ="Submit", command = self.reveal)
        self.submit_button.grid(row = 8, column = 1, sticky = W)
        
        self.quit_button = Button(self, text ="Quit", command = self.quit)
        self.quit_button.grid(row = 8, column = 1, sticky = E)
    
        
    def reveal(self):
        words = defaultdict(list)
        bye = []
        inputWord = self.vowelsconsonants.get()
        #self.text.insert(0.0, inputWord)
        # read from file and and populate the dictionary
        #words = defaultdict(list)
        file = open('dictionary.txt','r')
        f = file.readlines()
        for word in f:
            word=word.strip()
            words[''.join(sorted(word))].append(word)
            
        length_of_word = len(inputWord)
        #sort the vowels and consonants
        inputWord = sorted(inputWord) 
        while length_of_word > 0:
                    # generate possible combinations of anagrams based on the length_of_word
                    #itertools combinations will maintain the sort order of the letters
            for wordcombination in itertools.combinations(inputWord, length_of_word):  
                result = ''.join(wordcombination)
                if result in words:
                    bye =  words[result]
            length_of_word -= 1
            
        for word in bye:
            if(word in bye):
                self.text.insert(0.0, word,'\n')
                print("Longest Generated Word is: ",word)

        
		
	
root = Tk()
root.title("Ngondo James Word Countdown")
root.geometry("600x450")


app = Application(root)
root.mainloop()    
    
    
    
    
    
	