import pprint
import smtplib
import random
import time

choreAssign = []
emailList = ['Dad', 'Abdulquadri', 'Rodiat', 'BrotherSodiq', 'Abdulbadie']
choresList = ['dishes and kitchen', 'bathroom', 'sweep', 'toilet', 'mop', 'wash car', 'cook', 'clean shoes',
              'iron clothes']
file = open(r"C:\Users\Abdulbadie\OneDrive\User\PycharmProjects\My_Python_for_Automation_Journey"
            r"\18_Sending_Email_And_Text_Messages\choreHistory.txt")
choreHistory = file.read()
file.close()

smtpObj = smtplib.SMTP_SSL('smtp.gmail.com', 465)
smtpObj.ehlo()
smtpObj.login('gbejiwumi2002@gmail.com', 'uxxxxxxxxxx')

random.shuffle(emailList)
while len(choresList) != 0:
    for email in emailList:
        if len(choresList) == 0:
            break
        randomChore = random.choice(choresList)

        # To avoid giving the same chore to the same person as previously
        while f'[{email}] = {randomChore}' in choreHistory and len(choresList) > 1:
            randomChore = random.choice(choresList)

        choreAssign.append(f'[{email}] = {randomChore}')
        message = f'Subject: Weekly chore.\nYour chore this week is {randomChore}'
        smtpObj.sendmail('gbejiwumi2002@gmail.com', f'{email}@gmail.com', message)
        time.sleep(3)
        choresList.remove(randomChore)  # This chore is now taken and should be removed

# Print and save the chore
pprint.pprint(choreAssign)
file = open(r"C:\Users\Abdulbadie\OneDrive\User\PycharmProjects\My_Python_for_Automation_Journey"
            r"\18_Sending_Email_And_Text_Messages\choreHistory.txt", 'w')
file.write(str(choreAssign))
file.close()
smtpObj.quit()
