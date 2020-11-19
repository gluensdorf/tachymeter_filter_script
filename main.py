import argparse
import os
from pathlib import Path
from pprint import pprint as pp
import PySimpleGUI as sg 

import formatter
import find_pairs

# PARSER = argparse.ArgumentParser(
#     description="Load a file from a tachymeter to format and order it.")
# PARSER.add_argument(
#     "TACHYMETER_FILE", metavar="F", type=str,
#     help="Path to the file from a tachymeter you want to use.")
# ARGS = PARSER.parse_args()
GON_PRECISION = 5
DISTANCE_PRECISION = 3


def prepare_data(tachymeter_file):
    """
    Loads a file, throws away unwanted data and returns the remaining data.
    """
    # load file and read it line by line
    with open(tachymeter_file) as f:
        # split each line at " " and store the result in a list
        list_of_data = [line.split() for line in f.readlines()]
        # throw away the first data entry
        if len(list_of_data[0]) == 4:
            list_of_data = list_of_data[1:len(list_of_data)]
            # print("Ignoring first entry in the dataset.")
    
    # keep only the first 5 values per entry
    for idx, ele in enumerate(list_of_data):
        list_of_data[idx] = ele[0:5]
    list_of_data = formatter.split_at_minus_and_plus(list_of_data)
    return list_of_data


def start_formatting(path_to_tachymeter_file):
    """
    Load file, format it, save a formatted version of it.
    """
    list_of_data = prepare_data(path_to_tachymeter_file)
    list_of_data = formatter.split_at_minus_and_plus(list_of_data)
    list_of_data = formatter.remove_leading_zeros(list_of_data)
    list_of_data = formatter.do_X_over_values(
        list_of_data,
        X=(lambda val: val / 10**GON_PRECISION),
        row_begin=1,
        row_end=3  # this will apply X over rows 1 and 2 excluding 3
    )
    list_of_data = formatter.do_X_over_values(
        list_of_data,
        X=(lambda val: val / 10**DISTANCE_PRECISION),
        row_begin=3,
        row_end=4  # this will apply X over row 3 excluding 4
    )
    new_list = find_pairs.create_sorted_list(list_of_data)
    formatted_file_name = f"{Path(path_to_tachymeter_file.name).stem}_formatted.txt"
    formatted_file_path = path_to_tachymeter_file.parent
    f = open(formatted_file_path.joinpath(formatted_file_name), "w+")
    for ele in new_list:
        f.write(ele + "\n")
    return formatted_file_path.joinpath(formatted_file_name)


if __name__ == "__main__":
    layout = [
            [sg.Text('Browse to tachymeter file to format:')],
            [sg.Input(key='-FILE-', visible=False, enable_events=True), sg.FileBrowse()],
        ]

    event, values = sg.Window('File Compare', layout).read(close=True)

    print(f'You chose:\n{values["-FILE-"]}')
    path_to_tachymeter_file = Path(values["-FILE-"])
    created_file = start_formatting(path_to_tachymeter_file)
    print(f'Created formatted file:\n{created_file}')
