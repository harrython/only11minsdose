from threading import Thread
class MyExam:
    def solved_question(self):
        self.q1()
        self.q2()
        self.q3()

    def q1(self):
        print("Hello")
    def q2(self):
        print("Pilla")
    def q3(self):
        print("Laila")

Myt= MyExam()
t = Thread(target=Myt.solved_question)
t.start()
