'''
Print Even / Odd Numbers in Incremental order using two different threads.

Use
Thread1 - Generates Even Number
Thread2 - Generates Odd Number

Expected Output: 1 2 3 4 5 6 7 8 9 10
Thread2 - 1
Thread1 - 2
Thread2 - 3
Thread1 - 4
Thread2 - 5
Thread1-  6
Thread2 - 7
Thread1 - 8
Thread2 - 9
Thread1- 10
'''

import threading
import time

class multi_threads:
    def __init__(self):
        self.lock_event1 = threading.Event();
        self.lock_event2 = threading.Event();
        thread1 = threading.Thread(name="thread1", target=self.thread1_start)
        thread2 = threading.Thread(name="thread2", target=self.thread2_start)
        self.num = 1
        thread1.start()
        thread2.start()

    def thread1_start(self):
        while(self.num <= 9):
            self.lock_event2.clear()
            print(f"thread1={self.num}")
            self.num += 1
            self.lock_event1.set()
            self.lock_event2.wait()

    def thread2_start(self):
        while(self.num < 10):
            self.lock_event1.wait()
            print(f"thread2={self.num}")
            self.num += 1
            self.lock_event1.clear()
            self.lock_event2.set()

multi_threads()