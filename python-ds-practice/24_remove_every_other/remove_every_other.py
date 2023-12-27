def remove_every_other(lst):
    """Return a new list of other item.

        >>> lst = [1, 2, 3, 4, 5]

        >>> remove_every_other(lst)
        [1, 3, 5]

    This should return a list, not mutate the original:

        >>> lst
        [1, 2, 3, 4, 5]
    """
    every_other_list = []
    current_index = 0
    for number in lst:
        if current_index % 2 == 0:
            every_other_list.append(number)
        current_index += 1
    return every_other_list
