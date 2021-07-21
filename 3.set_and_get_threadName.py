from threading import Thread, current_thread

def disp():
    print("Child Thread Object", current_thread().getName())

t1 = Thread(target= disp)
t1.start()

print("Main Thread", current_thread().getName())



print()
#ab thread ka name change karna hai
def kisp():
    print("Default Child Thread", current_thread())
    current_thread().setName("Harry Thread")
    print("New Child Thread", current_thread().getName())

t2 = Thread(target = kisp)
t2.start()
print("Default Main Thread", current_thread())
current_thread().setName("geeky")
print("New Main Thread", current_thread().getName())


print()
#name janane k liye name property ka bhi use kr sakte hai
def sipcy():
    print("Default Child Thread", current_thread().name)
    current_thread().name = "FlyingThread"
    print("New child Thread", current_thread().name)

t3 = Thread(target= sipcy)
t3.start()
print("Default Main_Thread", current_thread().name)
current_thread().name = "madarchodThread"
print("New Main_Thread", current_thread().name)



print()
print()
#is tarah bhi kr sakte hai
def terima():
    pass
t = Thread(target= terima)
print("Default", t.name)
t.name = 'Flying Thread'
print("New", t.name)


print()
##ya phir iss tareh se direct name changge kr sakte hai
def ghanta():
    pass
tt= Thread(target= ghanta, name= 'ghantathread')
print(tt.name)




