import random, webbrowser, datetime, time
from datetime import datetime, timedelta
Time = time.strftime("%H:%M:%S")
print("")
print ("Currently it is:", Time)
minutes_of_sleep = int(input("Enter the number of minutes you would like to sleep for:"))
hours_of_sleep = int(input("Enter the number of hours you would like to sleep for:"))
print("")
Alarm = (datetime.now() + timedelta(hours=hours_of_sleep) + timedelta(minutes=minutes_of_sleep)).strftime('%H:%M:%S')
print("You will be woken up at:", Alarm)
yes_no = str(input("Would you like to set this alarm? [Y/N]")).lower()
print("Alarm not set!")
print("")

while yes_no == "y" or yes_no == "yes":

    while Time != Alarm:
        print("It is currently:", time.strftime("%H:%M:%S"))
        Time = time.strftime("%H:%M:%S")
        time.sleep(1)
        if Time == Alarm:
            print("")
            print("Time to wake up!")
            break