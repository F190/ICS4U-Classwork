from typing import List, Dict


def add(a: int, b: int) -> int:
    """Add two integers.

    Args:
        a: an integer
        b: an integer
    Returns:
        The sum of the two integers
    """
    print(f"a: {a}")
    print(f"b: {b}")
    return a+b


def list_sum(alist: List[int]) -> int:

    """Gives the sum of a list

    Args:
        alist: A list of integers
    Returns:
        The sum of all the integers in the list
    """
    total = 0
    for i in alist:
        total += i
    return total


def count_occurances(words: List[str]) -> Dict:
    """Get occurances of words in a list

    Args:
        words: a list of strings
    Returns:
        A dictionary of the number of 
        occurances for each word in the list.
    """
    occurances = {}
    for word in words:
        if word not in occurances.keys():
            occurances[word] = 1
        else:
            occurances[word] += 1
    """
    try:
        occurances[word] += 1
    except KeyError:
        occurances[word] = 1
    """
    return occurances