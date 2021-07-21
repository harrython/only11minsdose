#Thread ek class hai threading module ka
#creating a thread without using a class

from threading import Thread
def disp(a):
    print("Thread Running", a)

t = Thread(target=disp, args=(10,))     #thread me arg pass karte waqt comma lagao to hi ek tupple mana jayega
t.start()
print()

# agar do arg ho to 
def disp(a,b):
    print("Thread Running", a, b)

t = Thread(target=disp, args=(10,20))
t.start()
# is thread ko hum multiple time start kr sakte hai ya run kr sakte hai
for i in range(5):     # 0 se 4 ke liye hoga 
    t = Thread(target=disp, args=(10,20))
    t.start()
print()

##Now 
def disp():
    for i in range(5):
        print("Publish Video C")

t = Thread(target=disp)     #only one thread starts

t.start()       #Now second thread starts here

for i in range(5):
    print("Publish Video M")




