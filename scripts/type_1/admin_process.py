

def run(return_queue, flag_queue, process_count):
    print("admin flag queue : " + str(flag_queue.qsize()))


    while not flag_queue.empty():
        while not return_queue.empty():
            # print("admin qsize " + str(return_queue.qsize()))
            value = return_queue.get()
            print("admin value " + str(value))
