"""
Expects data of a Tachymeter.
Find pairs by comparing their IDs and sort them such that "Lage 1" is before
"Lage 2".
"""

def sort_dataset_by_lage(dataset):
    """
    Iterates of each entry of dataset and sorts every pair.
    """
    size = len(dataset)
    for idx in range(size):
        if idx == size and size % 2 == 0 or idx == size-1 and size % 2 == 1:
            return dataset
        elif is_same_target(dataset[idx], dataset[idx + 1]):
            lage_1, lage_2 = sort_pair_by_lage(
                dataset[idx], 
                dataset[idx + 1]
                )
            dataset[idx] = lage_1
            dataset[idx + 1] = lage_2
            idx = idx + 1

def sort_pair_by_lage(A_candidate, B_candidate):
    """
    Checks Lage of both candidates and puts Lage 1 before Lage 2.

    A_candidate, B_candidate: lists
    return: list of sorted candidates.
    """
    # vertical angle <= 200 means Lage 1 and >= 200 means Lage 2
    # TODO: if both are the same order in a specfic way or does it not matter?
    if A_candidate[2] <= 200 and B_candidate[2] >= 200:
        return (A_candidate, B_candidate)
    else:
        return (B_candidate, A_candidate)

def is_same_target(A_candidate, B_candidate):
    """
    Compare IDs to check if A and B are the same target.

    Returns are boolean.
    """

    if A_candidate[0] == B_candidate[0]:
        return True
    else: 
        return False
