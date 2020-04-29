
import multiprocessing
from multiprocessing import Process, Lock, Queue, Pool
from admin_process import run as admin_run
from process import run as process_run
from process import run1 as process_run1
import array_splitter

from itertools import product
from functools import partial

def run(unsorted_array):
    count_process = 2

    pool = Pool(processes = count_process)

    queue = Queue(0)
    queue_flag = Queue(0)

    for i in range(count_process):
        queue_flag.put("Done")

    admin = Process(target = admin_run, args = (queue, queue_flag, count_process,))
    admin.start()

    unsorted_arrays = array_splitter.split(unsorted_array, count_process)

    process_pool = []
    input_list = []

    for index in range(len(unsorted_arrays)):
        item = unsorted_arrays[index]
        process = Process(target = process_run, args = ("Thread " + str(index), queue, item, queue_flag,))
        process_pool.append(process)  # Store the processes in an array

        input_list.append(("Thread " + str(index), queue, item, queue_flag))


    manager = multiprocessing.Manager()
    passable_queue = manager.Queue()
    passable_queue2 = manager.Queue()

    passable_queue.put("1")
    passable_queue.put("2")

    passable_queue2.put("3")
    passable_queue2.put("4")

    param_b = [1, 2]
    func0 = partial(process_run1, passable_queue)
    func = partial(func0, passable_queue2)
    results = pool.map(func, param_b)
    print(results)
    # print(input_list)
    # pool.map(wrapper, input_list)
    # wrapper(input_list[1])

    # pool.map(wrapper, input_list[0])
    print()
    for process in process_pool:
        process.start()
    #     process.join()
