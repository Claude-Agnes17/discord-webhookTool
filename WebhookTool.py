import requests
import os
import time
import pyfiglet

banner = pyfiglet.figlet_format("ClaudeAgnes")
print(banner)

print("----------------")
print("1. Spammer")
print("2. Sender")
print("3. EXIT")
print("----------------")

inputed_number = int(input("Select Number : "))

if inputed_number == 1:
    msg = input("Spam Message : ")
    webhook = input("WebHook URL : ")
    def spam(msg, webhook):
        while True:
            try:
                data = requests.post(webhook, json={'content': msg})
                if data.status_code == 204:
                    print(f"Sent MSG {msg}")
            except:
                print("Bad Webhook :" + webhook)
                time.sleep(5)
                exit()
    ClaudeAgnes_top = 1
    while ClaudeAgnes_top == 1:
        spam(msg, webhook)

elif inputed_number == 2:
    print(" ")
    def cls():
        os.system('cls' if os.name=='nt' else 'clear')
    wh = input("WebHook : ")
    name = input("Username : ")
    cls()
    while True:
        msg = input("Message --> ")
        requests.post(wh,json={'content': msg, 'Username' : name})
        cls()
        time.sleep(0.0000000001)

elif inputed_number == 3:
    exit()

else:
    print("Try again")

