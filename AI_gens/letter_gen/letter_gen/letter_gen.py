import random as rand 
import pandas as pd 
import matplotlib as plt 
#import tensorflow as tf 
#from tensorflow import Keras 
import qrcode as qr 
import pandas as pd 
import sys

class Letter:
    def __init__(self):
        self.letter = []
        
    def upperAlpha(self):
        self.letter = ["A", 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        rand.shuffle(self.letter)

    def lowerAlpha(self):
        self.letter = [letter.lower() for letter in self.letter]
        rand.shuffle(self.letter)
        
    def displayLetter(self):
        print(self.letter)
       
    def saveLetter(self):
        with open("letter.txt", "w") as f:
            f.writelines(', '.join(map(str, self.letter)))
        df = pd.DataFrame(self.letter)
        df.to_csv('letter.csv', index=False)
        print(df)

def main():
     while True:    
        alphabet = Letter()
        alphabet.upperAlpha()
        alphabet.lowerAlpha()
        alphabet.displayLetter()
        alphabet.saveLetter()
        break

def runAgain():
    print("Would you like to run the application again?\n")
    run_again = input("Y/N\n")
    if run_again.upper() == "Y":
        main()
    else:
        sys.exit()

if __name__ == "__main__":
    main()
    while True:
        runAgain()
    
   
