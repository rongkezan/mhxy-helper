import threading
import time


class MyThread(threading.Thread):
    def run(self) -> None:
        print(time.time())


t1 = MyThread()
t2 = MyThread()
t1.start()
t2.start()
