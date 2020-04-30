# Python program for implementation of Selection
# Sort

import time
from numba import jit, cuda

@jit(target = "cuda")
def sort_array(unsorted_array):
    start_time = time.clock()

    sorted_array = unsorted_array.copy()
    ua_len = len(sorted_array)
    # Traverse through all array elements
    for i in range(ua_len):

        # Find the minimum element in remaining
        # unsorted array
        min_idx = i
        for j in range(i + 1, ua_len):
            if sorted_array[min_idx] > sorted_array[j]:
                min_idx = j

            # Swap the found minimum element with
        # the first element
        sorted_array[i], sorted_array[min_idx] = sorted_array[min_idx], sorted_array[i]


    end_time = time.clock()
    total_time = end_time - start_time

    return total_time, sorted_array

