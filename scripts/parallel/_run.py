from parallel import process_handler
import input_reader

if __name__ == '__main__':
    print("Parallel Selection Sort")
    unsorted_array = input_reader.read_csv("input_10")
    process_handler.run(unsorted_array)






