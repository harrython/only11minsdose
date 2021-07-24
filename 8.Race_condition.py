from threading import Thread, current_thread
class Flight:
    def __init__(self, avalable_seat):
        self.avalable_seat = avalable_seat

    def reserve(self, need_seat):
        print('Avalable Seat:', self.avalable_seat)
        if(self.avalable_seat >= need_seat):
            name = current_thread().name
            print(f'{need_seat} seat is alloted for {name}')
            self.avalable_seat -= need_seat

        else:
            print('Sorry! All seats has alloted')

f = Flight(1)
t1 = Thread(target = f.reserve, args=(1,), name='Rahul')
t2 = Thread(target = f.reserve, args=(1,), name='Sonam')
t1.start()
t2.start()






