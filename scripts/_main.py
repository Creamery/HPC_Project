
from serial import _run as serial_run
from parallel import _run as parallel_run
import input_reader

if __name__ == '__main__':

    csv_array = input_reader.read_csv("input_1000")
    run_count = 3

    # print(csv_array)
    print("Parallel Selection Sort")
    average_time = 0
    sorted_array_parallel = []
    for i in range(run_count):
        unsorted_array = csv_array.copy()
        elapsed_time, sorted_array_parallel = parallel_run.run(unsorted_array)

        print("Elapsed Time : " + str(elapsed_time))
        average_time = average_time + elapsed_time

    print()
    average_time = average_time / run_count
    print("Average Time : " + str(average_time))
    # print(sorted_array_parallel)

    print()
    print()
    print()

    print("Serial Selection Sort")
    average_time = 0
    sorted_array_serial = []
    for i in range(run_count):
        unsorted_array = csv_array.copy()
        elapsed_time, sorted_array_serial = serial_run.run(unsorted_array)

        print("Elapsed Time : " + str(elapsed_time))
        average_time = average_time + elapsed_time

    print()
    average_time = average_time / run_count
    print("Average Time : " + str(average_time))
    # print(sorted_array_serial)


