from serial import selection_sort


def sort(unsorted_array, thread_name = "Thread"):
    sorted_array = selection_sort.sort_array(unsorted_array)

    print()
    print(thread_name)
    print("Unsorted Array : " + str(unsorted_array))
    print("Selection Sort : " + str(sorted_array))





