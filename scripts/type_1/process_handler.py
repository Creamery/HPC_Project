
from multiprocessing import Process, Lock, Queue
from admin_process import run as admin_run
from process import run as process_run


if __name__ == '__main__':
    queue = Queue()
    queue_flag = Queue()

    count_process = 20

    for i in range(count_process):
        queue_flag.put("Done")

    admin = Process(target = admin_run, args = (queue, queue_flag, count_process,))
    admin.start()


    # process_pool = []
    for num in range(count_process):
        process = Process(target = process_run, args = (queue, num, queue_flag,))
        process.start()

        # process_pool.append(process)  # Store the processes in an array



    # for process in process_pool:
    #     process.join()