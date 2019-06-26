from win10toast import ToastNotifier
from pycricbuzz import Cricbuzz
import time
cric          = Cricbuzz()
details     = cric.matches()
 
#To filter out the None objects from details
details=filter(None, details)
message="No match in progress"
 
for i in details:
    # traversing i
    if 'mchstate' in i:
      if i['mchstate']== 'inprogress':
        id= i['id']
        main=cric.livescore(id)
        ms =main['batting']['score'][0]
        bat1=main['batting']['batsman'][0]
        bat2=main['batting']['batsman'][1]
        #print(bat1['name'])
        message=i['srs']+ "      "+"Format: "+i['type'] +  "\n" + "Score: " +main['batting']['team']+" "+ms['runs'] +'/'+ms['wickets'] +" ("+ms['overs']+")"+"\n" +bat1['name']+":"+bat1['runs']+"("+bat1['balls']+")   "+ bat2['name']+":"+bat1['runs']+"("+bat2['balls']+")"


toaster = ToastNotifier()
prev_time = time.time()
while(True):
        if(time.time() - prev_time > 2):
            toaster.show_toast("Sample Notification",message)
            prev_time = time.time()
        
'''
import pyautogui as p
import time
import webbrowser as w
#Declaring the variables.
x = input("Type the name of receiver: ").strip()
y = input("Type message: ").strip()
s = int(input("Enter HOUR: "))
c = int(input("Enter MINUTE: "))
print("The message will be sent at the given time")
if (s == 00):
    s = 24
if (c == 00):
    c = 60
    s = s-1
while True:
    #Checks forever whether given time is equal to current time.
    l = time.localtime(time.time())
    if(l.tm_hour == s)&(l.tm_min == (c-1)):
        w.open('https://web.whatsapp.com/')
        time.sleep(60)
        p.click(76,156,interval=0.5,button='left') 
        p.typewrite(x,0.1)     
        p.press('enter')
        time.sleep(1)
        p.typewrite(y,0.1)
        p.press('enter')
        break;
'''
