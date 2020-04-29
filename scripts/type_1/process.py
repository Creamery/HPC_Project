
import numpy


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

