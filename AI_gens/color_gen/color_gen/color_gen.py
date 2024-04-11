import random as rand
import qrcode as qr
import pandas as pd
#import tensorflow as tf
#from tensorflow import Keras
import sys 
import csv as c
import matplotlib.pyplot as plt 


class Color:
    def __init__(self):
        self.red = rand.randint(0, 255)
        self.blue = rand.randint(0, 255)
        self.green = rand.randint(0, 255)

    def displayColor(self):
        color = [self.red, self.green, self.blue]
        data = color
        img = qr.make(data)
        img.show()
        print(color)

    def saveColor(self):
        color = [self.red, self.green, self.blue]
        with open("color.txt", 'w') as f:
            f.writelines(', '.join(map(str, color)))
        df = pd.DataFrame([color], columns=['Red', 'Green', 'Blue'])
        df.to_csv('color.csv', index=False)
        print(df)

def main():
   while True:
        color_instance = Color()
        color_instance.displayColor()
        color_instance.saveColor()
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
        
    
   
