from multiprocessing import Process, Lock, Queue


def single_process(return_queue, lock, i, flag_queue):
    print('hello world', i)
    return_queue.put(i)

    for i in range(10000):
        j = i + 1

    flag_queue.get()
    # l.acquire()
    # try:
    #     print('hello world', i)
    #     return_queue.put(i)
    # finally:
    #     l.release()


def admin_process(return_queue, lock, flag_queue, process_count):

    while not flag_queue.empty():
        while not return_queue.empty():
            value = return_queue.get()
            print(value)


if __name__ == '__main__':
    l = Lock()
    queue = Queue()
    queue_flag = Queue()

    count_process = 20

    for i in range(count_process):
        queue_flag.put("Done")

    admin = Process(target = admin_process, args = (queue, l, queue_flag, count_process,))
    admin.start()


    process_pool = []
    for num in range(count_process):
        process = Process(target = single_process, args = (queue, l, num, queue_flag,))
        process.start()

        process_pool.append(process)  # Store the processes in an array



    # for process in process_pool:
    #     process.join()