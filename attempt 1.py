
import sys
import datetime

from time import sleep, strftime, time
#Class Instance
class UAV:
    def __init__(self, MAC):
        self.MAC = MAC
        self.time = []
        self.velocity_list =[]      
        self.url_path = ()
        self.position = []
#define position
    @classmethod
    def position(cls, MAC, time):
        return cls(MAC, time.time() - time)
        #find position(use class attributes)
    
#find velocity (position)    
    def addData(self, urlFile):
        myFile = open(urlFile, "r")
        with myFile as fp:
            for cnt, line in enumerate(fp):
                if cnt == 0: continue
                current_record = line.split(",")
                self.time.append(float(current_record[0]))
                self.position.append(float(current_record[1]))
        myFile.close()
    
    
    
    def findposition(time): #got this portion from file
        intFile += 1
        myMAC = get_MAC_address() #generates a random MAC address for UAV
        timeStart = time.time() #store the original start time
        timeNow = time.time()   #initialize the timeNow that will be updated in the loop
        delay = 0.2             #set the delay between each velocity reading
        velocity = 0.0 

 
def getMAC(urlFile1):
    myFile = open("/tmp/UNSY_329/3_4_Data_1.cvs", "r")#opens directory
    if (myFile.mode == "r"):
        line = str(myFile.readline())
        MAC_Int = str(line)
        print('UAV 1:', MAC_Int)
    else:
        line = 'Error: file not opened for reading.'
    myFile.close()#saves file
    return line
def getMAC2(urlFile2):
    myFile2 = open("/tmp/UNSY_329/3_4_Data_2.cvs", "r")#opens directory
    if (myFile2.mode == "r"):
        line = str(myFile2.readline())
        MAC2_Int = str(line)
        print('UAV 2:', MAC2_Int)
    else:
        line = 'Error: file not opened for reading.'
    myFile2.close()#saves file
    return line
def getMAC3(urlFile3):
    myFile3 = open("/tmp/UNSY_329/3_4_Data_3.cvs", "r")#opens directory
    if (myFile3.mode == "r"):
        line = str(myFile3.readline())
        MAC3_Int = str(line)
        print('UAV 3:',  MAC3_Int)
    else:
        line = 'Error: file not opened for reading.'
    myFile3.close()#saves file
    return line


def checkRange(myTimer, start, stop):
     if not start <= myTimer <= stop:
        myTimer = float(input("How many seconds would you like your data? 1-5  "))
        isValid = False
     else:
        isValid = True
     if not isValid:
         checkRange(myTimer, start, stop)
     return myTimer

def main():
    t = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    for i in range(1):
        
        urlFile1 = "/tmp/UNSY_329/3_4_Data_1.cvs"
        uav1 = UAV(getMAC(urlFile1))
        uav1.addData(urlFile1)
        urlFile2 = "/tmp/UNSY_329/3_4_Data_2.cvs"
        uav2 = UAV(getMAC(urlFile2))
        uav2.addData(urlFile2)
        urlFile3 = "/tmp/UNSY_329/3_4_Data_3.cvs"
        uav3 = UAV(getMAC(urlfile3))
        uav3.addData(urlFile3)
        
        print(t)
       # deltaDistance = abs(
        print("UAV: %s is %s meters away from UAV: %s at %s seconds") #prints temperature with decimal placement
        break
exit()