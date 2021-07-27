# same thread multiple times acquire kr sakta hai
from threading import *
class Flight:
    def __init__(self, available_seat):
        self.available_seat = available_seat
        self.l = RLock()
        #print(self.l)

    def reserve(self, need_seat):
        self.l.acquire()        #multi times acquire kr sakte hai
        self.l.acquire()
        #print(self.l)
        print('Available Seat:', self.available_seat)
        if(self.available_seat >= need_seat):
            name = current_thread().name
            print(f'{need_seat} seat is alloted for {name}')
            self.available_seat -= need_seat

        else:
            print('Sorry! All seats has alloted')
        self.l.release()
        self.l.release()        #multi time release bhi karna padega

f = Flight(2)
t1 = Thread(target = f.reserve, args=(1,), name='Rahul')
t2 = Thread(target = f.reserve, args=(1,), name='Sonam')
t3 = Thread(target = f.reserve, args=(1,), name='Sona')
t1.start()
t2.start()
t3.start()
