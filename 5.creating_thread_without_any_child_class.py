#Creating a thread without using class
#Creating a thread by creating a child class to thread class
#Creating a thread without creating child class to thread class

from threading import Thread
class Mythread:
    def disp(self, a):
        print(a)

myt = Mythread()

t = Thread(target = myt.disp, args=(23,))
t.start()

#sabse imp method hai yeh





