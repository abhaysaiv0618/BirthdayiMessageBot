#download & pip imessage library: https://pypi.org/project/py-imessage-shortcuts/
import imessage, time

#Sends Birthday Message
def sendBirthdayMessage(phone, name):
    message = "Happy Birthday " + name
    imessage.send(phone, message)
    time.sleep(3)

#Sends text on days it is no ones birthday ->used to ensure scheduling function through Cron Job is working
def nothingSpecial(phone):
    message = "No one's Birthday Today... \n \n -Sent from your BirthdayMessageBot"
    imessage.send(phone, message)
    time.sleep(3)
    
#Reminder that it is the persons birthday
def Reminder(phone, name):
    message1 = "REMINDER: It is " + name + "'s Birthday! Wish them a Happy Birthday! \n \n -Sent from your BirthdayMessageBot"
    imessage.send(phone, message1)
