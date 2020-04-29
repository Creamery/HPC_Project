
import csv
import os

def read_csv(file_name = "input_10"):
    contents = []
    parent_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    with open(parent_path + "\\test_data\\" + file_name + ".csv", encoding = 'utf-8-sig') as csv_file:
        reader = csv.reader(csv_file)  # change contents to floats
        for row in reader:  # each row is a list
            value = ','.join(row)
            contents.append(int(value))

    # print(contents)
    return contents






