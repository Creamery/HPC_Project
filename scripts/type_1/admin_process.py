

def run(return_queue, flag_queue, process_count):

    while not flag_queue.empty():
        while not return_queue.empty():
            value = return_queue.get()
            print(value)

