
from serial import process_handler
import input_reader


def run(unsorted_array):
    elapsed_time, sorted_array = process_handler.run(unsorted_array)
    return elapsed_time, sorted_array




