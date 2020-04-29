
from multiprocessing import Process, Lock, Queue
from admin_process import run as admin_run
from process import run as process_run
import array_splitter


def run(unsorted_array):
    count_process = 2

    queue = Queue(0)
    queue_flag = Queue(0)

    for i in range(count_process):
        queue_flag.put("Done")

    admin = Process(target = admin_run, args = (queue, queue_flag, count_process,))
    admin.start()

    unsorted_arrays = array_splitter.split(unsorted_array, count_process)

    process_pool = []
    for index in range(len(unsorted_arrays)):
        item = unsorted_arrays[index]
        process = Process(target = process_run, args = ("Thread " + str(index), queue, item, queue_flag,))
        process_pool.append(process)  # Store the processes in an array

    for process in process_pool:
        process.start()
        process.join()