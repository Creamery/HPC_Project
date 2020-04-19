# Python program for implementation of Selection
# Sort
import sys


def sort_array(unsorted_array):

    ua_len = len(unsorted_array)
    # Traverse through all array elements
    for i in range(ua_len):

        # Find the minimum element in remaining
        # unsorted array
        min_idx = i
        for j in range(i + 1, ua_len):
            if unsorted_array[min_idx] > unsorted_array[j]:
                min_idx = j

            # Swap the found minimum element with
        # the first element
        unsorted_array[i], unsorted_array[min_idx] = unsorted_array[min_idx], unsorted_array[i]

    # Driver code to test above
    print("Sorted array")
    for i in range(ua_len):
        print("%d" % unsorted_array[i])



