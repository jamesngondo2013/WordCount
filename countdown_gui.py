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
    
        self.label= Label(self, text = "")
        self.label.grid(row=0, column=1, columnspan=2, sticky=W)
        
        self.label2= Label(self, text = "Countdown Letter Game Solver",font=("Helvetica", 15),fg="blue")
        self.label2.grid(row=1, column=1, columnspan=2, sticky=W)
        
        self.label4= Label(self, text = "")
        self.label4.grid(row=2, column=1, columnspan=2, sticky=W)

           
        self.instruction = Label(self, text = "Enter Vowels(5) and Consonants(4)")
        self.instruction.grid(row = 3, column =0, columnspan=2,sticky =W)
        
        self.label3= Label(self, text = "")
        self.label3.grid(row=4, column=1, sticky=W)
        
        #textbox that displays the vowels and consonants
        self.vowelsconsonants = Entry(self)
        self.vowelsconsonants.grid(row =3, column = 2, sticky = E)
        
        #textbox that displays the message
        self.text = Text(self, width =40, height = 10)
        self.text.grid(row =6, column =0, columnspan = 3, sticky = E)
        
        self.label3= Label(self, text = "")
        self.label3.grid(row=7, column=1, sticky=W)
        
        self.submit_button = Button(self, text="Submit  ", command=self.reveal)
        self.reset_button = Button(self, text="  Reset   ", command= self.reset)
        self.quit_button = Button(self, text="  Exit   ", command = self.quit)

        # LAYOUT

        self.submit_button.grid(row=8, column=0,sticky=W)
        self.reset_button.grid(row=8, column=1)
        self.quit_button.grid(row=8, column=2)
        
            # clears the textboxes
    def reset(self):
        self.vowelsconsonants.delete(0, END)
        self.text.delete(1.0, END)
        
    def validate(self, P):
        self.vowelsconsonants.config(state=(NORMAL if P else DISABLED))
        return True
        
    def reveal(self):
        words = defaultdict(list)
        outputlst = []
        inputWord = self.vowelsconsonants.get()
   
        # read from file and and populate the dictionary
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
                    outputlst =  words[result]
            length_of_word -= 1
        
        if(outputlst):
            for word in outputlst:
                if(word in outputlst):
                    self.text.insert(1.0, word + '\n')
                    
                print("Longest Generated Word is: ",word)
        else:
            self.text.insert(0.0, "Can't generate word...Please try again")

        
		
	
root = Tk()
root.title("James Ngondo 2016")
root.geometry("400x400")


app = Application(root)
root.mainloop()    
    
    
    
    
    
	