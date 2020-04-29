from type_1 import thread_handler
import input_reader

def main():

    unsorted_array = input_reader.read_csv()
    thread_handler.run(unsorted_array)

main()




