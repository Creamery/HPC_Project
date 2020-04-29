
import numpy


def run1(passable_queue, passable_queue1, param_b):
    print("passable_queue size : " + str(passable_queue.qsize()))
    print("passable_queue : " + str(passable_queue.get()))

    print("passable_queue2 : " + str(passable_queue1.get()))

    print("param_b : " + str(param_b))
    # print("b : " + str(b))
    print()
    return int(param_b) + 1


def run(name, return_queue, unsorted_array, flag_queue):
    while len(unsorted_array) > 0:

        print(name)
        # print("unsorted array : " + str(unsorted_array))

        min_value = float('inf')
        min_index = 0

        for index in range(len(unsorted_array)):
            item = unsorted_array[index]
            if item < min_value:
                min_value = item
                min_index = index

        return_queue.put(min_value)
        # print("index : " + str(min_index))
        # del unsorted_array[min_index]
        unsorted_array = numpy.delete(unsorted_array, min_index)
        # print("unsorted_array size : " + str(len(unsorted_array)))
        # print()
        # unsorted_array = unsorted_array[0:min_index - 1] + unsorted_array[min_index + 1:-1]


    flag_queue.get()

