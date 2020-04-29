

def run(return_queue, flag_queue, process_count):
    print("admin flag queue : " + str(flag_queue.qsize()))

    sorted_array = []

    while not flag_queue.empty():
        while not return_queue.empty():
            # print("admin qsize " + str(return_queue.qsize()))
            tuple = return_queue.get()
            value = tuple[0]
            process_id = tuple[1]
            print(str(value) + " from p " + str(process_id))

            if len(sorted_array) == 0:
                sorted_array.append(value)
            else:
                pointer_index = len(sorted_array) - 1
                pointer_value = sorted_array[pointer_index]

                while value < pointer_value and pointer_index > -1:
                    pointer_index = pointer_index - 1
                    pointer_value = sorted_array[pointer_index]

                pointer_index = pointer_index + 1

                print("ptr val : " + str(pointer_value))
                sorted_array.insert(pointer_index, value)
                print("sorted array contents : ")
                print(sorted_array)
                print()

    print(sorted_array)
