import random as rand 
import pandas as pd 
import sklearn as sk 
import matplotlib as plt 
import seaborn as sea 
import qrcode as qr
import sys

class Number:
    def __init__(self):
        self.number = []
        
    def singleDigit(self):
        digit = rand.randint(1, 9)
        self.number.append(digit)
       
    def doubleDigit(self):
        digit = rand.randint(10, 99)
        self.number.append(digit)
       
    def tripleDigit(self):
        digit = rand.randint(100, 999)
        self.number.append(digit)
        
    def fourthDigit(self):
        digit = rand.randint(1000, 9999)
        self.number.append(digit)
          
    def displayNum(self):
       print(self.number)

    def saveNumber(self):
        with open('numbers.txt', "w") as f:
            f.writelines(', '.join(map(str, self.number)))
        df = pd.DataFrame(self.number)
        df.to_csv('number.csv', index=False)
        print(df)
        
def main():
    while True:
        number = Number()
        number.singleDigit()
        number.doubleDigit()
        number.tripleDigit()
        number.fourthDigit()
        number.displayNum()
        number.saveNumber()
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
    
    
    

