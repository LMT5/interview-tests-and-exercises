import threading
import time
import sys

class FooBar():
    def __init__(self, n):
        self.n = n
        #self.mutex = threading.Mutex()
        self.cv = threading.Condition()
        self.count = 0
        #self.foo()
        threads = []
        threads.append(threading.Thread(target = self.foo))
        threads.append(threading.Thread(target = self.bar))
        threads.append(threading.Thread(target = self.yeah))
        threads[0].start()
        threads[1].start()
        threads[2].start()
        for i in range(3):
            threads[i].join()

    def foo(self):
        for _ in range(int(self.n)):
            with self.cv:
                while self.count != 0:
                    self.cv.wait()
                print("foo",end = "", flush = True)
                self.count = 1
                self.cv.notifyAll()
            

    def bar(self):
        for _ in range(int(self.n)):
            with self.cv:
                while self.count != 1:
                    self.cv.wait()
                print("bar",end = "", flush = True)
                self.count = 2
                self.cv.notifyAll()
                

    def yeah(self):
        for _ in range(int(self.n)):
            with self.cv:
                while self.count != 2:
                    self.cv.wait()
                print("yeah", flush = True)
                self.count = 0
                self.cv.notifyAll()
        

FooBar(sys.argv[1])