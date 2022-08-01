from time import sleep, time
from threading import Thread


class MyThread(Thread):
    def __init__(self, thread_id):
        Thread.__init__(self)
        self.id = thread_id
        self.start_time = 0
        self._loop = False

    def stop(self):
        self._loop = True
        self.join(timeout=1)

    def run(self, t=5):
        while not self._loop:
            print('Thread {} is running at {}'.format(self.id, self.start_time))
            sleep(t)
            self.start_time += t


if __name__ == "__main__":
    t1 = MyThread(1)
    t2 = MyThread(2)
    t3 = MyThread(3)
    t1.start()
    t3.start()
    start_time = time()
    while True:
        if (
                time() - start_time >= 20 and
                t1.is_alive() and
                not t2.is_alive()
        ):
            t1.stop()
            t2.start()
        if (
                time() - start_time >= 38 and
                t3.is_alive() and
                not t1.is_alive()
        ):
            t3.stop()
            t1 = MyThread(1)
            t1.start()
        if time() - start_time >= 100:
            break
    for t in [t1, t2, t3]:
        if t.is_alive():
            t.stop()
            t.join(timeout=1)
