
import array_splitter
from type_1 import thread
import threading

def run(unsorted_array):

    threads = []
    thread_count = 2

    print(unsorted_array)
    array_splitter.split(unsorted_array, thread_count)

    for i in range(thread_count):
        t = threading.Thread(target = thread.sort, args = (unsorted_array,))
        threads.append(t)
        t.start()
