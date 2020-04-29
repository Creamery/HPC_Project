
import multiprocessing
from multiprocessing import Process, Lock, Queue, Pool
from admin_process import run as admin_run
from process import run as process_run
import array_splitter
from functools import partial


def run(unsorted_array):
    count_process = 4

    pool = Pool(processes = count_process)

    manager = multiprocessing.Manager()
    # passable_queue = manager.Queue()
    # passable_queue2 = manager.Queue()
    queue = manager.Queue()
    queue_flag = manager.Queue()

    for i in range(count_process):
        queue_flag.put("Done")

    admin_function_0 = partial(admin_run, queue)
    admin_function_1 = partial(admin_function_0, queue_flag)
    iterable = [count_process]
    pool.map_async(admin_function_1, iterable)


    # admin = Process(target = admin_run, args = (queue, queue_flag, count_process,))
    # admin.start()

    unsorted_arrays = array_splitter.split(unsorted_array, count_process)
    unsorted_tuples = []
    for item in unsorted_arrays:
        unsorted_tuples.append(tuple(item))

    process_id = range(count_process)
    worker_partial_1 = partial(process_run, queue)
    worker_partial_2 = partial(worker_partial_1, queue_flag)
    worker_partial_3 = partial(worker_partial_2, unsorted_tuples)
    pool.map(worker_partial_3, process_id)

    pool.close()
    # pool.join()


    # for index in range(len(unsorted_arrays)):
    #     item = unsorted_arrays[index]
    #     process = Process(target = process_run, args = ("Thread " + str(index), queue, item, queue_flag,))
    #     process_pool.append(process)  # Store the processes in an array
    #
    #     input_list.append(("Thread " + str(index), queue, item, queue_flag))




    # passable_queue.put("1")
    # passable_queue.put("2")
    # passable_queue.put("3")
    #
    # passable_queue2.put("4")
    # passable_queue2.put("5")
    # passable_queue2.put("6")
    #
    # param_b = [[1, 2, 3, 4], [5, 6, 7, 8, 1, 2, 3, 4, 5, 6, 7], [9, 10, 11, 12]]
    # func0 = partial(process_run1, passable_queue)
    # func = partial(func0, passable_queue2)
    # results = pool.map(func, param_b)
    # print(results)

    # print(input_list)
    # pool.map(wrapper, input_list)
    # wrapper(input_list[1])

    # pool.map(wrapper, input_list[0])
    # print()
    # for process in process_pool:
    #     process.start()
    #     process.join()
