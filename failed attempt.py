import os #data extraction
import time
from time import sleep, strftime, time

from os import listdir
from os.path import isfile, join #allows us to join folder to get data

#Class Instance

class UAV:
    def __init__(self, MAC):
       self.MAC = ()
       time_list = []
       velocity_list =[]
       self.url_path = ()
    
#define position
    @classmethod
    def position(cls, MAC, time):
        return cls(MAC, time.time() - time)
        #find position(use class attributes)
       

    

#get MAC values
#def getMAC(path):
 #   MAC = []
    onlyfiles = [f for f in listdir('/tmp/UNSY_329') if isfile(join('/tmp/UNSY_329', f))] #finds folder directory
    for file in onlyfiles:
        with open(join('/tmp/UNSY_329', file), 'r') as f: #locates files in folder
              first_line = f.readline()
              print (first_line) #prints first line in all 3 data folders to provide the MAC
        #return MAC
def main():

    while True: 
    #input handling code
        userInput = input("how many seconds do you want your data?\n").lower()
        if userInput == "yes":
            print("That's what I am talking about! Let's continue. Give me one moment while I execute commands.") #allows user to continue through process
            break #stops loop after yes is given
        if userInput == "no":
            print("If you insist, Goodbye.") #cuts code off
            exit() #exits commands
        elif userInput != "yes" "no":
            print("I only accept 1-5, please try again.") #prompts user to try again, restarts loop
#check range

#check our objects
            #uav1 = UAV(getMAC(path1))
            #uav2 = UAV(getMAC(path2))
            #uav3 = UAV(getMAC(path3))
main()
       