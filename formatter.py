"""
Expects data of a tachymeter.
Holds a set of functions to format the data.
"""

import find_pairs

def create_new_list(list_of_data):
    new_list = [create_header()]
    size = len(list_of_data)
    dummy = ['', '99999', '99999', '99999', '99999']
    idx = 0
    while idx <= size:
        print(idx)
        if idx == size-1 and size % 2 == 0 or idx == size-2 and size % 2 == 1:
            return new_list
        elif find_pairs.is_same_target(list_of_data[idx], list_of_data[idx+1]):
            new_list.append(merge_pair(list_of_data[idx], list_of_data[idx+1]))
            idx += 1
            print("increased idx: " + str(idx))
        # add dummy values if only one Lage was measured
        else:
            if list_of_data[idx][2] <= 200:
                new_list.append(merge_pair(list_of_data[idx], dummy))
            else:
                new_list.append(merge_pair(dummy, list_of_data[idx]))
            pass
        idx += 1

def create_header():
    #<5 chars>|<12 chars>|<12 chars>| ...
    header = (f" Nr. |  Hz Lage I | Hz Lage II |  Vt Lage I | Vt Lage II |"
              f"   S Lage I |  S Lage II |  NP Lage I | NP Lage II ")
    return header

def merge_pair(A, B):
    if A[0] == B[0]:
        id = A[0]
    elif A[0] != "" and B[0] == "":
        id = A[0]
    elif A[0] == "" and B[0] != "":
        id = B[0]
    else:
        id = "XXX"

    merged = f"{id:^{5}}|"\
        f"{A[1]:^{12}}|{B[1]:^{12}.{5}}|"\
        f"{A[2]:^{12}}|{B[2]:^{12}.{5}}|"\
        f"{A[3]:^{12}}|{B[3]:^{12}.{5}}|"\
        f"{A[4]:^{12}}|{B[4]:^{12}.{5}}"
    return merged

def split_at_minus_and_plus(list_of_data):
    """
    Splits each value for each element of list_of_data at '+' or '-'.
    From the list of splitted values keep the last element.

    Returns a list holding lists of fractional values. 
    """

    for idx_a, ele in enumerate(list_of_data):
        split_plus = [value.split('+') for value in ele]
        for idx_b, bar in enumerate(split_plus):
            if '-' in bar[-1]:
                split_minus = bar[-1].split('-')
                split_plus[idx_b] = [split_minus[-1]]
        for idx_b, bar in enumerate(split_plus):
            list_of_data[idx_a][idx_b] = bar[-1]
    return list_of_data

def remove_leading_zeros(list_of_data):
    """
    Convert all values to integer else remove leading zeros.
    """
    for idx_outer, ele_outer in enumerate(list_of_data):
        for idx_inner, ele_inner in enumerate(ele_outer):
            if idx_inner != 0:
                reduced_value = float(ele_inner)
            else:
                reduced_value = ele_inner.lstrip('0')
            list_of_data[idx_outer][idx_inner] = reduced_value
    return list_of_data

def do_X_over_values(list_of_data, X, row_begin, row_end):
    """
    Manipulates each entry from row_begin to row_end using function X.

    Returns manipulated list_of_data.
    """

    for idx, entry in enumerate(list_of_data):
        for row in range(row_begin, row_end):
            list_of_data[idx][row] = X(entry[row])
    return list_of_data