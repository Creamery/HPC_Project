# Python program for implementation of Selection
# Sort

import time


def sort_array(unsorted_array):
    start_time = time.clock()
    sorted_array = unsorted_array.copy()

    for i in range(len(sorted_array)):

        min_index = i
        for j in range(i + 1, len(sorted_array)):
            if sorted_array[min_index] > sorted_array[j]:
                min_index = j

        sorted_array[i], sorted_array[min_index] = sorted_array[min_index], sorted_array[i]

    end_time = time.clock()
    total_time = end_time - start_time

    return total_time, sorted_array

