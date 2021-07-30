from threading import Thread, Condition
from time import sleep
lst = []

def produce():
    cv.acquire()
    for i in range(1, 6):
        lst.append(i)
        sleep(1)
        print('Item Produced.....')
    cv.notify()                     #ab yeh notice jo wait kr rha hai uske pass chla jayega are u okay lounde
    cv.release()

def consume():
    cv.acquire()
    cv.wait(timeout=0)              #yeh jagega aur lock ko release krega fir print karega
    cv.release()
    print(lst)

cv = Condition()
t1 = Thread(target = produce)
t2 = Thread(target = consume)
t1.start()
t2.start()
