"""
Expects data of a Tachymeter.
Find pairs by comparing their IDs and sort them such that "Lage 1" is before
"Lage 2".
"""

def is_pair(A_candidate, B_candidate):
    """
    Extract and compare IDs of both input arguments.

    A_candidate, B_candidate: strings
    return: boolean, true if IDs are equal.
    """

    A_parts = A_candidate.split()
    B_parts = B_candidate.split()
    print(A_parts)
    print(B_parts)