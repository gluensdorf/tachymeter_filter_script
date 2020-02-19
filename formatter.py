"""
Expects data of a tachymeter.
Holds a set of functions to format the data.
"""


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
            if idx_inner != 0 and idx_inner != 4:
                reduced_value = float(ele_inner)
            elif idx_inner == 4:
                reduced_value = int(ele_inner) 
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
