
from serial import selection_sort
from numba import jit


@jit(forceobj = True)
def run(unsorted_array):
    elapsed_time, sorted_array = selection_sort.sort_array(unsorted_array)

    return elapsed_time, sorted_array





