"""
Commandline interface to start execution of a model.
"""
import argparse
import os
from pprint import pprint as pp

import formatter
import find_pairs

"""
Load a config file to create a neural network.

usage: simple_configloader.py [-h] [-c C [C ...]] F

positional arguments:
  F                     Path to the config.yml you want to use.

optional arguments:
  -h, --help            show this help message and exit
  -c C [C ...], --corpus C [C ...]
                        Path to folder holding the corpus you want to train
                        on. Can be multiple paths.
"""

PARSER = argparse.ArgumentParser(
    description="Load a file from a tachymeter to format and order it.")
PARSER.add_argument(
    "TACHYMETER_FILE", metavar="F", type=str,
    help="Path to the file from a tachymeter you want to use.")
""" OPTIONAL ARGUMENT EXAMPLE
PARSER.add_argument(
    "-c", "--corpus", metavar="C", type=str, nargs='+',
    help="Absolut path to folder holding the corpus you want to train on.\
          Can be multiple paths.")
"""
ARGS = PARSER.parse_args()
GON_PRECISION = 5
DISTANCE_PRECISION = 3

def prepare_data(tachymeter_file):
    # load file and read it line by line
    with open(tachymeter_file) as f:
        # split each line at " " and store the result in a list
        list_of_data = [line.split() for line in f.readlines()]
        # throw away the first data entry
        if len(list_of_data[0]) is 4:
            list_of_data = list_of_data[1:len(list_of_data)]
            print("Ignoring first entry in the dataset.")
    
    # keep only the first 5 values per entry
    for idx, ele in enumerate(list_of_data):
        list_of_data[idx] = ele[0:5]
    list_of_data = formatter.split_at_minus_and_plus(list_of_data)
    return list_of_data

def start_formatting():
    """
    Load file, format it, save a formatted version of it.
    """
    list_of_data = prepare_data(ARGS.TACHYMETER_FILE)
    list_of_data = formatter.split_at_minus_and_plus(list_of_data)
    list_of_data = formatter.remove_leading_zeros(list_of_data)
    list_of_data = formatter.do_X_over_values(
        list_of_data,
        X = (lambda val: val / 10**GON_PRECISION),
        row_begin = 1,
        row_end = 3 # this will apply X over rows 1 and 2 excluding 3
    )
    list_of_data = formatter.do_X_over_values(
        list_of_data,
        X = (lambda val: val / 10**DISTANCE_PRECISION),
        row_begin = 3,
        row_end = 4 # this will apply X over rows 1 and 2 excluding 3
    )
    list_of_data = find_pairs.sort_dataset_by_lage(list_of_data)
    pp(list_of_data)
    # sort lines depending on "lage1" or "lage2"
    # format the values (removing unwanted precision and values[rows])
    #   also adds a header
    # some feedback that the process is done and where the file can be found

if __name__ == "__main__":
    start_formatting()