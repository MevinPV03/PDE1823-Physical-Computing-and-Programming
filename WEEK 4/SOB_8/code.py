def find_n_max(lst, n):
    """
    This function returns the nth largest element from a list.

    Parameters:
    lst (list): A list of numbers
    n (int): The position of the largest element to find

    Returns:
    int: The nth largest value in the list
    """
    sorted_list = sorted(lst, reverse=True)
    return sorted_list[n - 1]


# Example usage
mylist = [30, 21, 16, 66, 78, 109, 1, 4, 52]
nth_max = find_n_max(mylist, 3)

print("3rd largest element:", nth_max)