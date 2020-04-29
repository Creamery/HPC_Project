
import array_splitter
from parallel import thread
import threading

def run(unsorted_array):

    threads = []
    thread_count = 2

    print(unsorted_array)
    unsorted_arrays = array_splitter.split(unsorted_array, thread_count)

    for i in range(thread_count):
        t = threading.Thread(target = thread.sort, args = (unsorted_arrays[i], "Thread " + str(i),))
        threads.append(t)
        t.start()
