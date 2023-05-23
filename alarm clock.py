from datetime import datetime
from playsound import playsound 
alarmHour = int (input("enter Hour: "))
alarmMin = int (input("enter Minutes: "))
alarmAm= input("am / pm: ")
if (alarmAm =="pm"):
    alarmHour += 12
while True:
     if alarmHour==datetime.now().hour and alarmMin==datetime.now().minute :
        print("WAKE UP!!")
        playsound("jvke-golden-hour-songreelscom_mgxjWTHr.mp3")
        break
