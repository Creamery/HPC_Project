
from serial import selection_sort


def run(unsorted_array):
    elapsed_time, sorted_array = selection_sort.sort_array(unsorted_array)
    print(sorted_array)

    return elapsed_time, sorted_array





