from threading import Thread
import time

THREAD_DELAY_SECONDS = 5


class CleanupThread(Thread):
    def __init__(self, shelves, pickup_queue):
        Thread.__init__(self)
        self.pickup_queue = pickup_queue
        self.shelves = shelves

    def __cleanup(self):
        removed = False
        for shelf in self.shelves.values():
            removed_order = shelf.cleanup_orders()
            if removed_order:
                removed = True
        if removed:
            print(self.shelves)

    def run(self, dryrun=False):
        while(not self.pickup_queue.end_pickup_thread()):
            self.__cleanup()
            if dryrun:
                break
            time.sleep(THREAD_DELAY_SECONDS)
