#creating a Thread using child class thread
#isme hm start() run() join() dekhenge

from threading import Thread
class Mythread(Thread):
    pass

t = Mythread()
print(t.name)
print()
#run Method
class Mytread(Thread):
    def run(self):
        print("Run Method", t1.name)

t1=Mytread()
t1.start()          #t1 start hone k baad hi run execute hota hai
print()
#join Method
class Mytrend(Thread):
    def run(self):
        for i in range(5):
            print("Child Class")

t2= Mytrend()
t2.start()
t2.join()               #ab pahle ek thread ko run karega uske baad next thread...
for i in range(5):
    print("Main Thread")







