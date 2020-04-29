

def run(return_queue, i, flag_queue):
    print('hello world', i)
    return_queue.put(i)

    for i in range(10000):
        j = i + 1

    flag_queue.get()

