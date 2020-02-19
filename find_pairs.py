"""
Expects data of a Tachymeter.
Find pairs by comparing their IDs and vertical angle.
Sorts them such that "Lage 1" is before "Lage 2".
"""

import math


def create_sorted_list(dataset):
    """
    Iterates over each entry of dataset and sorts every pair.
    """
    header = f" Nr.; Hz Lage I; Hz Lage II; Vt Lage I; Vt Lage II;"\
             f" S Lage I; S Lage II; NP Lage I; NP Lage II"
    dummy = ['', '99999', '99999', '99999', '99999']
    new_list = [header]
    size = len(dataset)
    idx = 0
    nl = '\n'
    while idx < size:
        if idx + 1 < size:
            A = dataset[idx]
            B = dataset[idx + 1]
            if math.isclose(A[2] + B[2], 400, rel_tol=1e-04):
                if A[0] == B[0]:
                    lage_1, lage_2 = sort_pair_by_lage(A, B)
                    # print("Lage 1:")
                    # print(lage_1)
                    # print("Lage 2:")
                    # print(lage_2)
                    new_list.append(merge_pair(lage_1, lage_2))
                    # print(merge_pair(lage_1, lage_2))
                    # print("/////////////////////")
                    idx += 1  # prevents iterating over B in the next cycle
                else:
                    # raise ValueError(
                    print(
                        f'Vertical angles are close to 400 but IDs are '\
                        f'different: {nl}'\
                        f'1. entry: {A[0]}, {A[2]}{nl}'\
                        f'2. entry: {B[0]}, {B[2]}')
                    print('Assuming they belong to the same point/target.')
                    lage_1, lage_2 = sort_pair_by_lage(A, B)
                    new_list.append(merge_pair(lage_1, lage_2))
                    idx += 1
            else: # A and B are not a pair
                new_list.append(merge_pair(A, dummy))
            idx += 1
        else:  # A is the last entry in the dataset and therefore cannot form a pair
            A = dataset[idx]
            new_list.append(merge_pair(A, dummy))
            idx += 1
    return new_list


def merge_pair(A, B):
    """
    Merge values of A and B.

    Returns a string.
    """
    if A[0] == B[0]:
        id = A[0]
    elif A[0] != "" and B[0] == "":
        id = A[0]
    elif A[0] == "" and B[0] != "":
        id = B[0]
    else:
        id = "XXX"

    merged = f"{id};"\
        f"{A[1]};{B[1]};"\
        f"{A[2]};{B[2]};"\
        f"{A[3]};{B[3]};"\
        f"{A[4]};{B[4]}"
    return merged


def sort_pair_by_lage(candidate_a, candidate_b):
    """
    Checks Lage of both candidates and puts Lage 1 before Lage 2.

    A_candidate, B_candidate: lists
    return: list of sorted candidates.
    """
    # vertical angle <= 200 means Lage 1 and >= 200 means Lage 2
    # TODO: if both are the same order in a specfic way or does it not matter?
    if candidate_a[2] <= 200 and candidate_b[2] >= 200:
        return (candidate_a, candidate_b)
    else:
        return (candidate_b, candidate_a)
