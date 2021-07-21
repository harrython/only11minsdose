from threading import *

class Mythread(Thread):
    def __init__(self):
        Thread.__init__(self)
        print("Child Thread Constructor")

    def run(self):
        pass

t= Mythread()
t.start()
print("main thread")


print()
#how can I pass the parameter
class Mytread(Thread):
    def __init__(self, a):
        Thread.__init__(self)
        print("Child Class Constructor", a)

    def run(self):
        pass

t1= Mytread(10)
t1.start()
print("Main Thread")
