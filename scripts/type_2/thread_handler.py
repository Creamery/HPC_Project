from type_2 import thread
import threading


def run(unsorted_array):

    threads = []
    threads_num = 2

    for i in range(threads_num):
        t = threading.Thread(target = thread.sort, args = (unsorted_array,))
        threads.append(t)
        t.start()
